import cv2
import mediapipe as mp
import time
from class_game.cam_counter import *
import random as rd

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
                hand_landmarks = results.multi_hand_landmarks[0]
                for id, lm in enumerate(hand_landmarks.landmark):
                    fingers = 0
                    if id == 0:
                        continue

                    if (
                        hand_landmarks.landmark[8].y < hand_landmarks.landmark[5].y
                        and hand_landmarks.landmark[4].y > hand_landmarks.landmark[5].y
                        and hand_landmarks.landmark[12].y > hand_landmarks.landmark[7].y
                        and hand_landmarks.landmark[16].y > hand_landmarks.landmark[7].y
                        and hand_landmarks.landmark[20].y > hand_landmarks.landmark[7].y
                    ):
                        fingers = 1
                    if (
                        hand_landmarks.landmark[8].y < hand_landmarks.landmark[5].y
                        and hand_landmarks.landmark[12].y < hand_landmarks.landmark[9].y
                        and hand_landmarks.landmark[4].y > hand_landmarks.landmark[5].y
                        and hand_landmarks.landmark[16].y > hand_landmarks.landmark[7].y
                        and hand_landmarks.landmark[20].y > hand_landmarks.landmark[7].y
                        
                    ):
                        fingers = 2

                    if (
                        hand_landmarks.landmark[8].y < hand_landmarks.landmark[5].y
                        and hand_landmarks.landmark[12].y < hand_landmarks.landmark[9].y
                        and hand_landmarks.landmark[16].y < hand_landmarks.landmark[13].y
                        and hand_landmarks.landmark[4].y > hand_landmarks.landmark[5].y
                        and hand_landmarks.landmark[20].y > hand_landmarks.landmark[17].y
                    ):
                        fingers = 3

                    if (hand_landmarks.landmark[8].y < hand_landmarks.landmark[5].y
                        and hand_landmarks.landmark[12].y < hand_landmarks.landmark[9].y
                        and hand_landmarks.landmark[16].y < hand_landmarks.landmark[13].y  
                        and hand_landmarks.landmark[20].y < hand_landmarks.landmark[17].y   
                    ):
                        fingers = 4

                    if (hand_landmarks.landmark[8].y < hand_landmarks.landmark[5].y
                        and hand_landmarks.landmark[12].y < hand_landmarks.landmark[9].y
                        and hand_landmarks.landmark[16].y < hand_landmarks.landmark[13].y  
                        and hand_landmarks.landmark[20].y < hand_landmarks.landmark[17].y  
                        and hand_landmarks.landmark[4].x > hand_landmarks.landmark[5].x
                    ):
                        fingers = 5

                    
                    if self.i < 5 :
                        if Number_random[self.i] == 0:
                            if(
                                fingers == 0
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
                                if self.i < 5:
                                    # If there are more numbers, return current index
                                    return self.i
                                else:
                                    # If all numbers are answered, reset and return 0
                                    self.i = 0
                                    # Reset Number_random for new set of random numbers
                                    Number_random = [0] + [rd.randint(1, 5) for _ in range(4)]
                                    return 999


                        if Number_random[self.i] == 1:
                            if(
                                fingers == 1
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
                                if self.i < 5:
                                    # If there are more numbers, return current index
                                    return self.i
                                else:
                                    # If all numbers are answered, reset and return 0
                                    self.i = 0
                                    # Reset Number_random for new set of random numbers
                                    Number_random = [0] + [rd.randint(1, 5) for _ in range(4)]
                                    return 999
                        if Number_random[self.i] == 2:
                            if (
                                fingers == 2
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
                                if self.i < 5:
                                    # If there are more numbers, return current index
                                    return self.i
                                else:
                                    # If all numbers are answered, reset and return 0
                                    self.i = 0
                                    # Reset Number_random for new set of random numbers
                                    Number_random = [0] + [rd.randint(1, 5) for _ in range(4)]
                                    return 999
                        if Number_random[self.i] == 3:
                            if (
                                fingers == 3
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
                                if self.i < 5:
                                    # If there are more numbers, return current index
                                    return self.i
                                else:
                                    # If all numbers are answered, reset and return 0
                                    self.i = 0
                                    # Reset Number_random for new set of random numbers
                                    Number_random = [0] + [rd.randint(1, 5) for _ in range(4)]
                                    return 999
                        if Number_random[self.i] == 4:
                            if (
                                fingers == 4
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
                                if self.i < 5:
                                    # If there are more numbers, return current index
                                    return self.i
                                else:
                                    # If all numbers are answered, reset and return 0
                                    self.i = 0
                                    # Reset Number_random for new set of random numbers
                                    Number_random = [0] + [rd.randint(1, 5) for _ in range(4)]
                                    return 999
                        if Number_random[self.i] == 5:
                            if (
                                fingers == 5
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
                                if self.i < 5:
                                    # If there are more numbers, return current index
                                    return self.i , Number_random
                                else:
                                    # If all numbers are answered, reset and return 0
                                    self.i = 0
                                    # Reset Number_random for new set of random numbers
                                    Number_random = [0] + [rd.randint(1, 5) for _ in range(4)]
                                    return 999
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        return self.i
    
        


    
        


