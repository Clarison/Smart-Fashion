import os
import openai
import streamlit as st

openai.api_key = "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"

def genimage(ask):
    try:
        response = openai.Image.create(
        prompt= ask,
        n=1,
        size="256x256"
        )
        image_url = response['data'][0]['url']
        st.image(image= image_url)
        
    except openai.error.OpenAIError as e:
        print(e.http_status)
        print(e.error)

ask = st.text_input(label='Enter the description of clothing you want to see')
run = st.button(label='Build', key='button1')

if run and ask != "":
    genimage(ask)
