import cv2
import numpy as np
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose

count_work = 0

class VideoCamera(object):
    def __init__(self):
        self.camera_index = 0 
        self.video = cv2.VideoCapture(self.camera_index)
        self.face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.3)
        self.hands = mp_hands.Hands(min_detection_confidence=0.3)
        self.pose = mp_pose.Pose(min_detection_confidence=0.3, min_tracking_confidence=0.3)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        if not ret:
            return None
        cv2.putText(frame, str(count_work), (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 255, 255), 2)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Face Detection using Mediapipe
        results_face = self.face_detection.process(rgb_frame)
        if results_face.detections:
            for detection in results_face.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(frame, bbox, (0, 0, 255), 2)

        # Hand Detection using Mediapipe
        results_hands = self.hands.process(rgb_frame)
        if results_hands.multi_hand_landmarks:
            for hand_landmarks in results_hands.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Body (Pose) Detection using Mediapipe
        results_pose = self.pose.process(rgb_frame)
        if results_pose.pose_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # self.overlay_image(frame)

        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            return None
        return jpeg.tobytes()
    
    def overlay_image(self, frame):
        # อ่านรูปภาพ overlay
        overlay_image = cv2.imread('/static/img/benefit_2_4.png', cv2.IMREAD_UNCHANGED)

        # ตรวจสอบว่าสามารถอ่านรูปภาพได้หรือไม่
        if overlay_image is None:
            print("ไม่สามารถอ่านรูปภาพ overlay ได้")
            return

        # ตำแหน่งที่ต้องการ overlay
        x, y = 50, 50

        # คำนวณขนาดของรูป overlay ให้มีขนาดเท่ากับภาพจากกล้อง
        h, w = overlay_image.shape[:2]
        overlay = cv2.resize(overlay_image, (w, h))

        # คำนวณตำแหน่งที่ต้องการ overlay บนภาพจากกล้อง
        rows, cols = overlay.shape[:2]
        roi = frame[y:y+rows, x:x+cols]

        # หา mask จากรูป overlay
        overlay_mask = overlay[:, :, 3]

        # หา inverse mask
        overlay_mask_inv = cv2.bitwise_not(overlay_mask)

        # ดึงสีจากภาพจากกล้องที่อยู่ใน ROI
        frame_bg = cv2.bitwise_and(roi, roi, mask=overlay_mask_inv)

        # ดึงสีจากรูป overlay
        overlay_fg = cv2.bitwise_and(overlay, overlay, mask=overlay_mask)

        # ผสมภาพจากกล้องกับภาพ overlay
        combined = cv2.addWeighted(frame_bg, 1, overlay_fg, 1, 0)

        # นำภาพที่ผสมเสร็จแล้วมาใส่ใน ROI
        frame[y:y+rows, x:x+cols] = combined

    

# Usage example
if __name__ == "__main__":
    camera = VideoCamera()
    while True:
        frame_bytes = camera.get_frame()
        if frame_bytes is not None:
            # Process the frame bytes as needed (e.g., display or save the image)
            pass
