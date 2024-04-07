import cv2
import math
import mediapipe as mp
from google.protobuf.json_format import MessageToDict

mp_hands = mp.solutions.hands
confirm_right = 0
confirm_left = 0
count_right = 0
count_left = 0
count_final = 0


class thumb_pinky:
    def __init__(self):
        self.hands = mp_hands.Hands(min_detection_confidence=0.3)

    def calculate_distance(self, lm1, lm2):
        return math.sqrt((lm1.x - lm2.x) ** 2 + (lm1.y - lm2.y) ** 2)

    def detect_and_count_finger_distance(self, frame, count):
        global confirm_right, confirm_left, count_right, count_left, count_final

        count_final = count

        check_count = count
        if check_count == 0:
            count_left, count_right = 0, 0

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results_hands = self.hands.process(rgb_frame)

        cv2.putText(
            frame,
            str(count_final),
            (100, 130),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (255, 255, 255),
            7,
        )

        if count_final == 10:
            return 10

        if results_hands.multi_hand_landmarks:
            if confirm_left == 0 or confirm_right == 0:
                for hand_landmarks_inner, handedness_inner in zip(
                    results_hands.multi_hand_landmarks, results_hands.multi_handedness
                ):
                    label = MessageToDict(handedness_inner)["classification"][0][
                        "label"
                    ]

                    thumb_tip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.THUMB_TIP
                    ]
                    index_tip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.INDEX_FINGER_TIP
                    ]
                    middle_tip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.MIDDLE_FINGER_TIP
                    ]
                    ring_tip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.RING_FINGER_TIP
                    ]
                    pinky_tip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.PINKY_TIP
                    ]
                    thumb_ip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.THUMB_IP
                    ]
                    index_dip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.INDEX_FINGER_DIP
                    ]
                    middle_dip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.MIDDLE_FINGER_DIP
                    ]
                    ring_dip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.RING_FINGER_DIP
                    ]
                    pinky_dip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.PINKY_DIP
                    ]
                    index_pip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.INDEX_FINGER_PIP
                    ]
                    middle_pip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.MIDDLE_FINGER_PIP
                    ]
                    ring_pip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.RING_FINGER_PIP
                    ]
                    pinky_pip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.PINKY_PIP
                    ]

                    # TIP ต้องอยู่ด้านซ้าย PIP ในแนวแกน x note
                    if label == "Right":
                        if (
                            thumb_tip.y < index_tip.y
                            and index_pip.y < middle_pip.y
                            and middle_pip.y < ring_pip.y
                            and ring_pip.y < pinky_pip.y
                        ):
                            cv2.putText(
                                frame,
                                "Right great",
                                (10, 200),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1,
                                (0, 255, 0),
                                2,
                            )
                            confirm_right += 1
                            if confirm_right == 1:
                                count_right += 1

                    if label == "Left":
                        if (
                            pinky_tip.y < ring_tip.y
                            and ring_tip.y > ring_dip.y
                            and middle_tip.y > middle_dip.y
                            and index_tip.y > index_dip.y
                            and thumb_tip.x < thumb_ip.x
                        ):
                            cv2.putText(
                                frame,
                                "Left great",
                                (10, 100),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1,
                                (0, 255, 0),
                                2,
                            )
                            confirm_left += 1
                            if confirm_left == 1:
                                count_left += 1
                if count_left == count_right:
                    count_final = count_left

            elif confirm_left >= 1 and confirm_right >= 1:
                for hand_landmarks_inner, handedness_inner in zip(
                    results_hands.multi_hand_landmarks, results_hands.multi_handedness
                ):
                    label = MessageToDict(handedness_inner)["classification"][0][
                        "label"
                    ]

                    thumb_tip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.THUMB_TIP
                    ]
                    index_tip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.INDEX_FINGER_TIP
                    ]
                    middle_tip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.MIDDLE_FINGER_TIP
                    ]
                    ring_tip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.RING_FINGER_TIP
                    ]
                    pinky_tip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.PINKY_TIP
                    ]
                    thumb_ip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.THUMB_IP
                    ]
                    index_dip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.INDEX_FINGER_DIP
                    ]
                    middle_dip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.MIDDLE_FINGER_DIP
                    ]
                    ring_dip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.RING_FINGER_DIP
                    ]
                    pinky_dip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.PINKY_DIP
                    ]
                    index_pip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.INDEX_FINGER_PIP
                    ]
                    middle_pip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.MIDDLE_FINGER_PIP
                    ]
                    ring_pip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.RING_FINGER_PIP
                    ]
                    pinky_pip = hand_landmarks_inner.landmark[
                        mp_hands.HandLandmark.PINKY_PIP
                    ]

                    if label == "Left":
                        if (
                            thumb_tip.y < index_tip.y
                            and index_pip.y < middle_pip.y
                            and middle_pip.y < ring_pip.y
                            and ring_pip.y < pinky_pip.y
                        ):
                            cv2.putText(
                                frame,
                                "Left great",
                                (10, 200),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1,
                                (0, 255, 0),
                                2,
                            )
                            confirm_right += 1
                            if confirm_right >= 1 and count_right % 2 == 1:
                                count_right += 1

                    if label == "Right":
                        if (
                            pinky_tip.y < ring_tip.y
                            and ring_tip.y > ring_dip.y
                            and middle_tip.y > middle_dip.y
                            and index_tip.y > index_dip.y
                            and thumb_tip.x > thumb_ip.x
                        ):
                            cv2.putText(
                                frame,
                                "Right great",
                                (10, 100),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1,
                                (0, 255, 0),
                                2,
                            )
                            confirm_left += 1
                            if confirm_left >= 1 and count_left % 2 == 1:
                                count_left += 1

                    if (
                        count_left == count_right
                        and count_right % 2 == 0
                        and count_left % 2 == 0
                    ):
                        count_final = count_left
                        confirm_right, confirm_left = 0, 0
            mp.solutions.drawing_utils.draw_landmarks(
                frame, hand_landmarks_inner, mp_hands.HAND_CONNECTIONS
            )
        return count_final


# cap = cv2.VideoCapture(0)

# thumb_pinky_obj = thumb_pinky()
# count = 0

# while True:
#     ret, frame = cap.read()
#     frame = cv2.flip(frame,1)

#     count = thumb_pinky_obj.detect_and_count_finger_distance(frame, count)

#     cv2.imshow('Frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
