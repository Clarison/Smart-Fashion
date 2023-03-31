import streamlit as st
import asyncio
from DALLE import DALLE

dalle = DALLE("sess-xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

async def generate_images(prompt):
    images = await dalle.generate(prompt)
    return images

def app():
    st.title("DALLE Image Generation App")

    # Get text prompt from user
    prompt = st.text_input("Enter a text prompt", "Kitten")

    # Generate images when the user clicks the button
    if st.button("Generate Images"):
        # Generate the images asynchronously
        task = asyncio.create_task(generate_images(prompt))
        st.write("Generating images...")

        # Wait for the images to be generated
        images = await task

        # Display the images
        for image in images:
            st.image(image)
