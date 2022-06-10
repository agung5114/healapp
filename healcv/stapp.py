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

# import mediapipe as mp
import main
import requests
from streamlit_lottie import st_lottie
from annotated_text import annotated_text
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal  # type: ignore

# import cv2
# from aiortc.contrib.media import MediaPlayer
# from streamlit_webrtc import (
#     AudioProcessorBase,
#     RTCConfiguration,
#     VideoProcessorBase,
#     WebRtcMode,
#     webrtc_streamer
# )
# # from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, ClientSettings
# import av
# from args import get_args

st.set_page_config(
    page_title='healcv',
    layout='wide'
    )

# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose
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
col2, col3= st.columns([2,2])

# with col1:
#     annotated_text(
#         "Let's get started working out!",
#     )
    # lottie_diagram_url = 'https://assets7.lottiefiles.com/packages/lf20_k17htwqs.json'
    # lottie_diagram = load_lottieurl(lottie_diagram_url)
    # st_lottie(lottie_diagram, key='diagram')

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
    annotated_text(
        "Let's get started!",
    )
    st.camera_input('Open Camera')
#     sets = user_input_sets
#     reps = user_input_rep
#     def calculate_angle(a,b,c):
#         a = np.array(a) # First
#         b = np.array(b) # Mid
#         c = np.array(c) # End
        
#         radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
#         angle = np.abs(radians*180.0/np.pi)
        
#         if angle > 180.0:
#             angle = 360-angle
            
#         return angle
#     class VideoProcessor(VideoProcessorBase):
#     # class VideoProcessor():
#         type: Literal["noop", "cartoon", "edges", "rotate"]
#         def __init__(self) -> None:
#             self.type = "noop"
#         def recv(self, frm):
#             self.type = "noop"
#             frame = frm.to_ndarray(format="bgr24")
#             # vid = av.VideoFrame.from_ndarray(frame,format='bgr24')
#             # cap = cv2.VideoCapture(frame,cv2.CAP_DSHOW)
#             sets_counter = 0

#             while sets_counter < sets:
#                 # Bench Press reps_counter variables
#                 stage = None
#                 reps_counter = 0

#                 # Setup mediapipe instance
#                 with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
#                     # cap.isOpened()
#                     while reps_counter < reps:
#                         # ret, frame = cap.read()
                        
#                         # Recolor image to RGB
#                         # cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#                         # image = cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),1.1,3)
#                         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                         image.flags.writeable = False
                    
#                         # Make detection
#                         results = pose.process(image)
                    
#                         # Recolor back to BGR
#                         image.flags.writeable = True
#                         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                        
#                         # Extract landmarks
#                         try:
#                             landmarks = results.pose_landmarks.landmark
                            
#                             # Get coordinates
#                             shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
#                                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
#                             elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
#                                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
#                             wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
#                                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                            
#                             # Setup status box
#                             cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
                            
#                             # Rep data
#                             cv2.putText(image, 'REPS', (15,12), 
#                                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
#                             cv2.putText(image, str(reps_counter), 
#                                         (10,60), 
#                                         cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
                            
#                             # Stage data
#                             cv2.putText(image, 'STAGE', (65,12), 
#                                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
#                             cv2.putText(image, stage, 
#                                         (60,60), 
#                                         cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
                            
#                             # Render detections
#                             mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
#                                                     mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
#                                                     mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
#                                                     )   

#                             # Calculate angle
#                             angle = calculate_angle(shoulder, elbow, wrist)
                            
#                             # Visualize angle
#                             cv2.putText(image, str(angle), 
#                                         tuple(np.multiply(elbow, [640, 480]).astype(int)), 
#                                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
#                                                 )
                            
#                             # Press reps_counter logic
#                             if angle < 60:
#                                 stage = "up"
#                             elif angle > 160 and stage == "up":
#                                 stage = "down"
#                                 reps_counter +=1
#                         except:
#                             pass
#                     sets_counter += 1
#                     if (sets_counter!=sets):
#                         try:
#                             cv2.putText(image, 'FINISHED SET', (100,250), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 3, cv2.LINE_AA)
#                             cv2.imshow('Mediapipe Feed', image)
#                             cv2.waitKey(1)
#                             time.sleep(60)   

#                         except:
#                             cv2.imshow('Mediapipe Feed', image)
#                             pass 
                                    
#             cv2.rectangle(image, (50,180), (600,400), (0,255,0), -1)
#             cv2.putText(image, 'FINISHED EXERCISE', (100,250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 3, cv2.LINE_AA)
#             cv2.putText(image, 'REST FOR 60s' , (155,350), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 3, cv2.LINE_AA)   
#             cv2.imshow('Mediapipe Feed', image)
#             cv2.waitKey(1)
#             time.sleep(60)                      
#             frame.release()
#             cv2.destroyAllWindows() 
#             # return av.VideoFrame.from_ndarray(frame,format='bgr24')
            
    
#     RTC_CONFIGURATION = RTCConfiguration(
#         {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
#     )

#     cam = webrtc_streamer(
#         key="opencv-filter",
#         mode=WebRtcMode.SENDRECV,
#         rtc_configuration=RTC_CONFIGURATION,
#         video_processor_factory=VideoProcessor,
#         media_stream_constraints={"video": True, "audio": False},
#         async_processing=True)

    
