from PIL import Image
import pytesseract


def extract_text(path, lang):
    return pytesseract.image_to_string(Image.open(path), lang=lang)
