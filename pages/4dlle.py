import streamlit as st
import asyncio
from DALLE import DALLE

st.write('Hi there!')

# Instantiate DALLE model
dalle = DALLE("sess-xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# Define async function to generate images
async def generate_images(prompt):
    images = await dalle.generate(prompt)
    return images

# Define Streamlit app
def app():
    st.title("DALLE Image Generation App")

    # Get text prompt from user
    prompt = st.text_input("Enter a text prompt", "Kitten")

    # Generate images when the user clicks the button
    if st.button("Generate Images"):
        # Display loading message
        with st.spinner("Generating images..."):
            # Generate the images asynchronously
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            images = loop.run_until_complete(generate_images(prompt))

            # Display the images
            for image in images:
                st.image(image)

# Run the app
if __name__ == "__main__":
    app()
