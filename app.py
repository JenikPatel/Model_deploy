from fastai.vision.all import *
import streamlit as st
import pathlib, pathlib._local
import sys
if sys.platform == 'win32':
    pathlib.PosixPath = pathlib.WindowsPath
    pathlib._local.PosixPath = pathlib.WindowsPath
uploaded_image = st.file_uploader("Select a bear!", type = ["jpg", "jpeg", "png"])
st.write("This is my first website for model prediction!!!")
if uploaded_image is not None:
    img = PILImage.create(uploaded_image.getvalue())
    st.image(img, caption = "Your Uploaded Image")
    learn_inf = load_learner('export.pkl')
    pred, pred_indx, prob = learn_inf.predict(img)
    st.write(f"Prediction: {pred}; Probability: {prob[pred_indx]:.4f}")