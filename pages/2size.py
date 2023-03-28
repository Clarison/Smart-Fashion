import streamlit as st
from PIL import Image

st.title("Image Resizer")

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open uploaded image with PIL
    image = Image.open(uploaded_file)

    # Resize image to three different sizes
    small_image = image.resize((100, 100))
    medium_image = image.resize((300, 300))
    large_image = image.resize((500, 500))

    # Display resized images in columns
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.image(small_image, caption="Small (100x100)")
    with col2:
        st.image(medium_image, caption="Medium (300x300)")
    with col3:
        st.image(large_image, caption="Large (500x500)")
