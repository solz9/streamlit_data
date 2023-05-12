import streamlit as st
from deta import Deta
import cv2
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
    bytes_data = img.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    db.put({"name": name, "pic": cv2_img})
    """with open(cv2_img.name, "wb") as f:
            f.write(cv2_img.getbuffer())

# "---"
# "Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
