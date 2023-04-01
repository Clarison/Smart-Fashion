import streamlit as st
import pinecone
import requests
from PIL import Image

# Connect to Pinecone index
pinecone_index_name = "image-search"
pinecone.api_key = "deb8442d-d32a-4485-a5b7-35f577f68c01"
pinecone_index = pinecone.Index(index_name= pinecone_index_name)

# Set up Streamlit app
st.title("Image Search with Pinecone")
file = st.file_uploader("Upload an image")

if file is not None:
    # Load image and resize
    img = Image.open(file)
    img = img.resize((224, 224))

    # Convert to bytes
    img_bytes = img.tobytes()

    # Search index using Pinecone
    results = pinecone_index.query(queries=[img_bytes], top_k=5)

    # Display results
    st.write("Top 5 results:")
    for result in results[0]:
        url = result.id.decode("utf-8")
        score = result.score
        image = Image.open(requests.get(url, stream=True).raw)
        st.image(image, caption=f"Score: {score}")