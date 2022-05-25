import streamlit as st
import pandas as pd
import numpy as np
# import plotly_express as px
from PIL import Image
import streamlit.components.v1 as components
# import matplotlib.pyplot as plt
from tensorflow import keras
import joblib
import operator
import sys

# import mediapipe as mp
import main
import requests
from streamlit_lottie import st_lottie
from annotated_text import annotated_text

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose
# website_icon = Image.open('MyGymBuddy.jpg')   

st.set_page_config(
    page_title='healcv',
    )

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.applications.mobilenet import decode_predictions

from PIL import Image
sys.modules['Image'] = Image 
# [theme]
base="light"
primaryColor="purple"

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

model = keras.models.load_model('fcvmodel.h5')
dbfood = pd.read_csv('dbfood.csv',sep=";")
food = dbfood['nama'].tolist()

def getPrediction(data,model):
    img = Image.open(data)
    newsize = (224, 224)
    image = img.resize(newsize)
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    yhat = model.predict(image)
    label = yhat[0]
    prob = []
    for i in range(len(label)):
        # prob.append(i)
        prob.append(np.round(label[i]*100,2))
    data = {'nama': food, 'prob': prob}
    dfhasil = pd.DataFrame.from_dict(data)
    top3 = dfhasil.nlargest(3, 'prob')
    # top = dict(zip(food, prob))
    # top3 = dict(sorted(top.items(), key=operator.itemgetter(1), reverse=True)[:3])
    return top3

# st.set_page_config(layout='wide')

menu = ["Food Analyzer","Fitness Exercise"]
choice = st.sidebar.selectbox("Select Menu", menu)

if choice == "Food Analyzer":
    st.subheader("Heal - Food Analyzer")
    c1, c2 = st.columns([1, 1])
    with c1:
        with st.expander('Open Camera'):
            data1 = st.camera_input('')
    with c2:
        with st.expander('Upload from file'):
            data2 = st.file_uploader('Upload Photo')

    if data1 == None and data2 == None:
        st.write('Take or upload a photo of food to analyze')
        data = None
    elif data1 == None:
        data = data2
    else:
        data = data1

    if data == None:
        pass
    else:
        img = Image.open(data)
        newsize = (280, 230)
        image = img.resize(newsize)
        st.image(image)

        hasil = getPrediction(data,model)
        top = hasil.nlargest(1, 'prob')
        dfk = pd.merge(hasil,dbfood,how='left',on='nama')
        dfk['Protein'] = dfk['protein']*dfk['prob']/100
        dfk['Lemak'] = dfk['lemak']*dfk['prob']/100
        dfk['Karbohidrat'] = dfk['karbohidrat']*dfk['prob']/100
        dfk['Kkal'] = dfk['kkal']*dfk['prob']/100
        dfk['Score'] = dfk['skor']*dfk['prob']/100
        tingkat = dfk['Score'].tolist()
        total= tingkat[0]+tingkat[1]+tingkat[2]
        risiko = None
        if total >450:
            risiko = 'High risk to consume'
        elif total >250:
            risiko = 'Medium risk to consume'
        elif total >105:
            risiko = 'Low risk to consume'
        else:
            risiko = 'Safe to consume'
        top1 = top['nama'].tolist()
        st.subheader(top1[0])
        st.write(f'Risk for people with Diabetes/Heart Disease: {risiko}')
        st.write('Nutritional content:')
        a = dfk['Kkal'].sum()
        b = dfk['Lemak'].sum()
        c = dfk['Karbohidrat'].sum()
        d = dfk['Protein'].sum()
        st.write(f'Calories: {np.round(a)} Kkal')
        st.write(f'Fat: {np.round(b)} gr')
        st.write(f'Carbohydrate: {np.round(c)} gr')
        st.write(f'Protein: {np.round(d)} gr')
elif choice == "Fitness Exercise":
    st.title("Fitness Exercise")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("Select an exercise:")

        bicep_curl = st.checkbox('Bicep Curl')
        extensions = st.checkbox('Extensions')
        squats = st.checkbox('Squats')
        crunches = st.checkbox('Crunches')
        rows = st.checkbox('Rows')
        benchpress = st.checkbox('Benchpress')

        exercise_list = [bicep_curl, extensions, squats, crunches, rows, benchpress]
        exercises = ['Bicep Curl', 'Extensions', 'Squats','Crunches','Rows','Benchpress']
        exercise_to_do = {}

        for count, item in enumerate(exercise_list):
            if item:
                selected = True 
                user_input_rep = st.text_input("Please enter rep amount: " + exercises[count], key=count)
                user_input_sets = st.text_input("Please enter set amount: " + exercises[count],key=count)
                exercise_to_do[exercises[count]] = {"reps":user_input_rep,"sets":user_input_sets}

        options = st.button("Click me to begin.")
        if options:
            st.write(exercise_to_do)
            main.start(exercise_to_do)

    with col2:
        annotated_text(
            "Let's get started working out!",
        )
        lottie_diagram_url = 'https://assets7.lottiefiles.com/packages/lf20_k17htwqs.json'
        lottie_diagram = load_lottieurl(lottie_diagram_url)
        st_lottie(lottie_diagram, key='diagram')
