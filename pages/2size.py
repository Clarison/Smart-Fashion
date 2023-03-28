from PIL import Image

# Load the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])

# Resize the image
new_size = (500, 500)
uploaded_file = uploaded_file.resize(new_size)

# Display the image
st.image(uploaded_file, caption='My Image')
