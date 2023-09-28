from PyPDF2 import PdfReader

filename1 = "sample1.pdf"

reader = PdfReader(filename1)
page = reader.pages[0]
text = page.extract_text()

print(text)