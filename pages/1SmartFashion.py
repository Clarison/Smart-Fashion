import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
import streamlit as st
from pathlib import Path



        
# Read image features
fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
features = np.array(features)

for img_path in sorted(Path("./static/img").glob("*.jpg")):
        print(img_path)  # e.g., ./static/img/xxx.jpg
        feature = fe.extract(img=Image.open(img_path))
        feature_path = Path("./static/feature") / (img_path.stem + ".npy")  # e.g., ./static/feature/xxx.npy
        np.save(feature_path, feature)

def app():
    st.title("Smart Fashion Search Engine")
    st.write("Enter query image and find similar fashion images!")
    #st.write(features)
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
    
    if uploaded_file is not None:
        # Save query image
        img = Image.open(uploaded_file)  # PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + uploaded_file.name
        img.save(uploaded_img_path)

        # Run search
        query = fe.extract(img)
        dists = np.linalg.norm(features-query, axis=1)  # L2 distances to features
        ids = np.argsort(dists)[:30]  # Top 30 results
        scores = [(dists[id], img_paths[id]) for id in ids]

        # Display results
        st.image(uploaded_file, caption='Uploaded Image')
        st.write("Here are some similar fashion type , please give a check:")
        for score in scores:
            image = Image.open(score[1])
            st.image(np.array(image.resize((256,256))), caption=f"Distance: {score[0]}", use_column_width=True)

if __name__ == "__main__":
    app()
