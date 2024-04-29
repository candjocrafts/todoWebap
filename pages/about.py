import streamlit as st
from PIL import Image

st.write("hello")

img = st.camera_input("Camera")

gray_img = img.convert("L")

st.image(gray_img)