import streamlit as st
from PIL import Image
import numpy as np
from deta import Deta
# img_file_buffer = st.camera_input("Take a picture")
deta = Deta(st.secrets["data_key"])
db = deta.Base("project_face_reg")
# if img_file_buffer is not None:

#     img = Image.open(img_file_buffer)


#     img_array = np.array(img)


#     st.write(type(img_array))

#     st.write(img_array.shape)
#     db.put({"pic": img_array})
# ________________________________________

with st.form("form"):
    name = st.text_input("Your name")
#     img = st.camera_input('Chụp ảnh')
    age = st.number_input('Your age')
    submitted = st.form_submit_button("Store in database")
if submitted:
    db.put({"key": name, "tuổi": age})
