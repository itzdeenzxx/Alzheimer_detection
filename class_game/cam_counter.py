import cv2
import numpy as np
import mediapipe as mp
import time
from PIL import ImageFont, ImageDraw, Image 
from class_game.gamereal import HandTracker
import random as rd

mp_hands = mp.solutions.hands


# var break time 10sec
countdown_time = 10


class VideoCamera_Game(object):
    global Number_random
    def __init__(self):
        self.camera_index = 0
        self.video = cv2.VideoCapture(self.camera_index)
        self.game = HandTracker()
        self.Number_random = [0] + [rd.randint(1, 5) for _ in range(4)]
        self.i = 0
        self.score = 0
        self.confirm_game = True

    def __del__(self):
        self.video.release()

    def draw_text(self, image, text, position):
        if image is None:
            return None
        
        pil_im = Image.fromarray(image) 
        draw = ImageDraw.Draw(pil_im)
        font = ImageFont.truetype("class_game/Prompt-Regular.ttf", 50)  
        draw.text(position, text, font=font)  
        cv2_im_processed = np.array(pil_im)
        return cv2_im_processed

    def show_number(self, frame, Number_random):
        if frame is None:
            return None
        
        text = ""
        for idx, num in enumerate(Number_random):
            
            if idx == self.i and self.i > 1:
                text += "- "
            elif idx < self.i and num !=0:
                text += f"{num} "
            

        if self.i < len(Number_random):
            processed_frame = self.draw_text(frame, text.strip(), (50, 50))
            if processed_frame is not None:
                return processed_frame
            else:
                return frame
        else:
            return frame

    def show_number_allrd(self, frame, Number_random):
        if frame is None:
            return None
        
        text_tell = f"โปรดชูมือให้ถูกต้องตามตัวเลขปรากฏก่อนหน้า"
        
        text = f'ทำมือ "เลิฟยู" จึงเริ่มเกม'
        text_num = f"จงจำเลข : {str(Number_random[1])},{str(Number_random[2])},{str(Number_random[3])},{str(Number_random[4])}"
        text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_PLAIN, 3, 3)
        if self.i <= 0:
            processed_frame = self.draw_text(frame, text, (400, 500))
            if processed_frame is not None:
                processed_frame = self.draw_text(processed_frame, text_num, (480, 250))
                return processed_frame
            else:
                return frame
        else:
            frame = self.draw_text(frame , text_tell , (200,600))
            return frame
    def set_random(self , number) :
        self.Number_random = number

    def get_frame(self):
      
        ret, frame = self.video.read()

        if not ret:
            print("Error: Failed to retrieve frame")
            return None
        
        if frame is None:
            print("Error: Received None frame")
            return None
        if self.confirm_game :
            self.i , times = self.game.start_tracking(frame, self.Number_random) 
            if self.i == 999 :
                self.score += 1
                self.Number_random = [0] + [rd.randint(1, 5) for _ in range(4)]
                self.i = 0
            text_score = f"จำนวนแต้ม : {str(self.score)}"
            frame = self.show_number(frame, self.Number_random)
            frame = self.show_number_allrd(frame, self.Number_random)
            frame = self.draw_text(frame , text_score , (500,30))
            if times == 60 :
                self.confirm_game = False
            frame = self.draw_text(frame , str(60-times) , (1080,50))
        else :
            pass 
            # ทำฟังชันก์ใน gamereal ให้สามารถ restart และ บอกคะแนนทั้งหมดที่ได้ ได้ โดย ถ้าเงื่อนไขที่ return ออกมา เป็น true ให้ restart ได้ 
        
        

        ret, jpeg = cv2.imencode(".jpg", frame)

        if not ret:
            print("Error: Failed to encode frame as JPEG")
            return None
        

        return jpeg.tobytes()


    def gen(self):
        while True:
            
            frame = self.get_frame()

            yield (
                b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n"
            )
            if self.i == len(self.Number_random):
                self.Number_random = [0] + [rd.randint(1, 5) for _ in range(4)]
                self.i = 0
