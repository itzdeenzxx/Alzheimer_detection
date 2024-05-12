import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands

class Finish:
    def __init__(self):
        self.hands = mp_hands.Hands(min_detection_confidence=0.3)

    def check_finish(self, frame, finished):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results_hands = self.hands.process(rgb_frame)
        
        # Check if hands were detected
        if results_hands.multi_hand_landmarks:
            for hand_landmarks_inner in results_hands.multi_hand_landmarks:
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

                if (index_tip.y < index_dip.y and
                    middle_tip.y > middle_dip.y and
                    ring_tip.y > ring_dip.y and
                    pinky_tip.y < pinky_dip.y and
                    thumb_tip.x > thumb_ip.x) or (index_tip.y < index_dip.y and
                    middle_tip.y > middle_dip.y and
                    ring_tip.y > ring_dip.y and
                    pinky_tip.y < pinky_dip.y and
                    thumb_tip.x < thumb_ip.x):
                        finished = True

        return finished


# # Instantiate the Finish class
# finish_detector = Finish()

# # Open webcam
# cap = cv2.VideoCapture(0)

# finished = True

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Check if finished
#     finished = finish_detector.check_finish(frame, finished)
    
#     # Draw something on the frame to indicate if finished or not
#     if finished:
#         cv2.putText(frame, "Finished", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     else:
#         cv2.putText(frame, "Not Finished", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#     cv2.imshow("Frame", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
