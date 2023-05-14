# Imports
import streamlit as st
from deta import Deta
import io
DETA_KEY = "c0ub5ly8vj3_NXGqau6ih8xRuPk1jyeD5uFUPyMTk4ck" # Secret key to connect to deta drive
deta = Deta(DETA_KEY) # Initialize deta object with a project key

drive = deta.Drive("face_registration") # Connecting to the Deta drive
with st.form("my_form"):
    name = st.text_input('nhập tên')
    # Here i'm taking the input from `st.file_uploader`, same principle can be  applied.
    uploaded_files = st.camera_input("Choose photos to upload")
    st.set_option('deprecation.showfileUploaderEncoding', False) # Enabling the automatic file decoder
    submitted = st.form_submit_button("Submit")
    if submitted:
        file = io.BytesIO(b'this is a byte string')
        pic_names = [] # Later used for deleting the local files after being uploaded
        for uploaded_file in uploaded_files: # Iterating over each file uploaded
            file = io.BytesIO(uploaded_file)
            file = file.read() # Read the data
            image_result = open(uploaded_file.name, 'wb') # creates a writable image and later we can write the decoded result
            image_result.write(file) # Saves the file with the name uploaded_file.name to the root path('./')
            pic_names.append(uploaded_file.name) # Append the name of image to the list
            image_result.close() # Close the file pointer

        for i in range(len(pic_names)): # Iterating over each file name
            names = name # Getting the name of current file
            path ='./'+pic_names[i] # Creating path string which is basically ["./image.jpg"]
            drive.put(names, path=path) # so, we have our file name and path, so uploading images to the drive
            os.remove(pic_names[i]) # Finally deleting it from root folder
        st.success('Thanks for uploading!') # Success message
