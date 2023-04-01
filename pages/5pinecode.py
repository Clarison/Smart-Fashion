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

def input_query(img,num,index):
    #Initialize feature extractor 
    feature = fe.extract(img).tolist()
    
    #query index
    response = index.query(
    feature, 
    top_k=num)
    return response

def output(response, files_path):
    #Read the response and display image
    col1, col2, col3 = st.columns(3)
    i = 0
    for responses in response['matches']:
        i = i + 1
        if i == 1:
            with col1:
                image = Image.open(  files_path['{path}'.format(path = responses['id'])]  ) 
                st.image(image, caption='Score is {d_score}'.format(d_score = responses['score']))
        elif i == 2:
            with col2:
                image = Image.open(  files_path['{path}'.format(path = responses['id'])]  ) 
                st.image(image, caption='Score is {d_score}'.format(d_score = responses['score']))
        else:
            with col3:
                image = Image.open(  files_path['{path}'.format(path = responses['id'])]  ) 
                st.image(image, caption='Score is {d_score}'.format(d_score = responses['score']))
                i = 0   

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

index = intialize_pinecone()
file_path = load_imgpath()
if file2 and (num != 0) and run:
        st.image(file2, caption='Uploaded image')
        img = Image.open(file2)  # PIL image
        uploaded_img_path = r"./static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file2.name
        img.save(uploaded_img_path)
        response = input_query(img,num,index) 
        
        output(response, file_path)

        
        
