import pdfplumber as pf
def extract_text(file):
    text =""
    with pf.open(file) as f:
        for page in f.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n" 
    return text



        