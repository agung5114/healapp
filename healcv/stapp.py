import streamlit as st
import pandas as pd
import numpy as np
# import plotly_express as px
from PIL import Image
import streamlit.components.v1 as components
# import matplotlib.pyplot as plt
import tensorflow
from tensorflow import keras
import joblib
import operator
import sys

import mediapipe as mp
import main
import requests
from streamlit_lottie import st_lottie
from annotated_text import annotated_text
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal  # type: ignore

import cv2
from aiortc.contrib.media import MediaPlayer
from streamlit_webrtc import (
    AudioProcessorBase,
    RTCConfiguration,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer
)
# from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, ClientSettings
import av

st.set_page_config(
    page_title='healcv',
    layout='wide'
    )

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
# website_icon = Image.open('MyGymBuddy.jpg')
# args = get_args()  

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.applications.mobilenet import decode_predictions

from PIL import Image
sys.modules['Image'] = Image 
# [theme]
base="light"
primaryColor="teal"
st.title("Fitness Exercise")
col1, col2, col3= st.columns([1,2,2])

with col1:
    annotated_text(
        "Let's get started working out!",
    )
    lottie_diagram_url = 'https://assets7.lottiefiles.com/packages/lf20_k17htwqs.json'
    lottie_diagram = load_lottieurl(lottie_diagram_url)
    st_lottie(lottie_diagram, key='diagram')

with col2:
    import time
    st.write("Select an exercise:")
    exercises = ['Bicep Curl', 'Extensions', 'Squats','Crunches','Rows','Benchpress']
    selected = st.selectbox("Select Exercise", exercises)
    user_input_rep = st.number_input("Please enter rep amount: ",min_value=0, max_value=10, value=1, step=1)
    user_input_sets = st.number_input("Please enter set amount: ",min_value=0, max_value=10, value=1, step=1)
    exercise_to_do = {f'{selected}':{"sets":user_input_sets,"reps":user_input_rep}}
    # def start(sets, reps):
    #     cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        
with col3:
    sets = user_input_sets
    reps = user_input_rep
    def calculate_angle(a,b,c):
        a = np.array(a) # First
        b = np.array(b) # Mid
        c = np.array(c) # End
        
        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)
        
        if angle > 180.0:
            angle = 360-angle
            
        return angle
    class VideoProcessor(VideoProcessorBase):
        type: Literal["noop", "cartoon", "edges", "rotate"]
        def __init__(self) -> None:
            self.type = "noop"

        def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
            cap = frame.to_ndarray(format="bgr24")
            cap = cap[:,::-1,:]
            # cap = cv2.VideoCapture(cap)
            sets_counter = 0

            while sets_counter < sets:
                # Crunches reps_counter variables
                reps_counter = 0 
                stage = None

                # Setup mediapipe instance
                with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                    # cap.isOpened()
                    while reps_counter < reps:
                        # ret, frame = cap.read()
                        
                        # Recolor image to RGB
                        image = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)
                        # image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        image.flags.writeable = False
                    
                        # Make detection
                        results = pose.process(image)
                    
                        # Recolor back to BGR
                        image.flags.writeable = True
                        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                        
                        # Extract landmarks
                        try:
                            landmarks = results.pose_landmarks.landmark
                            
                            # Get coordinates
                            knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                            hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                            
                            # Setup status box
                            image_add = cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
                            
                            # Rep data
                            image_add = cv2.putText(image, 'REPS', (15,12), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                            image_add = cv2.putText(image, str(reps_counter), 
                                        (10,60), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
                            
                            # Stage data
                            image_add = cv2.putText(image, 'STAGE', (65,12), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                            image_add = cv2.putText(image, stage, 
                                        (60,60), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
                            
                            
                            # Render detections
                            mp_drawing.draw_landmarks(image_add, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                                    )    
                            # Calculate angle
                            angle = calculate_angle(knee, hip, shoulder)
                            
                            # Visualize angle
                            image_add = cv2.putText(image_add, str(angle), 
                                        tuple(np.multiply(hip, [640, 480]).astype(int)), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                                )
                            
                            # Crunches Increment Logic
                            if angle > 100:
                                stage = "up"
                            if angle < 50 and stage =='up':
                                stage="down"
                                reps_counter +=1
                        
                            # image = cv2.imshow('Mediapipe Feed', image)
                            show_image = av.VideoFrame.from_ndarray(cv2.bitwise_and(image, image_add), format="bgr24")

                            if cv2.waitKey(10) & 0xFF == ord('q'):
                                break

                        except:
                            pass    
                    sets_counter += 1
                    if (sets_counter!=sets):
                        try:
                            image = cv2.putText(image, 'FINISHED SET', (100,250), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 3, cv2.LINE_AA)
                            # image = cv2.imshow('Mediapipe Feed', image)
                            show_image = av.VideoFrame.from_ndarray(image, format="bgr24")
                            cv2.waitKey(1)
                            time.sleep(60)   

                        except:
                            # image = cv2.imshow('Mediapipe Feed', image)
                            # pass
                            show_image = av.VideoFrame.from_ndarray(image, format="bgr24")
            # image = cv2.bitwise_and(img_color, img_edges)                     
            image_add = cv2.rectangle(image, (50,180), (600,400), (0,255,0), -1)
            image_add = cv2.putText(image, 'FINISHED EXERCISE', (100,250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 3, cv2.LINE_AA)
            image_add = cv2.putText(image, 'REST FOR 60s' , (155,350), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 3, cv2.LINE_AA)   
            # image = cv2.imshow('Mediapipe Feed', img)
            show_image = av.VideoFrame.from_ndarray(cv2.bitwise_and(image, image_add), format="bgr24")
            # image.waitKey(1) 
            time.sleep(10)                      
            # image.release()
            # image.destroyAllWindows()
            return show_image
    
    RTC_CONFIGURATION = RTCConfiguration(
        {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    )
    cam = webrtc_streamer(
        key="opencv-filter",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        video_processor_factory=VideoProcessor,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True)

    
