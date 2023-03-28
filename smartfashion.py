import streamlit as st
from PIL import Image
import numpy as np
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path
from feature_extractor import FeatureExtractor


# Read image features
fe = FeatureExtractor()
st.write('prnt1')
features = []
st.write('prnt2')
img_paths = []
st.write('prnt3')
for feature_path in Path("./static/feature").glob("*.npy"):
    st.write('prnt4')
    features.append(np.load(feature_path))
    st.write('prnt5')
    img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
    st.write('prnt6')
features = np.array(features)

st.write('prnt7')
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit by Group 6! 👋")

st.write(features)

