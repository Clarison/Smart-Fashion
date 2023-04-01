import streamlit as st
import pinecone
import requests
from PIL import Image
from datetime import datetime
from feature_extractor import FeatureExtractor


pinecone.init(api_key="deb8442d-d32a-4485-a5b7-35f577f68c01", environment="us-west4-gcp")
# Connect to Pinecone index

pinecone.api_key = "deb8442d-d32a-4485-a5b7-35f577f68c01"
index_name="fashion"

index = pinecone.Index(index_name)
st.write("This is the list of index ",pinecone.list_indexes())
# Set up Streamlit app
st.title("Image Search with Pinecone")
file = st.file_uploader("Upload an image")

if file is not None:
    # Load image and resize
    img = Image.open(file)
    img = img.resize((224, 224))

    # Convert to bytes and encode as base64
    uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.name
    img.save(uploaded_img_path)

        # Run search
    fe = FeatureExtractor()
    query = fe.extract(img).tolist()
    st.write("This is the img_64 ",query)
    
  
    # Search index using Pinecone
    results = index.query(queries=[query], top_k=1)

    # Display results
    st.write("Top 5 results:")
    for result in results:
        if result.id is not None:
            url = result.id.decode("utf-8")
            score = result.score
            image = Image.open(requests.get(url, stream=True).raw)
            st.image(image, caption=f"Score: {score}")
          
