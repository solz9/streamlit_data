import streamlit as st
import cv2
import pandas as pd
import numpy as np
import face_recognition
from deta import Deta

DETA_KEY = "c0qy5dgedq2_7aSU1pPYRdDoNvwmqdwwVUDZLUGz3mpU"
deta = Deta(DETA_KEY) 
base = deta.Base("face_reg_project")

hs = pd.read_excel('DS_10Ly4 - Copy.xlsx')
gv = pd.read_excel('passgv.xlsx')
hs = hs.drop(columns=['Họ và tên đệm', 'Tên'])
name = hs['Họ và tên'].values.tolist()
name = [name[i].lower() for i in range(len(name))]
hs['họ và tên'] = name

# def face_input_regis():
y = st.text_input('Nhập họ và tên').lower()
x = st.text_input("Nhập mật khẩu", type="password")
uploaded_file = st.camera_input("Lấy ảnh")
st.set_option('deprecation.showfileUploaderEncoding', False)
df1 = hs[hs['họ và tên'] == y]
if st.button('Enter'):
    if df1['Password'].values != x:
        st.warning('Bạn đã nhập sai Password hoặc họ và tên, vui lòng nhập lại')
    else:
        if uploaded_file:
            bytes_data = uploaded_file.getvalue()
            cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            faceframe = face_recognition.face_locations(cv2_img)
            img_encode = face_recognition.face_encodings(cv2_img, faceframe)[0]
            base.put({'key':y, 'pic':img_encode.tolist()})
