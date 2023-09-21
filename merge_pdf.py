from PyPDF2 import PdfMerger, PdfFileReader
merger = PdfMerger()
merger.append(PdfFileReader(open(filename1, 'rb')))
merger.append(PdfFileReader(open(filename2, 'rb')))
merger.write("merged.pdf")