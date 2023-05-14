from bs4 import BeautifulSoup
import urllib.request as urllib2
import requests
import re
import numpy as np
import streamlit as st
img = st.camera_input('Take a picture')
if img is not None:
    st.image(img)   
