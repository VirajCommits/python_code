# from PyPDF2 import PdfReader

# def extract_information(pdf_path):
#     with open(pdf_path, 'rb') as f:
#         pdf = PdfReader(f)
#         # information = pdf.getDocumentInfo()
#         information=pdf.metadata
#         # number_of_pages = pdf.getNumPages()
#         number_of_pages = len(pdf.pages)

#     txt = f"""
#     Information about {pdf_path}: 

#     Author: {information.author}
#     Creator: {information.creator}
#     Producer: {information.producer}
#     Subject: {information.subject}
#     Title: {information.title}
#     Number of pages: {number_of_pages}
#     """

#     print(txt)
#     return information

# if __name__ == '__main__':
#     path = 'MATH215_in-class_lecture4.1_annotated.pdf'
#     extract_information(path)


import PyPDF2

# Open the PDF file in 'read binary' mode
with open('MATH215_in-class_lecture4.3_annotated.pdf', 'rb') as file:
    # Create a PyPDF2 PdfFileReader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Get the number of pages in the PDF file
    # num_pages = pdf_reader.getNumPages()
    num_pages = len(pdf_reader.pages)
    
    # Loop through each page in the PDF file and extract its text
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()
        print(page_text)
        # for i in page_text:
            # print(i)
        break