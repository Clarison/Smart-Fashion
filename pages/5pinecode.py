import pinecone

def intialize_pinecone():
    DATA_DIRECTORY = 'assignment4'
    INDEX_NAME = 'fashion'
    INDEX_DIMENSION = 4096
    BATCH_SIZE=200
    
    pinecone.init(api_key='deb8442d-d32a-4485-a5b7-35f577f68c01', environment='us-west4-gcp')
    # if the index does not already exist, we create it
    if INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(name=INDEX_NAME, dimension=INDEX_DIMENSION)
    # instantiate connection to your Pinecone index
    index = pinecone.Index(INDEX_NAME)
    
    return index
