# import streamlit as st
# from PIL import Image
# import numpy as np
# from deta import Deta
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# with st.form("form"):
#     name = st.text_input("Your name")
#     img_file_buffer = st.camera_input('Chụp ảnh')
#     submitted = st.form_submit_button("Store in database")

# deta = Deta(st.secrets["data_key"])
# db = deta.Base("project_face_reg")
# if submitted:
#     if img_file_buffer is not None:

#         img = Image.open(img_file_buffer)


#         img_array = np.array(img)

#         db.put({'key': name, "pic": img_array.tolist()})
/////////////////////////////////////////////////////////
import streamlit as st

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
