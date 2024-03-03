import cv2
import numpy as np
import mediapipe as mp
from class_fitness.L_pose import Hand_L_Detector,confirm_right,confirm_left,count_right,count_left

mp_hands = mp.solutions.hands

cont_of_L_pose = 0

class VideoCamera(object):
    def __init__(self):
        self.camera_index = 0 
        self.video = cv2.VideoCapture(self.camera_index)
        self.L_pose = Hand_L_Detector() #######

    def __del__(self):
        self.video.release()

    def get_frame(self):
        global cont_of_L_pose
        ret, frame = self.video.read()
        if not ret:
            return None
        
        self.L_pose.detect_and_count_finger_distance(frame)
       
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            return None
        return jpeg.tobytes()

    def count_hand_L(self):
        global cont_of_L_pose
        cont_of_L_pose += 1

    def gen(self):
        while True:
            frame = self.get_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
