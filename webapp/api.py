import streamlit as st
import requests
from PIL import Image
import os
import sys
sys.path.append(str(os.getcwd()))
import base64

st.title("Anomaly Detection Web Application ")
st.write("Authors : Achour Simoud, Youssef M'hasni, Mohamed Amine Elkaout, Oussama Abdelmoula")
st.write(" ")
st.subheader("In this Anomaly Detection Project, we've utilized CIFAR-10 image data. The anomaly in this context is identified as instances belonging to the 'Airplane' class.")

# Display authors' names in the top-right corner

def webapp():
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        uploaded_image_bytes = uploaded_image.getvalue()
        base64_encoded = base64.b64encode(uploaded_image_bytes).decode('utf-8')
        col1, col2, col3 = st.columns(3)
        with col2:
            st.image(image, caption="Uploaded Image", use_column_width=False,width=300)
            response = requests.post(f"http://serving-api:8080/predict/",json={"data": base64_encoded})
            result = response.json().get("prediction")
            st.write(f"Prediction: {result}")
            real_value=st.text_input(label="Please enter '1' if the observed data is an anomaly or '0' if it is not")
        if st.button('Feedback'):
            st.write(f"Feedback received: {real_value}")
            requests.post(f"http://serving-api:8080/feedback/",json={"data": base64_encoded,"predicted_value": int(result), "real_value": int(real_value)})

if __name__ == "__main__":
    webapp()    


