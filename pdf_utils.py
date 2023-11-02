
import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file_name):
    pdf_summary_text = ""

    with open(pdf_file_name, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)

        for page_num in range(len(pdf_reader.pages)):
            page_text = pdf_reader.pages[page_num].extract_text().lower()
            pdf_summary_text += page_text + "\n"

    return pdf_summary_text
