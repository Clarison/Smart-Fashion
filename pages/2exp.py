import streamlit as st
import numpy as np
from pathlib import Path
from PIL import Image
from feature_extractor import FeatureExtractor

# Read image features
fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
features = np.array(features)

# Define the Streamlit app
def app():
    # Set the app title and description
    st.set_page_config(page_title="Hello", page_icon="👋")
    st.write("# Welcome to Streamlit by Group 6! 👋")
    st.write("This app allows you to search for similar images from a collection of pictures.")

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

        # Display the search results
        st.write("Top 30 similar images:")
        for score in scores:
            st.image(score[1], caption=f"Distance: {score[0]}")

# Run the Streamlit app
if __name__ == "__main__":
    app()
