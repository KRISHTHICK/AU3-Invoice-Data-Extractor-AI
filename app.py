import streamlit as st
from extractor import extract_text, extract_invoice_fields
from utils import pdf_to_images
from PIL import Image
import json
import os

st.set_page_config(page_title="Invoice Extractor AI", layout="wide")
st.title("🧾 Invoice Extractor AI")

uploaded = st.file_uploader("Upload Invoice (PDF/Image)", type=["pdf", "png", "jpg", "jpeg"])

if uploaded:
    with open("temp_input", "wb") as f:
        f.write(uploaded.getbuffer())

    st.subheader("Preview")
    if uploaded.name.endswith(".pdf"):
        imgs = pdf_to_images("temp_input")
    else:
        img = Image.open("temp_input")
        img.save("temp_image.png")
        imgs = ["temp_image.png"]

    for img_path in imgs:
        st.image(img_path, width=600)

        st.markdown("#### Extracted Text")
        text = extract_text(img_path)
        st.text_area("OCR Text", text, height=200)

        st.markdown("#### Extracted Fields")
        fields = extract_invoice_fields(text)
        st.json(fields)

        # Save as JSON
        output_file = f"output/extracted_{os.path.basename(img_path)}.json"
        with open(output_file, "w") as f:
            json.dump(fields, f, indent=4)
        st.success(f"Saved to {output_file}")
