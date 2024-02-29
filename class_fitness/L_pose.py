import cv2
import math
import mediapipe as mp

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
                thump_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

                middle_dip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
                ring_dip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
                pinky_dip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y
                

                

                distance_threshold_thump = 0.05  
                distance_index_thumb = self.calculate_distance(
                    thump_tip,index_tip
                )
                
                
                if distance_index_thumb < distance_threshold_thump:
                    if (middle_tip < middle_dip) and (ring_tip < ring_dip) and (pinky_tip < pinky_dip):
                        self.count_work += 1
                        # cv2.putText(frame, f'Index Finger Tip close to Thumb Tip! Count: {self.count_work}', (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(frame, "JIB Pose Detected!", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    else :
                        print("Finger tips are not below their respective dips.")
                # วาด landmark ของมือ
    
                mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

