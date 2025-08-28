import streamlit as st
from PIL import Image

from mapping import get_bin_info 
from inference import run_inference



# Streamlit UI
st.set_page_config(page_title="Smart Waste Classifier", page_icon="🗑️", layout="centered")
st.title(" Smart Waste Classification")
st.write("Upload or capture a waste item image and I’ll suggest the right bin.")

# Upload or capture image
uploaded_file = st.file_uploader("Upload a waste image", type=["jpg", "jpeg", "png"])
camera_input = st.camera_input("Or take a photo")

# Decide which image to use
img_source = uploaded_file if uploaded_file else camera_input
print("image uploded ",type(img_source)) 

if img_source:
    image = Image.open(img_source)
    st.image(image, caption="Your Image", use_column_width=True)
    print(" image pil ", type(image))

    # YOLO inference 

    detected_classes = run_inference(image,0.2)
    if detected_classes == "No object detected":
        st.success(f" Detected: ** No dedection is possible at this moment for the object you choosed this will be added in further update **")
        st.info(f" Suggested Bin: ** No suggestions at the moment **")
    else:
        for detected_class in detected_classes:
            bin_suggestion = get_bin_info(detected_class)
            st.success(f" Detected: **{detected_class}**")
            st.info(f"Suggested Bin: **{bin_suggestion}**")
        
        


    
