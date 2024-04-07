import cv2
import numpy as np
import mediapipe as mp
import time
from datetime import datetime, timedelta
from class_fitness.L_pose import Hand_L_Detector
from class_fitness.thumb_pink import thumb_pinky
from class_fitness.header import Header_finger
from class_fitness.ear_head import Head_Ear_Detector
mp_hands = mp.solutions.hands

# set in fitness
set_of_Hand_L = 1
set_of_thumb_pinky = 1
set_of_Header = 1
set_of_Ear = 1
# var time 30sec
confirm_timer = False
timer_started = False
countdown_time = 30 # countdown
remaining_time_continue = 30 # countdown output
start_time = 30
start_stop_continue = True
pause_requested = False  
timer_paused = False  
pause_time = 0 
resume_requested = False
elapsed_time = 0
start_stop = False

class VideoCamera(object):
    def __init__(self):
        self.camera_index = 0 
        self.video = cv2.VideoCapture(self.camera_index)
        self.L_pose = Hand_L_Detector()
        self.thumb_pink = thumb_pinky()
        self.header_finger = Header_finger()
        self.ear = Head_Ear_Detector()
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
        global set_of_Hand_L , set_of_thumb_pinky , set_of_Header
        global confirm_timer , countdown_time , start_time , timer_started , remaining_time_continue , start_stop_continue , pause_requested , timer_paused ,pause_time , resume_requested , elapsed_time , start_stop
        
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
                start_stop = start_stop_continue
                resume_requested = True
            else : 
                pause_requested = True
            
            if True:
                if not timer_started:
                    if start_stop:
                        start_time = cv2.getTickCount()
                        start_stop_continue = False
                    timer_started = True
                current_time = cv2.getTickCount()

                # Check if pausing is requested
                if pause_requested:
                    if not timer_paused:
                        pause_time = cv2.getTickCount()
                        timer_paused = True
                        print("Paused at:", pause_time)
                    pause_requested = False  # Reset pause request flag
                else:
                    if resume_requested:
                        if timer_paused:
                            resume_time = cv2.getTickCount()
                            pause_duration = (resume_time - pause_time) / cv2.getTickFrequency()
                            start_time += pause_duration  # Adjust start time to resume
                            timer_paused = False
                            print("Resumed at:", resume_time)
                        resume_requested = False  # Reset resume request flag

                elapsed_time = (current_time - start_time) / cv2.getTickFrequency()
                remaining_time = max(0, countdown_time - elapsed_time)
                remaining_time_continue = remaining_time
                            

            text = f"Time left: {int(remaining_time_continue)} seconds"
            self.draw_text(frame, text, (frame.shape[1] // 2, 50))
            if remaining_time_continue == 0 :
                set_of_Header += 1
                #reset countdown 30sec
                # pause overlay 
                
        
        if set_of_Header > 3 and set_of_Ear <= 3:
            self.count_final_main = self.ear.detect_and_head_finger_distance(frame,self.count_final_main)
            
        elif self.count_final_main >= 10 and set_of_Ear <= 3 and set_of_Header > 3:
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
    
