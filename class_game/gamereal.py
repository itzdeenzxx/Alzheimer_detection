import cv2
import mediapipe as mp
import time
from class_game.cam_counter import *

class HandTracker:
    global i
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands()
        self.pTime = 0
        self.i= 0
        
        
    def start_tracking(self,frame,Number_random):

        results = self.hands.process(frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    fingers_1 = 0
                    fingers_2 = 0
                    fingers_3 = 0
                    fingers_4 = 0
                    fingers_5 = 0
                    if id == 0:
                        continue

                    if (
                        hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y
                        and hand_landmarks.landmark[8].x > hand_landmarks.landmark[17].x
                        or hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y
                        and hand_landmarks.landmark[0].x > hand_landmarks.landmark[8].x
                    ):
                        fingers_1 += 1

                    if (
                        hand_landmarks.landmark[12].y < hand_landmarks.landmark[11].y
                        and hand_landmarks.landmark[12].x
                        > hand_landmarks.landmark[17].x
                        or hand_landmarks.landmark[12].y < hand_landmarks.landmark[11].y
                        and hand_landmarks.landmark[0].x > hand_landmarks.landmark[12].x
                    ):
                        fingers_2 += 1

                    if (
                        hand_landmarks.landmark[16].y < hand_landmarks.landmark[15].y
                        and hand_landmarks.landmark[16].x
                        > hand_landmarks.landmark[17].x
                        or hand_landmarks.landmark[16].y < hand_landmarks.landmark[15].y
                        and hand_landmarks.landmark[0].x > hand_landmarks.landmark[16].x
                    ):
                        fingers_3 += 1

                    if (
                        hand_landmarks.landmark[20].y < hand_landmarks.landmark[19].y
                        and hand_landmarks.landmark[20].x
                        > hand_landmarks.landmark[17].x
                        or hand_landmarks.landmark[20].y < hand_landmarks.landmark[19].y
                        and hand_landmarks.landmark[0].x > hand_landmarks.landmark[20].x
                    ):
                        fingers_4 += 1

                    if hand_landmarks.landmark[4].x > hand_landmarks.landmark[2].x:
                        fingers_5 += 1
                    if self.i < 5 :
                        if Number_random[self.i] == 0:
                            if(
                                fingers_1 == 0
                                and fingers_2 == 0
                                and fingers_3 == 0
                                and fingers_4 == 0
                                and fingers_5 == 0
                            ):
                                cv2.putText(
                                    frame,
                                    f"START!!!",
                                    (250, 250),  
                                    cv2.FONT_HERSHEY_PLAIN,
                                    3,
                                    (255, 0, 0),
                                    3,
                                )
                                self.i += 1
                        if Number_random[self.i] == 1:
                            if(
                                fingers_1 == 1
                                and fingers_2 == 0
                                and fingers_3 == 0
                                and fingers_4 == 0
                                and fingers_5 == 0
                            ):
                                cv2.putText(
                                    frame,
                                    f"correct!",
                                    (250, 250),  
                                    cv2.FONT_HERSHEY_PLAIN,
                                    3,
                                    (255, 0, 0),
                                    3,
                                )
                                self.i += 1
                        elif Number_random[self.i] == 2:
                            if (
                                fingers_1 == 1
                                and fingers_2 == 1
                                and fingers_3 == 0
                                and fingers_4 == 0
                                and fingers_5 == 0
                            ):
                                cv2.putText(
                                    frame,
                                    f"correct!",
                                    (250, 250),  
                                    cv2.FONT_HERSHEY_PLAIN,
                                    3,
                                    (255, 0, 0),
                                    3,
                                )
                                self.i += 1
                        elif Number_random[self.i] == 3:
                            if (
                                fingers_1 == 1
                                and fingers_2 == 1
                                and fingers_3 == 1
                                and fingers_4 == 0
                                and fingers_5 == 0
                            ):
                                cv2.putText(
                                    frame,
                                    f"correct!",
                                    (250, 250),  
                                    cv2.FONT_HERSHEY_PLAIN,
                                    3,
                                    (255, 0, 0),
                                    3,
                                )
                                self.i += 1
                        elif Number_random[self.i] == 4:
                            if (
                                fingers_1 == 1
                                and fingers_2 == 1
                                and fingers_3 == 1
                                and fingers_4 == 1
                                and fingers_5 == 0
                            ):
                                cv2.putText(
                                    frame,
                                    f"correct!",
                                    (250, 250),  
                                    cv2.FONT_HERSHEY_PLAIN,
                                    3,
                                    (255, 0, 0),
                                    3,
                                )
                                self.i += 1
                        elif Number_random[self.i] == 5:
                            if (
                                fingers_1 == 1
                                and fingers_2 == 1
                                and fingers_3 == 1
                                and fingers_4 == 1
                                and fingers_5 == 1
                            ):
                                cv2.putText(
                                    frame,
                                    f"correct!",
                                    (250, 250),  
                                    cv2.FONT_HERSHEY_PLAIN,
                                    3,
                                    (255, 0, 0),
                                    3,
                                )
                                self.i += 1

    def show_number(self, frame, Number_random):
        text = ""
        for idx, num in enumerate(Number_random):
            if idx == self.i and self.i > 0:
                text += "- "
            elif idx < self.i:
                text += f"{num} "
            else:
                text += "- "

        if self.i < len(Number_random):
            cv2.putText(
                frame,
                text.strip() ,  
                (50, 50),  
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (255, 0, 0),
                2
            )
        


    def show_number_allrd(self, frame, Number_random):
        # คำนวณความกว้างและความสูงของภาพ
        height, width, _ = frame.shape
        
        # ขนาดของข้อความ
        text = f"handful to start {str(Number_random[0])} "
        text1 = f"Number:{str(Number_random[1])},{str(Number_random[2])},{str(Number_random[3])},{str(Number_random[4])}"
        text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_PLAIN, 3, 3)
        
        
        # คำนวณตำแหน่งที่จะวางข้อความให้อยู่ตรงกลาง
        text_x = int((width - text_size[0]) / 2)
        text_y = int((height + text_size[1]) / 2)
        
        if self.i <= 0 :
            cv2.putText(
                frame,
                text,
                
                (250, 300),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (255, 0, 0),
                2,
            )
            cv2.putText(
                frame,
                text1,
                
                (265, 250),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (255, 0, 0),
                2,
            )
        



    def stop_tracking(self):
        self.cap.release()
        cv2.destroyAllWindows()


# Instantiate the HandTracker class and start tracking
