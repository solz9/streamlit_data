from bs4 import BeautifulSoup
import urllib2
import re
import numpy as np
import streamlit as st
img = st.camera_input('Take a picture')
st.image(img)
html_page = urllib2.urlopen("https://solz9-streamlit-data-data-q8uqz2.streamlit.app/")
soup = BeautifulSoup(html_page)
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))

st.write(images)
