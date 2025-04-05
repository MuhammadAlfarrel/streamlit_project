import streamlit as st

st.title("Ini Streamlit Pertama Farrel")
st.write("Hello Streamlit, Welcome")

container = st.container()
with container:
    st.subheader("Container")
    st.write("Ini adalah container satu")
    st.write("Ini adalah container dua")
    st.write("Ini adalah container tiga")