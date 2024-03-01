import cv2
import math
import mediapipe as mp
from google.protobuf.json_format import MessageToDict

mp_hands = mp.solutions.hands




class Hand_L_Detector:
    def __init__(self):
        self.hands = mp_hands.Hands(min_detection_confidence=0.3)
        self.count_work = 0

    def calculate_distance(self, lm1, lm2):
        return math.sqrt((lm1.x - lm2.x)**2 + (lm1.y - lm2.y)**2)

    def detect_and_count_finger_distance(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Hand Detection using Mediapipe
        results_hands = self.hands.process(rgb_frame)
        if results_hands.multi_hand_landmarks:
            for hand_landmarks in results_hands.multi_hand_landmarks:
                # ตำแหน่งของ point นิ้ว
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

                middle_dip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP]
                ring_dip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP]
                pinky_dip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP]
                
                distance_threshold_thump = 0.05  
                distance_index_thumb = self.calculate_distance(
                    thumb_tip,index_tip
                )
                
                # Assume hand_landmarks is the list of landmarks detected in the hand
# Assume frame is the current frame of the video

                if len(results_hands.multi_handedness) == 2:
                    for hand_landmarks in results_hands.multi_hand_landmarks:
                        for i in results_hands.multi_handedness:
                            label = MessageToDict(i)['classification'][0]['label']
                            if label == 'Left':
                                if distance_index_thumb < distance_threshold_thump:
                                    cv2.putText(frame, "JIB L", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                                    if (middle_tip.x < middle_dip.x and ring_tip.x < ring_dip.x and pinky_tip.x < pinky_dip.x) and (middle_tip.y < middle_dip.y and ring_tip.y < ring_dip.y and pinky_tip.y < pinky_dip.y):
                                        print("L Hand: Thumb below all fingertips and fingers below respective dips.")
                                    # Show hand as left hand
                                    cv2.putText(frame, "Left Hand", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                            elif label == 'Right':
                                if (thumb_tip.x < index_tip.x and thumb_tip.x < middle_tip.x and thumb_tip.x < ring_tip.x and thumb_tip.x < pinky_tip.x) and (middle_tip.y < middle_dip.y and ring_tip.y < ring_dip.y and pinky_tip.y < pinky_dip.y):
                                    cv2.putText(frame, 'LR', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                                    # Show hand as right hand
                                    
                                    hand_text = "Right Hand"
                                    
                                    text_x = int(hand_landmarks.landmark[0].x * frame.shape[1])
                                    text_y = int(hand_landmarks.landmark[0].y * frame.shape[0])
                                    
                                    cv2.putText(frame, hand_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                        else:
                            print("Finger tips are not below their respective dips.")
                else:
                    cv2.putText(frame, "pls 2 hand", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    
                mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

