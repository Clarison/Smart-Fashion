import streamlit as st
from PIL import Image
import numpy as np

segm = Image.open(f)

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit by Group 6! 👋")

segm = Image.open(f)
