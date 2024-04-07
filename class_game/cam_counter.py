import cv2
import numpy as np
import mediapipe as mp
import time

mp_hands = mp.solutions.hands


#var break time 10sec
countdown_time = 10


class VideoCamera_Game(object):
    def __init__(self):
        self.camera_index = 0 
        self.video = cv2.VideoCapture(self.camera_index)
        self.check_count = True
        self.count_final_main = 0

    def __del__(self):
        self.video.release()

    def get_frame(self):
        
        ret, frame = self.video.read()

        if not ret:
            return None
        
        if self.count_final_main < 10 :
            pass
        elif self.count_final_main >= 10 :
            pass

        ret, jpeg = cv2.imencode('.jpg', frame)

        if not ret:
            return None
        return jpeg.tobytes()
    
    
            

    def gen(self):
        while True:
            frame = self.get_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
