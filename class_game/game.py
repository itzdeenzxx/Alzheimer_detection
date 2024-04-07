import cv2
import mediapipe as mp
import time
import random

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

pTime = 0
cTime = 0
random_number = random.randint(1, 5)
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            for id, lm in enumerate(hand_landmarks.landmark):
                lable = random_number
                fingers_1 = 0
                fingers_2 = 0
                fingers_3 = 0
                fingers_4 = 0
                fingers_5 = 0
                if id == 0:
                    pass

                if (
                    hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y
                    and hand_landmarks.landmark[8].x > hand_landmarks.landmark[17].x
                    or hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y
                    and hand_landmarks.landmark[0].x > hand_landmarks.landmark[8].x
                ):
                    fingers_1 += 1

                if (
                    hand_landmarks.landmark[12].y < hand_landmarks.landmark[11].y
                    and hand_landmarks.landmark[12].x > hand_landmarks.landmark[17].x
                    or hand_landmarks.landmark[12].y < hand_landmarks.landmark[11].y
                    and hand_landmarks.landmark[0].x > hand_landmarks.landmark[12].x
                ):
                    fingers_2 += 1

                if (
                    hand_landmarks.landmark[16].y < hand_landmarks.landmark[15].y
                    and hand_landmarks.landmark[16].x > hand_landmarks.landmark[17].x
                    or hand_landmarks.landmark[16].y < hand_landmarks.landmark[15].y
                    and hand_landmarks.landmark[0].x > hand_landmarks.landmark[16].x
                ):
                    fingers_3 += 1

                if (
                    hand_landmarks.landmark[20].y < hand_landmarks.landmark[19].y
                    and hand_landmarks.landmark[20].x > hand_landmarks.landmark[17].x
                    or hand_landmarks.landmark[20].y < hand_landmarks.landmark[19].y
                    and hand_landmarks.landmark[0].x > hand_landmarks.landmark[20].x
                ):
                    fingers_4 += 1

                if hand_landmarks.landmark[4].x > hand_landmarks.landmark[2].x:
                    fingers_5 += 1

                if lable == 1:
                    if (
                        fingers_1 == 1
                        and fingers_2 == 0
                        and fingers_3 == 0
                        and fingers_4 == 0
                        and fingers_5 == 0
                    ):
                        cv2.putText(
                            img,
                            f"correct!",
                            (250, 250),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                            cv2.FONT_HERSHEY_PLAIN,
                            3,
                            (255, 0, 0),
                            3,
                        )
                        pass
                if lable == 2:
                    if (
                        fingers_1 == 1
                        and fingers_2 == 1
                        and fingers_3 == 0
                        and fingers_4 == 0
                        and fingers_5 == 0
                    ):
                        cv2.putText(
                            img,
                            f"correct!",
                            (250, 250),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                            cv2.FONT_HERSHEY_PLAIN,
                            3,
                            (255, 0, 0),
                            3,
                        )
                        pass
                if lable == 3:
                    if (
                        fingers_1 == 1
                        and fingers_2 == 1
                        and fingers_3 == 1
                        and fingers_4 == 0
                        and fingers_5 == 0
                    ):
                        cv2.putText(
                            img,
                            f"correct!",
                            (250, 250),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                            cv2.FONT_HERSHEY_PLAIN,
                            3,
                            (255, 0, 0),
                            3,
                        )
                        pass
                if lable == 4:
                    if (
                        fingers_1 == 1
                        and fingers_2 == 1
                        and fingers_3 == 1
                        and fingers_4 == 1
                        and fingers_5 == 0
                    ):
                        cv2.putText(
                            img,
                            f"correct!",
                            (250, 250),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                            cv2.FONT_HERSHEY_PLAIN,
                            3,
                            (255, 0, 0),
                            3,
                        )
                        pass
                if lable == 5:
                    if (
                        fingers_1 == 1
                        and fingers_2 == 1
                        and fingers_3 == 1
                        and fingers_4 == 1
                        and fingers_5 == 1
                    ):
                        cv2.putText(
                            img,
                            f"correct!",
                            (250, 250),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                            cv2.FONT_HERSHEY_PLAIN,
                            3,
                            (255, 0, 0),
                            3,
                        )
                        pass

            # นับจำนวนนิ้วของมือขวา
            # for id, lm in enumerate(hand_landmarks.landmark):
            #     fingers_right = 0
            #     if id == 0:
            #         continue

            #     if (
            #         hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y
            #         and hand_landmarks.landmark[17].x > hand_landmarks.landmark[8].x
            #         or hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y
            #         and hand_landmarks.landmark[8].x > hand_landmarks.landmark[0].x
            #     ):
            #         fingers_right += 1

            #     if (
            #         hand_landmarks.landmark[12].y < hand_landmarks.landmark[11].y
            #         and hand_landmarks.landmark[17].x > hand_landmarks.landmark[12].x
            #         or hand_landmarks.landmark[12].y < hand_landmarks.landmark[11].y
            #         and hand_landmarks.landmark[12].x > hand_landmarks.landmark[0].x
            #     ):
            #         fingers_right += 1

            #     if (
            #         hand_landmarks.landmark[16].y < hand_landmarks.landmark[15].y
            #         and hand_landmarks.landmark[17].x > hand_landmarks.landmark[16].x
            #         or hand_landmarks.landmark[16].y < hand_landmarks.landmark[15].y
            #         and hand_landmarks.landmark[16].x > hand_landmarks.landmark[0].x
            #     ):
            #         fingers_right += 1

            #     if (
            #         hand_landmarks.landmark[20].y < hand_landmarks.landmark[19].y
            #         and hand_landmarks.landmark[17].x > hand_landmarks.landmark[20].x
            #         or hand_landmarks.landmark[20].y < hand_landmarks.landmark[19].y
            #         and hand_landmarks.landmark[20].x > hand_landmarks.landmark[0].x
            #     ):
            #         fingers_right += 1

            #     if hand_landmarks.landmark[4].x < hand_landmarks.landmark[2].x:
            #         fingers_right += 1

            # แสดงจำนวนนิ้วที่นับได้บนภาพ

            cv2.putText(
                img,
                f"1: {str(fingers_1)}",
                (100, 200),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                cv2.FONT_HERSHEY_PLAIN,
                3,
                (255, 0, 0),
                3,
            )
            cv2.putText(
                img,
                f"2: {str(fingers_2)}",
                (100, 250),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                cv2.FONT_HERSHEY_PLAIN,
                3,
                (255, 0, 0),
                3,
            )
            cv2.putText(
                img,
                f"3: {str(fingers_3)}",
                (100, 300),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                cv2.FONT_HERSHEY_PLAIN,
                3,
                (255, 0, 0),
                3,
            )
            cv2.putText(
                img,
                f"4: {str(fingers_4)}",
                (100, 350),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                cv2.FONT_HERSHEY_PLAIN,
                3,
                (255, 0, 0),
                3,
            )
            cv2.putText(
                img,
                f"5: {str(fingers_5)}",
                (100, 400),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                cv2.FONT_HERSHEY_PLAIN,
                3,
                (255, 0, 0),
                3,
            )
            cv2.putText(
                img,
                f"Number {str(random_number)}",
                (400, 150),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือซ้าย
                cv2.FONT_HERSHEY_PLAIN,
                3,
                (255, 0, 0),
                3,
            )
            # cv2.putText(
            #     img,
            #     f"Right: {str(fingers_right)}",
            #     (100, 300),  # ตำแหน่งที่จะแสดงจำนวนนิ้วมือขวา
            #     cv2.FONT_HERSHEY_PLAIN,
            #     3,
            #     (255, 0, 0),
            #     3,
            # )

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # แสดง FPS (Frames Per Second) บนภาพ
    cv2.putText(
        img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3
    )

    cv2.imshow("Image", img)

    # ตรวจจับการกดปุ่ม Esc เพื่อปิดโปรแกรม
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap
