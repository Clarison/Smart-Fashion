import streamlit as st
import torch
from dalle_pytorch import OpenAIDiscreteVAE, DALLE
from dalle_pytorch.tokenizer import tokenizer


vae = OpenAIDiscreteVAE()
dalle = DALLE(vae = vae)
dalle.load('dalle.pt')

st.title("DALL-E Text-to-Image Generator")

    # Ask the user for some text input
text = st.text_input("Enter some text:")

    # Generate an image from the text
image = dalle.generate_images(text)

    # Display the image
st.image(image)

