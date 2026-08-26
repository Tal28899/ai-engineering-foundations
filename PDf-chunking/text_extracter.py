import pdfplumber as pf

def extract_text(file):
    "Takes a PDF file as input and returns the extracted text from all pages."
    try:
        text =""
        with pf.open(file) as f:
            for page in f.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n" 
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        raise


        