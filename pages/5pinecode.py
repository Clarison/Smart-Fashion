import pinecone
import streamlit as st

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

def load_imgpath():
    root_dir = r'./static/img'
    # define dict
    files_path = {}
    
    #loop through the files 
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".jpg"):
                #Extract img path
                img_path = os.path.join(subdir, file)
                #Extract subdict name and file name
                subdirectory_name = os.path.basename(subdir)
                file_name = os.path.splitext(file)[0] # e.g., ./static/img/xxx.jpg
                
                #append to dict 
                files_path['{sub}_{file}'.format(sub = subdirectory_name, file = file_name)] = img_path
    return files_path


file2 = st.file_uploader(label='Upload image to search', type=['jpg','png','jpeg'], key='FileInput2')
num = st.number_input('Enter the number of images to match', min_value= 0, max_value=5, value=1, step=1)
run = st.button(label='Search', key='button2')
