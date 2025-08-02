import pytesseract
import re
import cv2
from PIL import Image

def extract_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray)

def extract_invoice_fields(text):
    result = {}

    invoice_no = re.search(r'Invoice\s*(No|#):?\s*(\w+)', text, re.IGNORECASE)
    result["invoice_number"] = invoice_no.group(2) if invoice_no else "NA"

    date = re.search(r'Date\s*:?\s*([\d/.-]+)', text, re.IGNORECASE)
    result["date"] = date.group(1) if date else "NA"

    vendor = re.search(r'(Vendor|From):\s*(.+)', text, re.IGNORECASE)
    result["vendor"] = vendor.group(2).strip() if vendor else "NA"

    total = re.search(r'Total\s*:?\s*\$?\s*([\d.,]+)', text, re.IGNORECASE)
    result["total_amount"] = total.group(1) if total else "NA"

    return result
