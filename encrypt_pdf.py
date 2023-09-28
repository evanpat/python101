from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("sample1.pdf")

writer = PdfWriter()
writer.append_pages_from_reader(reader)
writer.encrypt("12345")

with open("sample1_encrypted.pdf", "wb") as out_file:
    writer.write(out_file)
    
reader1 = PdfReader("sample1_encrypted.pdf")

# password = ["123", "234", "12345"]
# for i in password:
reader1.decrypt("12345")


writer = PdfWriter()
writer.append_pages_from_reader(reader1)

with open("sample1_decrypted.pdf", "wb") as out_file1:
    writer.write(out_file1)
