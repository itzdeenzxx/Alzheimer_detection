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
            if idx == self.i and self.i > 0:
                text += "- "
            elif idx < self.i:
                text += f"{num} "
            else:
                text += "- "

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
        
        # คำนวณความกว้างและความสูงของภาพ
        # ขนาดของข้อความ
        text = f"ทำมือเลข {str(Number_random[0])} เพื่อเริ่มเกม"
        text_num = f"จงจำเลข :{str(Number_random[1])},{str(Number_random[2])},{str(Number_random[3])},{str(Number_random[4])}"
        text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_PLAIN, 3, 3)
        # คำนวณตำแหน่งที่จะวางข้อความให้อยู่ตรงกล
        if self.i <= 0:
            processed_frame = self.draw_text(frame, text, (250, 300))
            if processed_frame is not None:
                processed_frame = self.draw_text(processed_frame, text_num, (265, 250))
                return processed_frame
            else:
                return frame
        else:
            return frame

    def get_frame(self):
        ret, frame = self.video.read()

        if not ret:
            print("Error: Failed to retrieve frame")
            return None
        
        if frame is None:
            print("Error: Received None frame")
            return None

        self.i = self.game.start_tracking(frame, self.Number_random) 
        frame = self.show_number(frame, self.Number_random)
        frame = self.show_number_allrd(frame, self.Number_random)

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
