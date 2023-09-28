from PyPDF2 import PdfReader, PdfWriter

reader1 = PdfReader("sample1_encrypted.pdf")
reader1.decrypt("12345")

writer = PdfWriter()
writer.append_pages_from_reader(reader1)

with open("sample1_decrypted.pdf", "wb") as out_file1:
    writer.write(out_file1)
