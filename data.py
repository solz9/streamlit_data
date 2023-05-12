import streamlit as st
from PIL import Image
import numpy as np
from deta import Deta
with st.form("form"):
    name = st.text_input("Your name")
    img_file_buffer = st.camera_input('Chụp ảnh')
    submitted = st.form_submit_button("Store in database")

deta = Deta(st.secrets["data_key"])
db = deta.Base("project_face_reg")
if submitted:
    if img_file_buffer is not None:

        img = Image.open(img_file_buffer)


        img_array = np.array(img)

        db.put({'key': name, "pic": img_array.tolist()})

