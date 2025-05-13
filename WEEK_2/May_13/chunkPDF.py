import fitz # PyMuPDF
def chunk_pdf(file,chunks): # file is the path to the PDF file, chunks is the number of pages per chunk
    pdf=fitz.open(file) # open the PDF file
    full_text="" 
    for page in pdf: # iterate through the pages
        full_text+=page.get_text()
    pdf.close() # close the PDF file
    # split the text into chunks
    chunked_text = []
    for i in range(0, len(full_text), chunks):
        chunked_text.append(full_text[i:i+chunks])
    return chunked_text
# Example usage
file="bob.pdf" # path to the PDF file
chunks=15
chunked_text=chunk_pdf(file,chunks) # call the function
# print the chunked text
for i, chunk in enumerate(chunked_text):
    print(f"Chunk {i+1}:\n{chunk}\n")