
import streamlit as st
import joblib
import os
# import urllib.request
import gdown

# model_url = "https://drive.google.com/uc?id=1TLwuRLBCQbQkKLI9-YKNzF78Y2q9JIdK"
file_id = "1TLwuRLBCQbQkKLI9-YKNzF78Y2q9JIdK"
model_path = "modells1.pkl"
download_url = f"https://drive.google.com/uc?id={file_id}"


st.info(f"Working directory: {os.getcwd()}")
# if not os.path.exists(model_path):
#     gdown.download(f"https://drive.google.com/uc?id={file_id}", model_path, quiet=False)
if not os.path.exists(model_path):
    try:
        st.info("Downloading model...")
        gdown.download(download_url, model_path, quiet=False)
        st.success("Download complete.")
    except Exception as e:
        st.error(f"Model download failed: {e}")
        st.stop()


if not os.path.exists(model_path):
    st.error("Model file still not found after download. Check if the link is valid or download failed.")
    st.stop()
try:
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()




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

