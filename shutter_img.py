import cv2
import math
import mediapipe as mp
from google.protobuf.json_format import MessageToDict

mp_hands = mp.solutions.hands
confirm_right = 0
confirm_left = 0
count_right = 0
count_left = 0
sumcont = 0
class Hand_L_Detector:
    def __init__(self):
        self.hands = mp_hands.Hands(min_detection_confidence=0.3)
        
    def calculate_distance(self, lm1, lm2):
        return math.sqrt((lm1.x - lm2.x)**2 + (lm1.y - lm2.y)**2)

    def detect_and_count_finger_distance(self, frame):
        global confirm_right, confirm_left, count_right, count_left
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results_hands = self.hands.process(rgb_frame)

        if results_hands.multi_hand_landmarks:
             for hand_landmarks_inner, handedness_inner in zip(results_hands.multi_hand_landmarks, results_hands.multi_handedness):
                    label = MessageToDict(handedness_inner)['classification'][0]['label']

                    thumb_tip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.THUMB_TIP]
                    index_tip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    middle_tip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                    ring_tip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                    pinky_tip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.PINKY_TIP]
                    thumb_ip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.THUMB_IP]
                    index_dip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP]
                    middle_dip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP]
                    ring_dip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.RING_FINGER_DIP]
                    pinky_dip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.PINKY_DIP]

                    if label == 'Left':
                        if thumb_tip.x < thumb_ip.x and index_tip.y > index_dip.y and middle_tip.y < middle_dip.y and ring_tip.y < ring_dip.y and pinky_tip.y < pinky_dip.y:
                            cv2.putText(frame, "Left great", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                            
                    if label == 'Right':
                        if thumb_tip.x > thumb_ip.x and index_tip.y < index_dip.y and middle_tip.y > middle_dip.y and ring_tip.y > ring_dip.y and pinky_tip.y > pinky_dip.y:
                            cv2.putText(frame, "Right great", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                            
                    mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks_inner, mp_hands.HAND_CONNECTIONS)
                
    def set_zero(self):
        global confirm_right, confirm_left
        confirm_right, confirm_left = 0, 0


detector = Hand_L_Detector()

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    detector.detect_and_count_finger_distance(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

