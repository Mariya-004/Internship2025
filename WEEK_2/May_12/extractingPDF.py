import pymupdf as fitz  # import PyMuPDF

# open the PDF file
def open_pdf(file_path):
    
    pdf_document = fitz.open(file_path)  # open the PDF file

    # loop through all the pages

    for page_number in range(len(pdf_document)):
        # get the page
        page = pdf_document[page_number]

        # extract text from the page
        text = page.get_text()

        # print the text
        print(f"Page {page_number + 1}:\n{text}\n")
    # close the PDF document
    pdf_document.close()

# Example usage
file_path = "bob_magic_atm_story_fixed.pdf"
open_pdf(file_path)
