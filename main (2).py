
import os
from google.colab import files
from pdf_utils import extract_text_from_pdf
from openai_utils import summarize_text_with_openai

# Uploading the PDF file directly in Google Colab
uploaded = files.upload()

pdf_file_name = "TRUE.pdf"
pdf_summary_text = extract_text_from_pdf(pdf_file_name)

# Summarize the text using OpenAI
pdf_summary = summarize_text_with_openai(pdf_summary_text)

# Saving the summary to a file in Google Colab
pdf_summary_file = pdf_file_name.replace(os.path.splitext(pdf_file_name)[1], "_summary.txt")
with open(pdf_summary_file, "w") as file:
    file.write(pdf_summary)

# Display the content of the summary file
with open(pdf_summary_file, "r") as file:
    print(file.read())

print(f"Summary saved to: {pdf_summary_file}")

# Downloading the summary file to local machine
files.download(pdf_summary_file)
