import cv2
import mediapipe as mp
import time
import random


class HandTracker:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands()
        self.pTime = 0
        self.random_number = random.randint(1, 5)

    def start_tracking(self, frame):

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

                    if self.random_number == 1:
                        if (
                            fingers_1 == 1
                            and fingers_2 == 0
                            and fingers_3 == 0
                            and fingers_4 == 0
                            and fingers_5 == 0
                        ):
                            cv2.putText(
                                frame,
                                f"correct!",
                                (250, 250),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                                cv2.FONT_HERSHEY_PLAIN,
                                3,
                                (255, 0, 0),
                                3,
                            )
                    elif self.random_number == 2:
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
                                (250, 250),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                                cv2.FONT_HERSHEY_PLAIN,
                                3,
                                (255, 0, 0),
                                3,
                            )
                            return 
                    elif self.random_number == 3:
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
                                (250, 250),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                                cv2.FONT_HERSHEY_PLAIN,
                                3,
                                (255, 0, 0),
                                3,
                            )
                    elif self.random_number == 4:
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
                                (250, 250),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                                cv2.FONT_HERSHEY_PLAIN,
                                3,
                                (255, 0, 0),
                                3,
                            )
                    elif self.random_number == 5:
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
                                (250, 250),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                                cv2.FONT_HERSHEY_PLAIN,
                                3,
                                (255, 0, 0),
                                3,
                            )

    def show_number(self, frame):
        cv2.putText(
            frame,
            f"Number {str(self.random_number)}",
            (400, 150),
            cv2.FONT_HERSHEY_PLAIN,
            3,
            (255, 0, 0),
            3,
        )

    def stop_tracking(self):
        self.cap.release()
        cv2.destroyAllWindows()


# Instantiate the HandTracker class and start tracking
