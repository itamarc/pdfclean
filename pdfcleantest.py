import fitz  # PyMuPDF
from PyMuPDFtest import extract_text_without_strikethrough_lines, extract_text_without_strikethrough_annotation

CONFIG_FILE = "pdf_files.txt"

def count_art_1o(conteudo):
    return conteudo.count("Art. 1º")

with open(CONFIG_FILE, "r") as f:
    pdf_files = [line.strip() for line in f if line.strip()]

for pdf_path in pdf_files:
    print(f"\nFile: {pdf_path}")
    try:
        doc = fitz.open(pdf_path)
        print(f"  Producer: {doc.metadata['producer']}")

        # Teste com extract_text_without_strikethrough_lines
        result_lines = extract_text_without_strikethrough_lines(doc)
        art_count_lines = count_art_1o(result_lines)
        if art_count_lines == 1:
            print("  [extract_lines] >!!!!! SUCCESS")
        else:
            print("  [extract_lines] >##### FAILURE")

        # Teste com extract_text_without_strikethrough_annotation
        result_annot = extract_text_without_strikethrough_annotation(doc)
        art_count_annot = count_art_1o(result_annot)
        if art_count_annot == 1:
            print("  [extract_annotation] >!!!!! SUCCESS")
        else:
            print("  [extract_annotation] >##### FAILURE")
    except Exception as e:
        print(f"  Error: {e}")
