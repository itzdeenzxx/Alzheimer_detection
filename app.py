from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__, static_folder='static')

cam = VideoCamera()

@app.route('/')
def index():
    return render_template('index.html', sound_file_url='/static/sound/welcome_sound.wav')

@app.route('/fitness', methods=['GET', 'POST'])
def fitness():
    
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    return Response(cam.gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
