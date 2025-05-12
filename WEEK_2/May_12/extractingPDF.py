import pymupdf as fitz  # import PyMuPDF

# open the PDF file

pdf_document = fitz.open("bob_magic_atm_story_fixed.pdf")

# loop through all the pages

for page_number in range(len(pdf_document)):
    # get the page
    page = pdf_document[page_number]

    # extract text from the page
    text = page.get_text()

    # print the text
    print(f"Page {page_number + 1}:\n{text}\n")

