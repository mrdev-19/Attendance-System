import streamlit as st

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    st.write(type(bytes_data))