import streamlit as st
from deta import Deta
import cv2
from PIL import Image
# import database
# deta = 'c0qy5dgedq2_SNHHnXR1972LBCNH5fcgizZzuaAT4XtA'
# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Your name")
    img = st.camera_input('Chụp ảnh')
    submitted = st.form_submit_button("Store in database")


# Connect to Deta Base with your Data Key
deta = Deta(st.secrets["data_key"])

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("key_reg")

# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    cv2_img = img.read()
    db.put({"name": name, "pic": cv2_img})
