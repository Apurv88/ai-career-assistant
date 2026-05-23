import importlib


def extract_text_from_pdf(file_path):
    text = ""

    try:
        import pdfplumber
    except ImportError:
        pdfplumber = None

    if pdfplumber is not None:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    try:
        from pypdf import PdfReader
    except ImportError:
        raise ImportError(
            "No PDF parser installed. Install 'pdfplumber' or 'pypdf' to use extract_text_from_pdf."
        )

    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text() or ""

    return text