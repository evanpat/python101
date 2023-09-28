from PyPDF2 import PdfMerger, PdfReader

filename1 = "sample1.pdf"
filename2 = "sample2.pdf"

merger = PdfMerger()
merger.append(PdfReader(open(filename1, 'rb')))
merger.append(PdfReader(open(filename2, 'rb')))
merger.write("merged.pdf")

reader = PdfReader(filename1)
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)