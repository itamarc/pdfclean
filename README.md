# PDFClean

The purpose of this repository is to develop a way to remove text with strikethrough from PDF files.

It will be used to clean PDF files with laws and other legal documents that have parts of it marked with strikethrough that corresponds to previous version of the document that is not in effect anymore.

## Config virtual environment

```bash
python -m venv pdfclean-venv
pdfclean-venv\Scripts\activate
```

## Test files

Test files were generated with the content from:

[https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l10.973.htm](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l10.973.htm)

## Current status

```
>py pdfcleantest.py

File: testfiles/L10973-ChromeSaveAsPDF.pdf
  Producer: Skia/PDF m138
  [extract_lines] >##### FAILURE
  [extract_annotation] >##### FAILURE

File: testfiles/L10973-CriarAdobePDF.pdf
  Producer: Adobe PDF Services
  [extract_lines] >##### FAILURE
  [extract_annotation] >##### FAILURE

File: testfiles/L10973-LibreOfficeExport.pdf
  Producer: LibreOffice 25.2.1.1 (X86_64) / LibreOffice Community
  [extract_lines] >!!!!! SUCCESS
  [extract_annotation] >##### FAILURE

File: testfiles/L10973-MicrosoftPrintToPDF.pdf
  Producer: Microsoft: Print To PDF
  [extract_lines] >##### FAILURE
  [extract_annotation] >##### FAILURE

File: testfiles/L10973-WordPublicarComoPDF.pdf
  Producer: Microsoft® Word para Microsoft 365
  [extract_lines] >##### FAILURE
  [extract_annotation] >##### FAILURE

File: testfiles/L10973-WordPublicarComoPDF_A.pdf
  Producer: Microsoft® Word para Microsoft 365
  [extract_lines] >##### FAILURE
  [extract_annotation] >##### FAILURE

File: testfiles/L10973-WordPublicarComoPDF_A_TamanhoMinimo.pdf
  Producer: Microsoft® Word para Microsoft 365
  [extract_lines] >##### FAILURE
  [extract_annotation] >##### FAILURE

File: testfiles/L10973-WordPublicarComoPDF_TamanhoMinimo.pdf
  Producer: Microsoft® Word para Microsoft 365
  [extract_lines] >##### FAILURE
  [extract_annotation] >##### FAILURE
  ```
