import streamlit as st
from PIL import Image

# Set up Streamlit app
st.set_page_config(page_title="Image Resizer", layout="wide")
st.title("Image Resizer")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# If image is uploaded
if uploaded_file is not None:
    # Open uploaded image with Pillow
    img = Image.open(uploaded_file)

    # Display original image
    st.subheader("Original Image")
    st.image(img, use_column_width=True)

    # Display image in different sizes
    st.subheader("Resized Images")
    for size in [100, 200, 500]:
        resized_img = img.resize((size, size))
        st.image(resized_img, caption=f"{size} x {size}", use_column_width=True)
