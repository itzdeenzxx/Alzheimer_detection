from flask import Flask, render_template, Response, request
from camera import VideoCamera

app = Flask(__name__, static_folder="static")

cam = VideoCamera()


@app.route("/")
def index():
    return render_template(
        "index.html", sound_file_url="/static/sound/welcome_sound.wav"
    )


@app.route("/fitness", methods=["GET", "POST"])
def fitness():
    return render_template("camera.html")


@app.route("/video_feed")
def video_feed():
<<<<<<< HEAD
    return Response(cam.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

# game
@app.route('/game_counter', methods=['GET', 'POST'])
def game_counter():
    return render_template('game_menu.html')

@app.route('/cam_game_count')
def cam_game_count():
    return Response(cam_game.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
=======
    return Response(cam.gen(), mimetype="multipart/x-mixed-replace; boundary=frame")
>>>>>>> b5ccad74f13c20cbf7c02cf154b88c33128a7eda


if __name__ == "__main__":
    app.run(debug=True)
