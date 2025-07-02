import fitz  # PyMuPDF

def process_pdf(pdf_path):
    doc = fitz.open(pdf_path)
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

if __name__ == "__main__":
    import sys
    print(process_pdf(sys.argv[1]))
