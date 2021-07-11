
def pdf_reader():
    book = open('py3.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numpages
    speak(f"Total number of pages in a book{pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
