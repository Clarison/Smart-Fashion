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


# Create a file uploader with a label and type of image
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# Check if an image was uploaded
if uploaded_file is not None:
    # Display the image
    st.image(uploaded_file)

    
# Run search
query = fe.extract(uploaded_file)
dists = np.linalg.norm(features-query, axis=1)  # L2 distances to features
ids = np.argsort(dists)[:30]  # Top 30 results
scores = [(dists[id], img_paths[id]) for id in ids]


st.write(scores)
        
st.write(features)
