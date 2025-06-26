## https://drive.google.com/uc?id=1TLwuRLBCQbQkKLI9-YKNzF78Y2q9JIdK

import streamlit as st
import joblib
import os
import urllib.request


model_url = "https://drive.google.com/uc?id=1TLwuRLBCQbQkKLI9-YKNzF78Y2q9JIdK"
model_path = "modells1.pkl"


if not os.path.exists(model_path):
    urllib.request.urlretrieve(model_url, model_path)

model = joblib.load(model_path)

st.markdown("""
   <h1 style='color:#53299F;'> Fake News Detection</h1>

""",unsafe_allow_html=True)

st.markdown("<h5 style='color: teal;'>Enter a short news snippet to check if it's real or fake</h5>", unsafe_allow_html=True)
input_text = st.text_area("")


if st.button("predict"):
  if input_text.strip() == "":
    st.warning("Please enter some text")

  else:
    prediction = model.predict([input_text])

    if prediction[0] == 1:
      st.success("This is Real News")

    else:
      st.error("This is Fake News")

