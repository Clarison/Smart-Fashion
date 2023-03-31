import streamlit as st
import asyncio
from DALLE import DALLE


st.write('hi')
dalle = DALLE("sess-xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

async def generate_images(prompt):
    images = await dalle.generate(prompt)
    return images


st.title("DALLE Image Generation App")

    # Get text prompt from user
prompt = st.text_input("Enter a text prompt", "Kitten")

    # Generate images when the user clicks the button
    if st.button("Generate Images"):
        # Generate the images asynchronously
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        images = loop.run_until_complete(generate_images(prompt))
        st.write("Generating images...")

        # Display the images
        for image in images:
            st.image(image)
