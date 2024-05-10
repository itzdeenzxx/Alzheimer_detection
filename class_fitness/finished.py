import cv2
import mediapipe as mp
mp_hands = mp.solutions.hands

class Finish:
    def __init__(self):
        self.hands = mp_hands.Hands(min_detection_confidence=0.3)

    def check_finish(self, frame , finished):
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results_hands = self.hands.process(rgb_frame)
        for hand_landmarks_inner, handedness_inner in zip(results_hands.multi_hand_landmarks, results_hands.multi_handedness):
            
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

                    if thumb_tip.x < thumb_ip.x and index_tip.y > index_dip.y and middle_tip.y < middle_dip.y and ring_tip.y < ring_dip.y and pinky_tip.y < pinky_dip.y:
                       finished = True

                # mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks_inner, mp_hands.HAND_CONNECTIONS)/-ตภคึ/-ภถตค
            
            
        return finished

            
                


