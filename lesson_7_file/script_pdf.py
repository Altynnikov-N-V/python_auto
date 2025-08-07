from pypdf import PdfReader

reader = PdfReader("tmp/Tests.pdf")
print(reader.pages)
print(len(reader.pages))

text=reader.pages[0].extract_text()
print(text)
assert "Мама мыла раму" in text

