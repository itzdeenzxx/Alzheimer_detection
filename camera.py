import cv2
import numpy as np
import mediapipe as mp
import time
from class_fitness.L_pose import Hand_L_Detector,confirm_right,confirm_left,count_right,count_left,count_final
from class_fitness.thumb_pink import thumb_pinky

mp_hands = mp.solutions.hands

# set in fitness
set_of_Hand_L = 1
set_of_thumb_pinky = 1
#var break time 10sec
countdown_time = 10


class VideoCamera(object):
    def __init__(self):
        self.camera_index = 0 
        self.video = cv2.VideoCapture(self.camera_index)
        self.L_pose = Hand_L_Detector()
        self.thumb_pink = thumb_pinky()
        self.check_count = True
        self.count_final_main = 0

    def __del__(self):
        self.video.release()

    def get_frame(self):
        global set_of_Hand_L , set_of_thumb_pinky

        ret, frame = self.video.read()
        if not ret:
            return None
        
        if self.count_final_main < 10 and set_of_Hand_L <= 3:
            self.count_final_main = self.L_pose.detect_and_count_finger_distance(frame,self.count_final_main)

        elif self.count_final_main >= 10 and set_of_Hand_L <= 3:
            # self.show_overlay()
            set_of_Hand_L +=1
            self.count_final_main = 0

        if set_of_Hand_L > 3 and self.count_final_main < 10 and set_of_thumb_pinky <= 3:
            self.count_final_main = self.thumb_pink.detect_and_count_finger_distance(frame,self.count_final_main)

        elif self.count_final_main >= 10 and set_of_thumb_pinky <= 3 and set_of_Hand_L > 3:
            # self.show_overlay()
            set_of_thumb_pinky +=1
            self.count_final_main = 0

        ret, jpeg = cv2.imencode('.jpg', frame)

        if not ret:
            return None
        return jpeg.tobytes()
    
    def show_overlay(self):
        time.sleep(2)
            

    def gen(self):
        while True:
            frame = self.get_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
