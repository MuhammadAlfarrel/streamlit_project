import streamlit as st
from PIL import Image
import numpy as np
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification

@st.cache_resource
def load_model():
    # 1) load processor & model dari HF
    processor = AutoImageProcessor.from_pretrained("Falcom/animal-classifier")
    model = AutoModelForImageClassification.from_pretrained("Falcom/animal-classifier")
    model.eval()
    return processor, model

processor, model = load_model()

def predict(pil_img: Image.Image):
    # 2) preprocess
    inputs = processor(images=pil_img, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)[0].cpu().numpy()
    # 3) ambil label & probabilitas
    labels = model.config.id2label  # dict: idx→class name
    sorted_idxs = np.argsort(probs)[::-1]
    top1 = sorted_idxs[0]
    return labels[top1], { labels[i]: float(np.round(probs[i]*100,2)) for i in sorted_idxs[:5] }

st.title("Nilik Kewan")
st.write("Masukkan foto hewan, saya akan tebak apa itu!")

uploaded = st.file_uploader("Upload gambar hewan", type=["jpg","jpeg","png"])
if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Input Image", use_column_width=True)
    if st.button("Predict"):
        cls, top_probs = predict(img)
        st.markdown(f"**Prediksi:** `{cls}`")
        st.markdown("**Top-5 Probabilitas:**")
        st.json(top_probs)
