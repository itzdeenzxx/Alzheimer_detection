from flask import Flask, render_template, Response, jsonify
import cv2
import mediapipe as mp
import threading

app = Flask(__name__)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

finger_count = 0
lock = threading.Lock()

def count_fingers(hand_landmarks):
    # ข้อมูลตำแหน่งของนิ้วที่ใช้ในการตรวจจับการชูนิ้ว
    finger_tips = [4, 8, 12, 16, 20]
    count = 0
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1
    return count

def gen_frames():
    global finger_count
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(image)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    with lock:
                        finger_count = count_fingers(hand_landmarks)
            else:
                with lock:
                    finger_count = 0

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/finger_count')
def get_finger_count():
    global finger_count
    with lock:
        count = finger_count
    return jsonify({'count': count})

if __name__ == '__main__':
    app.run(debug=True)
