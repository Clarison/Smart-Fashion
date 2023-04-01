import streamlit as st
import requests
from PIL import Image
import numpy as np
import pinecone

# Set up Pinecone connection
pinecone.init(api_key="YOUR_API_KEY")
pinecone.create_index(index_name="image_embeddings", dimension=512)

# Set up Streamlit page
st.title("Image Search")
st.write("Upload an image to search for similar images")

# Get user input
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_column_width=True)

    # Convert the image to a vector using a pre-trained embedding model
    # Here, we're using ResNet50 as the embedding model
    model_url = "https://tfhub.dev/google/imagenet/resnet_v2_50/feature_vector/4?tf-hub-format=compressed"
    image_array = np.array(image)
    res = requests.post(model_url, json={"instances": image_array.tolist()})
    embedding = np.array(res.json()["predictions"])

    # Store the image embedding in Pinecone
    pinecone.index(index_name="image_embeddings").upsert(ids=[uploaded_file.name], vectors=[embedding])

    # Search for similar images in Pinecone
    query_results = pinecone.index(index_name="image_embeddings").query(queries=[embedding], top_k=5)

    # Display the similar images
    st.write("Similar images:")
    for result in query_results[0]:
        image_url = f"https://example.com/images/{result.id}"  # Replace with your image URL
        image = Image.open(requests.get(image_url, stream=True).raw)
        st.image(image, use_column_width=True)
