import cv2
import numpy as np
import mediapipe as mp
import time
from PIL import ImageFont, ImageDraw, Image 
from datetime import datetime, timedelta
from class_fitness.L_pose import Hand_L_Detector
from class_fitness.thumb_pink import thumb_pinky
from class_fitness.header import Header_finger
from class_fitness.ear_head import Head_Ear_Detector
from class_fitness.collarbone import Colarbone_finger
from class_fitness.finished import Finish
mp_hands = mp.solutions.hands
# set in fitness
set_of_Hand_L = 0
set_of_thumb_pinky = 0
set_of_Header = 0
set_of_Ear = 0
set_of_collar = 0
#var tutorail
select_player = True
pass_check = 0
video_path = "static/video/video-test3.mp4"
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

#finish
check_finish = False

class VideoCamera(object):
    def __init__(self):
        self.camera_index = 0 
        self.video = cv2.VideoCapture(self.camera_index)
        self.L_pose = Hand_L_Detector()
        self.thumb_pink = thumb_pinky()
        self.header_finger = Header_finger()
        self.ear = Head_Ear_Detector()
        self.collar = Colarbone_finger()
        self.finish = Finish()
        self.check_count = True
        self.count_final_main = 0
        self.set_main = 1

    def __del__(self):
        self.video.release()
    
    def draw_text(self,image, text , position):
        pil_im = Image.fromarray(image) 
        draw = ImageDraw.Draw(pil_im)
        font = ImageFont.truetype("static/font/Prompt-Regular.ttf", 50)  
        draw.text(position, text, font=font)  
        cv2_im_processed = np.array(pil_im)
        return cv2_im_processed
    
    def get_frame(self):
        global set_of_Hand_L , set_of_thumb_pinky , set_of_Header , set_of_collar , set_of_Ear
        global remaining_time_continue
        global set_main , pass_check
        global check_finish

        remaining_time = remaining_time_continue
        ret, frame = self.video.read()
        
        if self.count_final_main < 10 and set_of_Hand_L < 3 and self.set_main == 1 :
            self.count_final_main = self.L_pose.detect_and_count_finger_distance(frame,self.count_final_main)
            text_Lpose = f"สำเร็จ : {str(self.count_final_main)}"
            text_Lpose_round = f"รอบ : {str(set_of_Hand_L + 1)}"
            position_Lpose = (50,50)
            position_Lpose_round = (53,150)
            frame = self.draw_text(frame, text_Lpose , position_Lpose)
            frame = self.draw_text(frame, text_Lpose_round , position_Lpose_round)

        elif self.count_final_main >= 10 and set_of_Hand_L <= 3:
            # self.show_overlay()
            set_of_Hand_L +=1
            print(set_of_Hand_L)
            self.count_final_main = 0
            
        elif set_of_Hand_L == 3 and self.set_main == 1:
            check_finish = self.finish.check_finish(frame , check_finish)
            if check_finish :
                set_of_Hand_L = 0
                self.count_final_main = 0
                text_finish = f"เริ่มออกกำลังกายอีกครั้ง"
                frame = self.draw_text(frame, text_finish, (400, 500))
            else :
                text_finish = f"จบการออกกำลังกาย"
                text_finish_con = f"หากต้องการออกกำลังกายอีกครั้ง"
                text_finish_emote = f"ให้ทำมือสัญลักษณ์ เลิฟยู"
                frame = self.draw_text(frame, text_finish, (200, 200))
                frame = self.draw_text(frame, text_finish_con, (400, 400))
                frame = self.draw_text(frame, text_finish_emote, (400, 500))
         
        if self.count_final_main < 10 and set_of_thumb_pinky < 3 and self.set_main == 2:
            self.count_final_main = self.thumb_pink.detect_and_count_finger_distance(frame,self.count_final_main)
            text_thumb = f"สำเร็จ : {str(self.count_final_main)}"
            text_thumb_round = f"รอบ : {str(set_of_thumb_pinky + 1)}"
            position_thumb = (50,50)
            position_thumb_round = (53,150)
            frame = self.draw_text(frame, text_thumb , position_thumb)
            frame = self.draw_text(frame, text_thumb_round , position_thumb_round)
            
        elif self.count_final_main >= 10 and set_of_thumb_pinky <= 3:
            check_finish = False
            set_of_thumb_pinky +=1
            self.count_final_main = 0
        elif set_of_thumb_pinky == 3 and self.set_main == 2:
            check_finish = self.finish.check_finish(frame , check_finish)
            if check_finish :
                set_of_thumb_pinky = 0
                self.count_final_main = 0
                text_finish = f"เริ่มออกกำลังกายอีกครั้ง"
                frame = self.draw_text(frame, text_finish, (400, 500))
            else :
                text_finish = f"จบการออกกำลังกาย"
                text_finish_con = f"หากต้องการออกกำลังกายอีกครั้ง"
                text_finish_emote = f"ให้ทำมือสัญลักษณ์ เลิฟยู"
                frame = self.draw_text(frame, text_finish, (200, 200))
                frame = self.draw_text(frame, text_finish_con, (400, 400))
                frame = self.draw_text(frame, text_finish_emote, (400, 500))
                
        if self.set_main == 3 and set_of_Header == 0:
            check_finish = False
            remaining_time_continue = self.header_finger.detect_and_head_finger_distance(frame)
            text_header = f"เวลาที่เหลือ : {int(30 - remaining_time_continue)} วินาที"
            position_header = (50,50)
            frame = self.draw_text(frame, text_header,position_header)
            if remaining_time_continue == 30 :
                set_of_Header += 1
                remaining_time_continue = 0
                
        # elif set_of_Header != 0 and self.set_main == 3:
        #     check_finish = self.finish.check_finish(frame , check_finish)
        #     if check_finish :
        #         set_of_Header = 0
        #         self.count_final_main = 0
        #         text_finish = f"เริ่มออกกำลังกายอีกครั้ง"
        #         frame = self.draw_text(frame, text_finish, (400, 500))
        #     else :
        #         text_finish = f"จบการออกกำลังกาย"
        #         text_finish_con = f"หากต้องการออกกำลังกายอีกครั้ง"
        #         text_finish_emote = f"ให้ทำมือสัญลักษณ์ เลิฟยู"
        #         frame = self.draw_text(frame, text_finish, (200, 200))
        #         frame = self.draw_text(frame, text_finish_con, (400, 400))
        #         frame = self.draw_text(frame, text_finish_emote, (400, 500))
                
        if self.set_main == 4 and set_of_Ear < 3:
            check_finish = False
            self.count_final_main = self.ear.detect_and_head_finger_distance(frame,self.count_final_main)
            text_Ear = f"สำเร็จ : {str(self.count_final_main)}"
            text_Ear_round = f"รอบ : {str(set_of_thumb_pinky + 1)}"
            position_Ear = (50,50)
            position_Ear_round = (53,150)
            frame = self.draw_text(frame, text_Ear , position_Ear)
            frame = self.draw_text(frame, text_Ear_round , position_Ear_round)
            
        elif self.count_final_main >= 10 and set_of_Ear <= 3 :
            # self.show_overlay()
            set_of_thumb_pinky +=1
            self.count_final_main = 0
            
        elif set_of_Ear == 3 and self.set_main == 4:
            check_finish = self.finish.check_finish(frame , check_finish)
            if check_finish :
                set_of_Ear = 0
                self.count_final_main = 0
                text_finish = f"เริ่มออกกำลังกายอีกครั้ง"
                frame = self.draw_text(frame, text_finish, (400, 500))
            else :
                text_finish = f"จบการออกกำลังกาย"
                text_finish_con = f"หากต้องการออกกำลังกายอีกครั้ง"
                text_finish_emote = f"ให้ทำมือสัญลักษณ์ เลิฟยู"
                frame = self.draw_text(frame, text_finish, (200, 200))
                frame = self.draw_text(frame, text_finish_con, (400, 400))
                frame = self.draw_text(frame, text_finish_emote, (400, 500))
                
        if self.set_main == 5 and set_of_collar == 0:
            check_finish = False
            remaining_time_continue = self.collar.detect_and_coloarbone_finger_distance(frame)
            text_collar = f"เวลาที่เหลือ : {int(30 - remaining_time_continue)} วินาที"
            position_collar = (50,50)
            frame = self.draw_text(frame, text_collar,position_collar)
            if remaining_time_continue == 30 :
                set_of_collar += 1
                remaining_time_continue = 0
            pass
        # elif set_of_collar != 0 and self.set_main == 3:
        #     check_finish = self.finish.check_finish(frame , check_finish)
        #     if check_finish :
        #         set_of_collar = 0
        #         self.count_final_main = 0
        #         text_finish = f"เริ่มออกกำลังกายอีกครั้ง"
        #         frame = self.draw_text(frame, text_finish, (400, 500))
        #     else :
        #         text_finish = f"จบการออกกำลังกาย"
        #         text_finish_con = f"หากต้องการออกกำลังกายอีกครั้ง"
        #         text_finish_emote = f"ให้ทำมือสัญลักษณ์ เลิฟยู"
        #         frame = self.draw_text(frame, text_finish, (200, 200))
        #         frame = self.draw_text(frame, text_finish_con, (400, 400))
        #         frame = self.draw_text(frame, text_finish_emote, (400, 500))
        ret, jpeg = cv2.imencode('.jpg', frame)

        if not ret:
            return None
        
        return jpeg.tobytes()
    
    def set_of_main(self,check):
        self.set_main = check
        self.count_final_main = 0
            
    def gen(self):
        while True:
            frame = self.get_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
