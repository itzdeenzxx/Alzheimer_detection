import cv2
import numpy as np
import mediapipe as mp
import time
from datetime import datetime, timedelta
from class_fitness.L_pose import Hand_L_Detector
from class_fitness.thumb_pink import thumb_pinky
from class_fitness.header import Header_finger

mp_hands = mp.solutions.hands

# set in fitness
set_of_Hand_L = 1
set_of_thumb_pinky = 1
set_of_Header = 1
#var break time 10sec
confirm_timer = False

timer_started = False
countdown_time = 20
remaining_time_continue = 20
start_stop_continue = True

class VideoCamera(object):
    def __init__(self):
        self.camera_index = 0 
        self.video = cv2.VideoCapture(self.camera_index)
        self.L_pose = Hand_L_Detector()
        self.thumb_pink = thumb_pinky()
        self.header_finger = Header_finger()
        self.check_count = True
        self.count_final_main = 0

    def __del__(self):
        self.video.release()
        
    def draw_text(self,image, text, position, font_scale=1, font_thickness=2):
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
        text_width, text_height = text_size
        text_x = position[0] - text_width // 2
        text_y = position[1] + text_height // 2
        cv2.putText(image, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)
        
    def get_frame(self):
        global set_of_Hand_L , set_of_thumb_pinky
        global confirm_timer , countdown_time , start_time , timer_started , remaining_time_continue , start_stop_continue
        
        remaining_time = remaining_time_continue
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
        if set_of_thumb_pinky > 3 and set_of_Header <= 3:
            self.header_finger.detect_and_head_finger_distance(frame)
            if self.header_finger.confirm_left and self.header_finger.confirm_right:
                confirm_timer = True
                start_stop = start_stop_continue
            else:
                confirm_timer = False
            print(confirm_timer)
            
            if confirm_timer:
                if not timer_started:
                    if start_stop :
                        start_time = cv2.getTickCount()
                        start_stop_continue = False
                    timer_started = True
                current_time = cv2.getTickCount()
                elapsed_time = (current_time - start_time) / cv2.getTickFrequency()
                remaining_time = max(0, countdown_time - elapsed_time)
                remaining_time_continue = remaining_time
            else:
                timer_started = False
                
            text = f"Time left: {int(remaining_time)} seconds"
            self.draw_text(frame, text, (frame.shape[1] // 2, 50))
                

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
    
