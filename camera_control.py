import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
message = ""
def generate_frames():
    global message
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = cv2.flip(frame, 1)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                if len(results.multi_hand_landmarks) == 2:
                    message = "โปรดแบมือ 1 ข้าง"
                else:
                    for hand_landmarks in results.multi_hand_landmarks:
                        handedness = results.multi_handedness[0].classification[0].label
                        if handedness == 'Right':
                            message = "1"
                        else:
                            message = "2"
            else:
                message = "none"

            ret, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()
            print("messeage :" , message)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def get_message() :
    global message
    return message

def set_message(value):
    global message
    message = value
