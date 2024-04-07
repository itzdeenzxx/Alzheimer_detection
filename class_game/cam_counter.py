import cv2
import numpy as np
import mediapipe as mp
import time
from class_game.gamereal import HandTracker

mp_hands = mp.solutions.hands


# var break time 10sec
countdown_time = 10


class VideoCamera_Game(object):
    def __init__(self):
        self.camera_index = 0
        self.video = cv2.VideoCapture(self.camera_index)
        self.game = HandTracker()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()

        if not ret:
            return None
        
        self.game.start_tracking(frame)
        self.game.show_number(frame)
        ret, jpeg = cv2.imencode(".jpg", frame)

        if not ret:
            return None
        return jpeg.tobytes()

    def gen(self):
        while True:
            
            frame = self.get_frame()

            yield (
                b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n"
            )
