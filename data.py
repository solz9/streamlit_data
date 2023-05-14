from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import numpy as np
import streamlit as st
imgs = st.camera_input('Take a picture')
if imgs is not None:
    img = st.image(imgs)

    st.download_button(img)
# print(images)
