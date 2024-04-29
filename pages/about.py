import streamlit as st
from PIL import Image

st.write("hello")

camera_image = st.camera_input("Camera")


if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(camera_image)