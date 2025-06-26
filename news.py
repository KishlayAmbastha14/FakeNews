import streamlit as st
import joblib

model = joblib.load('modells1.pkl')


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

