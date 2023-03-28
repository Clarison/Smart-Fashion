from PIL import Image

# Load the image
image = Image.open('my_image.jpg')

# Resize the image
new_size = (500, 500)
image = image.resize(new_size)

# Display the image
st.image(image, caption='My Image')
