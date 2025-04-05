import streamlit as st
import numpy as np
from PIL import Image
import cv2
import tensorflow as tf

# Load model
model = tf.keras.models.load_model("model_cnn.h5")  # pastikan file model.h5 sudah ada

# Label kelas
class_names = ['NORMAL', 'PNEUMONIA']

def predict_image_streamlit(img_pil):
    img = img_pil.convert('RGB')
    img = img.resize((224, 224))  # sesuaikan dengan input shape model
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]  # ambil angka float-nya aja

    predicted_class = class_names[int(prediction > 0.5)]

    probabilities = {
        "PNEUMONIA": float(prediction),
        "NORMAL": float(1 - prediction)
    }

    return {
        "class": predicted_class,
        "probabilities": probabilities
    }

st.title("Deteksi XRAY Penumonia")
st.write("Hallo Pals , ini adalah project saya mencoba untuk membuat project pendeteksi penumonia berdasarkan hasil XRAY Paru-paru manusia")
st.write("Disini saya menggunakan model yang sudah dibuat oleh Luis Jose Mendez, berikut dokumentasinya")
st.markdown("""
            <div style="margin-bottom:10px">
                <a href="https://github.com/mendez-luisjose/Covid-19-and-Pneumonia-Recognition-with-X-Ray-Streamlit-CNN-and-TensorFlow/tree/main" target="_blank">
                    <button style="background-color:#3b5998; color:white; padding:10px 20px; border:none; border-radius:5px; width:200px;">
                        Luis Jose Mendez Documentation
                    </button>
                </a>
            </div>
            """, unsafe_allow_html=True)

uploaded_files = st.file_uploader(
    "Input Foto Xraynya", accept_multiple_files=True, type=["jpg", "jpeg", "png"]
)
for uploaded_file in uploaded_files:
    st.write("filename:", uploaded_file.name)
    img = Image.open(uploaded_file)
    st.image(img, caption=uploaded_file.name)

if uploaded_files:
    st.subheader("GASS DI PREDICTT:")
    predict_button = st.button("PREDICT", type="primary")

    if predict_button:
        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file)
            st.image(img, caption=uploaded_file.name)

            # Panggil fungsi prediksi
            result = predict_image_streamlit(img)

            # Tampilkan hasil
            st.write(f"🔍 **Prediksi Akhir**: `{result['class']}`")
            st.write("📊 Probabilitas:")
            st.json(result["probabilities"])

            
            

