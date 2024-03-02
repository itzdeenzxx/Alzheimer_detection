import cv2
import numpy as np
import mediapipe as mp
from class_fitness.L_pose import Hand_L_Detector,confirm_right,confirm_left,count_right,count_left
from class_fitness.L_pose_2 import Hand_L_Detector_2,confirm_right_2,confirm_left_2,count_right_2,count_left_2

mp_hands = mp.solutions.hands

cont_of_L_pose = 0

class VideoCamera(object):
    def __init__(self):
        self.camera_index = 0 
        self.video = cv2.VideoCapture(self.camera_index)

        self.L_pose = Hand_L_Detector() #######
        self.L_pose_2 = Hand_L_Detector_2() #######
        self.swap_hand = 0

    def __del__(self):
        self.video.release()

    def get_frame(self):
        global cont_of_L_pose
        ret, frame = self.video.read()
        if not ret:
            return None
        cv2.putText(frame, str(cont_of_L_pose), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        if self.swap_hand >= 10 :
            pass
        elif self.swap_hand % 2 == 0:
            self.L_pose.detect_and_count_finger_distance(frame)
            if(confirm_left == 1 and confirm_right == 1):
                print("1231231212121")
                # self.count_hand_L()
                cont_of_L_pose += 1
                self.swap_hand += 1
                self.L_pose.set_zero()

        elif self.swap_hand % 2 == 1:
            self.L_pose_2.detect_and_count_finger_distance_2(frame)
            self.L_pose_2.set_zero()
            self.count_hand_L()
            self.swap_hand += 1

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
    
