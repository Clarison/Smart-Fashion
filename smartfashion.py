import streamlit as st
from PIL import Image
import numpy as np
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path
from feature_extractor import FeatureExtractor

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)       
  
    
st.write("# Welcome to Streamlit by Group 6! 👋")

# Read image features
fe = FeatureExtractor()

for img_path in sorted(Path("./static/img").glob("*.jpg")):
        print(img_path)  # e.g., ./static/img/xxx.jpg
        feature = fe.extract(img=Image.open(img_path))
        feature_path = Path("./static/feature") / (img_path.stem + ".npy")  # e.g., ./static/feature/xxx.npy
        np.save(feature_path, feature)
        

features = []
img_paths = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
features = np.array(features)





st.write(features)
