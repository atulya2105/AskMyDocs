from pypdf import PdfReader

def read_pdf(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""
        
        # clean text
        text = text.replace("\n", " ")
        text = " ".join(text.split())

    except Exception as e:
        print("PDF Error:", e)

    return text