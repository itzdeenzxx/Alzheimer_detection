import cv2
import math
import mediapipe as mp
from google.protobuf.json_format import MessageToDict

mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
confirm_right = 0
confirm_left = 0
count_right = 0
count_left = 0
count_final = 0

class Head_Ear_Detector:
    def __init__(self):
        self.hands = mp_hands.Hands(min_detection_confidence=0.3)
        self.pose = mp_pose.Pose(min_detection_confidence=0.5)
        self.threshold = 0.05
        
    def calculate_distance(self, lm1, lm2):
        return math.sqrt((lm1.x - lm2.x)**2 + (lm1.y - lm2.y)**2)

    def detect_and_head_finger_distance(self, frame , count):
        global confirm_right , confirm_left , count_right , count_left , count_final

        count_final = count

        check_count = count
        if check_count == 0 :
            count_left , count_right = 0 , 0
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results_hands = self.hands.process(rgb_frame)
        results_pose = self.pose.process(rgb_frame)
        
        cv2.putText(frame, str(count_final), (100, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 7)

        if count_final == 10 :
            return 10
        
        if results_hands.multi_hand_landmarks and results_pose.pose_landmarks:
            if confirm_left == 0 or confirm_right == 0 :
                for hand_landmarks_inner, handedness_inner in zip(results_hands.multi_hand_landmarks, results_hands.multi_handedness):
                    label = MessageToDict(handedness_inner)['classification'][0]['label']

                    index_tip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    
                    for landmark in results_pose.pose_landmarks.landmark:
                        if label == 'Right':
                            if True:
                                cv2.putText(frame, "Right great", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                                confirm_right += 1
                                if confirm_right == 1 :
                                    count_right += 1

                        if label == 'Left':
                            if True:
                                cv2.putText(frame, "Left great", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                                confirm_left += 1
                                if confirm_left == 1 :
                                    count_left += 1
                if count_left == count_right:
                    count_final = count_left

                # mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks_inner, mp_hands.HAND_CONNECTIONS)/-ตภคึ/-ภถตค
            
            elif confirm_left >= 1 and confirm_right >= 1 :
                for hand_landmarks_inner, handedness_inner in zip(results_hands.multi_hand_landmarks, results_hands.multi_handedness):
                    label = MessageToDict(handedness_inner)['classification'][0]['label']
                
                    index_tip = hand_landmarks_inner.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    
                    for landmark in results_pose.pose_landmarks.landmark:
                        if label == 'Left':
                            if self.calculate_distance(index_tip, landmark) < self.threshold:
                                cv2.putText(frame, "Left great", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                                confirm_right += 1
                                if confirm_right >= 1 and count_right % 2 == 1:
                                    count_right += 1

                        if label == 'Right': 
                            if self.calculate_distance(index_tip, landmark) < self.threshold:
                                cv2.putText(frame, "Right great", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                                confirm_left += 1
                                if confirm_left >= 1 and count_left % 2 == 1 :
                                    count_left += 1

                    if count_left == count_right and count_right % 2 == 0 and count_left % 2 == 0:
                        count_final = count_left
                        confirm_right , confirm_left = 0,0 
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks_inner, mp_hands.HAND_CONNECTIONS)
            if results_pose.pose_landmarks:
                for landmark in results_pose.pose_landmarks.landmark:
                    height, width, _ = frame.shape
                    cx, cy = int(landmark.x * width), int(landmark.y * height)
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)
        return count_final
# Example usage
# if __name__ == "__main__":
#     detector = Head_Ear_Detector()
#     cap = cv2.VideoCapture(0)
#     count = 0
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         count = detector.detect_and_head_finger_distance(frame,count)

#         cv2.imshow('Hand and Torso Detection', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

                    

                        
            
                


