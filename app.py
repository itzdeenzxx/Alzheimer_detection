from flask import Flask, render_template, Response, request , url_for
from camera import VideoCamera
from class_game.cam_counter import VideoCamera_Game

app = Flask(__name__, static_folder="static")



set_main = 1
select_player = 0
count_present = 0

@app.route("/") 
def index():
    return render_template(
        "index.html", sound_file_url="/static/sound/welcome_sound.wav"
    )

@app.route("/fitness", methods=["GET", "POST"])
def fitness():
    global set_main
    set_main = 1
    cam.set_of_main(set_main)
    return render_template("camera.html", queue = set_main)
    
@app.route("/fitness2", methods=["GET", "POST"])
def fitness2():
    global set_main
    set_main = 2
    cam.set_of_main(set_main)
    return render_template("camera.html", queue = set_main)

@app.route("/fitness3", methods=["GET", "POST"])
def fitness3():
    global set_main
    set_main = 3
    cam.set_of_main(set_main)
    return render_template("camera.html", queue = set_main)

@app.route("/fitness4", methods=["GET", "POST"])
def fitness4():
    global set_main
    set_main = 4
    cam.set_of_main(set_main)
    return render_template("camera.html", queue = set_main)

@app.route("/fitness5", methods=["GET", "POST"])
def fitness5():
    global set_main
    set_main = 5
    cam.set_of_main(set_main)
    return render_template("camera.html", queue = set_main)

@app.route("/certificate", methods=["GET", "POST"])
def certificate() :
    return render_template("certificate.html")


cam = VideoCamera()
cam_game = VideoCamera_Game()

@app.route("/video_feed", methods=["POST", "GET"])
def video_feed():
    return Response(cam.gen(), mimetype="multipart/x-mixed-replace; boundary=frame")

# game
@app.route("/game_counter", methods=["GET", "POST"])
def game_counter():
    return render_template("game_room.html")

@app.route("/stroop_game", methods=["GET", "POST"])
def stroop_game():
    return render_template("stroop.html")

@app.route("/cam_game_count")
def cam_game_count():
    return Response(
        cam_game.gen(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )

@app.route("/game_menu" , methods=["GET","POST"])
def game_menu():
    return render_template("game_menu.html")

if __name__ == "__main__":
    app.run(debug=True,port=8080)
