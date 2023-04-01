import os
import pinecone
from feature_extractor import FeatureExtractor

# Initialize Pinecone
pinecone.init(api_key="deb8442d-d32a-4485-a5b7-35f577f68c01", environment="us-west4-gcp")

# Connect to Pinecone index
pinecone.api_key = "deb8442d-d32a-4485-a5b7-35f577f68c01"
index_name = "fashion"
index = pinecone.Index(index_name)

# Create a feature extractor instance
fe = FeatureExtractor()

# Set the path to the folder containing the images
image_folder = "./static/img"

# Loop over the images in the folder
for file_name in os.listdir(image_folder):
    # Load the image and extract features
    img_path = os.path.join(image_folder, file_name)
    features = fe.extract_from_path(img_path)

    # Upload the features to Pinecone
    index.upsert(ids=file_name, embeddings=features)

# Print the list of IDs in the index
print(index.list_ids())
