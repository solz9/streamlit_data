# Khang Trương
import streamlit as st
from PIL import Image
from deta import Deta
# from numpy import asarray
# Step 4: Capture the image using st.camera_input()
image = st.camera_input('take picture')
n = st.image(image)
# Step 5: Convert the image data to a suitable format (e.g., bytes)
# image_bytes = n.read()
# st.write(image.format)



# response = requests.get(url)
# img = Image.open(BytesIO(response.content))
# numpydata = asarray(image_bytes)

# st.write(img)
 
#  shape
# print(numpydata.shape)
# Step 6: Initialize the Deta base
# deta = Deta(st.secrets["data_key"])
# db = deta.Base("key_reg")
# Step 7: Save the image data to the Deta base
# db.put(image_bytes, 'image.jpg')

# Display a success message
st.success('Image saved to Deta database!')
# ___________________________________________
# import database
# deta = 'c0qy5dgedq2_SNHHnXR1972LBCNH5fcgizZzuaAT4XtA'
# Data to be written to Deta Base
# with st.form("form"):
#     name = st.text_input("Your name")
#     img = st.camera_input('Chụp ảnh')
#     submitted = st.form_submit_button("Store in database")


# # Connect to Deta Base with your Data Key
# deta = Deta(st.secrets["data_key"])

# # Create a new database "example-db"
# # If you need a new database, just use another name.
# db = deta.Base("key_reg")

# # If the user clicked the submit button,
# # write the data from the form to the database.
# # You can store any data you want here. Just modify that dictionary below (the entries between the {}).
# if submitted:
#     st.write(img.read())
#     db.put({"name": name, "pic": cv2_img})
