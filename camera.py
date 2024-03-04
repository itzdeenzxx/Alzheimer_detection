import cv2
import numpy as np
import mediapipe as mp
from class_fitness.L_pose import Hand_L_Detector,confirm_right,confirm_left,count_right,count_left,count_final

mp_hands = mp.solutions.hands

set_of_Hand_L = 0

#var break time 10sec
countdown_time = 10
overlay_break = cv2.imread('class_fitness/img/background_trans.png', cv2.IMREAD_UNCHANGED)

class VideoCamera(object):
    def __init__(self):
        self.camera_index = 0 
        self.video = cv2.VideoCapture(self.camera_index)
        self.L_pose = Hand_L_Detector() 
        self.check_count = True
        self.count_final_main = 0

    def __del__(self):
        self.video.release()

    def get_frame(self):
        global overlay_break , set_of_Hand_L , overlay_break
        ret, frame = self.video.read()
        if not ret:
            return None
        if self.count_final_main < 10 :
            self.count_final_main = self.L_pose.detect_and_count_finger_distance(frame)
            print(self.count_final_main)

        elif self.count_final_main >= 10 :
            overlay_break_resized = cv2.resize(overlay_break, (frame.shape[1], frame.shape[0]))
            cv2.imshow('Camera with Overlay', overlay_break_resized)
            print("11111111111111111111111111111111111111111111111111111")

        ret, jpeg = cv2.imencode('.jpg', frame)

        if not ret:
            return None
        return jpeg.tobytes()
    
    def show_overlay():
        pass

    def gen(self):
        while True:
            frame = self.get_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
