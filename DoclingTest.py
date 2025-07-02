from docling.document_converter import DocumentConverter

source = "D:\\itamar.iac\\BDCrim\\IT\\41\\IT 29-2016 - DITEC - CONSOLIDADA.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"
