import streamlit as st

    # Using object notation
    # add_selectbox = st.sidebar.selectbox(
    #     "How would you like to be contacted?",
    #     ("Email", "Home phone", "Mobile phone")
    # )

    # Using "with" notation
    # with st.sidebar:
    #     add_radio = st.radio(
    #         "Choose a shipping method",
    #         ("Standard (5-15 days)", "Express (2-5 days)")
    # )

st.title("Welcome to my Streamlite Page")

container = st.container()
with container:
    st.header("About Me")
    col1, col2 = st.columns(2)
    with col1:
        st.image("fotofarrel.jpeg", width = 2000)
    with col2:
        st.write("""Hallo! Nama saya Muhammad Alfarrel Arya Mahardika,
                  Saya adalah seorang Mahasiswa di Politeknik Elektronika Negeri Surabaya dan
                  sekarang sedang belajar di Program Studi Teknik Komputer""", )
        st.subheader("Berikut Data diri saya")
        st.write("Nama : Muhammad Alfarrel Arya Mahardika")
        st.write("Tempat, Tanggal Lahir : Malang, 6 Mei 2004")
        st.write("Alamat : Jl. Veteran 1A No. 14A, Pasuruan")
        
    st.subheader("Berikut Page sosial media saya:")
    st.markdown("""
            <div style="margin-bottom:10px">
                <a href="https://www.facebook.com/alfarrel.mahardika" target="_blank">
                    <button style="background-color:#3b5998; color:white; padding:10px 20px; border:none; border-radius:5px; width:200px;">
                        Facebook 
                    </button>
                </a>
            </div>
            <div style="margin-bottom:10px">
                <a href="https://www.instagram.com/_alfarrelm_/" target="_blank">
                    <button style="background-color:#E1306C; color:white; padding:10px 20px; border:none; border-radius:5px; width:200px;">
                        Instagram 
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)
    

