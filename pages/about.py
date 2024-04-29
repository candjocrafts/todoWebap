import streamlit as st
from PIL import Image, ImageOps

st.write("hello")

camera_image = st.camera_input("Camera")


if camera_image:
    img = Image.open(camera_image)
    gray_img = ImageOps.grayscale(img)
    st.image(gray_img)