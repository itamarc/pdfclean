import os
from PyMuPDFtest import process_pdf

CONFIG_FILE = "pdf_files.txt"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(CONFIG_FILE, "r") as f:
    pdf_files = [line.strip() for line in f if line.strip()]

for pdf_path in pdf_files:
    try:
        result = process_pdf(pdf_path)
        base = os.path.basename(pdf_path)
        out_path = os.path.join(OUTPUT_DIR, base + ".txt")
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(result)
        print(f"Processed: {pdf_path} -> {out_path}")
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
    