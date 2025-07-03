import fitz  # PyMuPDF

def extract_text_without_strikethrough_annotation(doc):
    result = []

    for page in doc:
        # 1. Coletar retângulos das anotações de strikethrough
        st_rects = []
        for annot in page.annots(types=[fitz.PDF_ANNOT_STRIKE_OUT]):
            st_rects.append(annot.rect)

        # 2. Extrair todas as palavras da página com suas coordenadas
        words = page.get_text("words")  # cada item: (x0, y0, x1, y1, "palavra", ...)

        # 3. Filtrar palavras que NÃO estão sob nenhum retângulo de strikethrough
        filtered_words = []
        for w in words:
            wrect = fitz.Rect(w[:4])
            # Se a palavra NÃO intersecta nenhum retângulo de strikethrough, mantemos
            if not any(wrect.intersects(rect) for rect in st_rects):
                filtered_words.append(w[4])  # w[4] é o texto da palavra

        # 4. Recompor o texto da página (simplesmente juntando as palavras)
        result.append(" ".join(filtered_words))

    return "\n\n".join(result)

def is_horizontal(line, tolerance=2):
    x0, y0, x1, y1 = line
    return abs(y0 - y1) < tolerance and abs(x0 - x1) > 10  # linha horizontal longa

def get_horizontal_lines(page):
    lines = []
    for item in page.get_drawings():
        for path in item["items"]:
            if path[0] == "l":  # 'l' indica linha
                x0, y0 = path[1]
                x1, y1 = path[2]
                if is_horizontal((x0, y0, x1, y1)):
                    lines.append((x0, y0, x1, y1))
    return lines

def words_crossed_by_line(words, line, tolerance=2):
    x0, y0, x1, y1 = line
    crossed_idxs = set()
    for idx, w in enumerate(words):
        wx0, wy0, wx1, wy1, text = w[:5]
        # Verifica se a linha cruza a caixa da palavra
        if (wx0 <= x0 <= wx1 or wx0 <= x1 <= wx1 or (x0 <= wx0 and x1 >= wx1)):
            if wy0 - tolerance <= y0 <= wy1 + tolerance:
                crossed_idxs.add(idx)
    return crossed_idxs

def extract_text_without_strikethrough_lines(doc):
    all_text = []
    for page in doc:
        words = page.get_text("words")  # (x0, y0, x1, y1, "texto", ...)
        lines = get_horizontal_lines(page)
        # Descobrir índices das palavras tachadas
        striked_idxs = set()
        for line in lines:
            striked_idxs |= words_crossed_by_line(words, line)
        # Montar texto sem as palavras tachadas
        filtered_words = [w[4] for idx, w in enumerate(words) if idx not in striked_idxs]
        page_text = " ".join(filtered_words)
        all_text.append(page_text)
    return "\n\n".join(all_text)

# Processa um PDF e remove palavras tachadas, retornando o texto limpo
if __name__ == "__main__":
    import sys
    print(extract_text_without_strikethrough_annotation(sys.argv[1]))
