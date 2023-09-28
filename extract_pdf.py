# get_doc_info.py
from PyPDF2 import PdfReader

def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        #info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        print(number_of_pages)
        # author = info.author
        # creator = info.creator
        # producer = info.producer
        # subject = info.subject
        # title = info.title

if __name__ == '__main__':
    path = 'sample1.pdf'
    get_info(path)