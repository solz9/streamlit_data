import streamlit as st
from deta import Deta
# import database
# deta = 'c0qy5dgedq2_SNHHnXR1972LBCNH5fcgizZzuaAT4XtA'
# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Your name")
    age = st.number_input("Your age")
    submitted = st.form_submit_button("Store in database")


# Connect to Deta Base with your Data Key
deta = Deta(st.secrets["data_key"])

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("project_face_reg")

# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"key": name, "age": age})

"---"
"Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
# db_content = db.fetch().items
st.write(db.get('Dương Huệ Mẫn'))
