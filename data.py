# Khang Trương
import streamlit as st
from PIL import Image
import deta

# Step 4: Capture the image using st.camera_input()
image = st.camera_input('take picture')

# Step 5: Convert the image data to a suitable format (e.g., bytes)
image_bytes = image.read()

# Step 6: Initialize the Deta base
deta = Deta(st.secrets["data_key"])
db = deta.Base("key_reg")
# Step 7: Save the image data to the Deta base
db.put(image_bytes, 'image.jpg')

# Display a success message
st.success('Image saved to Deta database!')
