import streamlit as st
from keras.models import load_model
from keras.applications.vgg16 import VGG16
import joblib
import numpy as np
from PIL import Image

def predict_image_streamlit(pil_img):
    animals = ['butterflies', 'chickens', 'elephants', 'horses', 'spiders', 'squirells']

    img_resized = pil_img.resize((224, 224)).convert("RGB")
    img_array = np.array(img_resized)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    features = vgg16.predict(img_array)  # ekstrak fitur
    preds = model.predict_proba(features)  # prediksi probabilitas
    class_pred = model.predict(features)[0]

    # Balikkan hasil prediksi
    result = {
        "class": animals[class_pred],
        "probabilities": dict(zip(animals, np.round(preds[0] * 100, 2)))
    }
    return result

st.title("Nilik Kewan")
st.write("Hallo Pals , ini adalah project saya untuk mengenali hewan apakah yang kamu input dibawah ini")
st.write("Gas Di Tilik")

uploaded_files = st.file_uploader(
    "Input Foto Hewan", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

if uploaded_files:
    st.subheader("GASS DI PREDICTT:")
    st.button("PREDICT", type="primary")

    if st.button("PREDICT", type="primary"):
        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file)
            st.image(img, caption=uploaded_file.name, use_column_width=True)

            # Panggil fungsi prediksi
            result = predict_image_streamlit(img)

            # Tampilkan hasil
            st.write(f"🔍 **Prediksi Akhir**: `{result['class']}`")
            st.write("📊 Probabilitas:")
            st.json(result["probabilities"])
            
            

