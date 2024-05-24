from flask import Flask, render_template, Response, jsonify , request
from waitress import serve
import threading
from camera import VideoCamera , get_queue_cam , set_queue_cam
from class_game.cam_counter import VideoCamera_Game
from camera_control import generate_frames , get_message , set_message
app = Flask(__name__, static_folder="static")

#develop mode
mode = "dev"
lock = threading.Lock()
count = 0
set_main = 1
select_player = 0
count_present = 0
state = False
@app.route("/") 
def index():
    return render_template(
        "index.html", sound_file_url="/static/sound/welcome_sound.wav"
    )

@app.route("/fitness", methods=["GET", "POST"])
def fitness():
    global set_main , count
    global state
    state = False
    count = 0
    cam.reset_all()
    set_queue_cam(0)
    set_main = 1
    cam.set_of_main(set_main)
    return render_template("camera.html", queue = set_main)
    
@app.route("/fitness2", methods=["GET", "POST"])
def fitness2():
    global set_main , count
    global state
    state = False
    count = 0
    cam.reset_all()
    set_queue_cam(0)
    set_main = 2
    cam.set_of_main(set_main)
    return render_template("camera.html", queue = set_main)

@app.route("/fitness3", methods=["GET", "POST"])
def fitness3():
    global set_main , count
    global state
    state = False
    count = 0
    cam.reset_all()
    set_queue_cam(0)
    set_main = 3
    cam.set_of_main(set_main)
    return render_template("camera.html", queue = set_main)

@app.route("/fitness4", methods=["GET", "POST"])
def fitness4():
    global set_main , count
    global state
    state = False
    count = 0
    cam.reset_all()
    set_queue_cam(0)
    set_main = 4
    cam.set_of_main(set_main)
    return render_template("camera.html", queue = set_main)

@app.route("/fitness5", methods=["GET", "POST"])
def fitness5():
    global set_main , count
    global state
    state = False
    count = 0
    cam.reset_all()
    set_queue_cam(0)
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

#send to sound
@app.route('/sound_on_cam')
def sound_on_cam():
    global count
    with lock:
        # print(get_queue_cam())
        # print(count)
        count = get_queue_cam()
        # print(count)
        
    return jsonify({'count': count})

# @app.route('/toggle', methods=['POST'])
# def toggle():
#     global state
#     data = request.get_json()
#     state = data['state']
#     print(f'Toggle state: {state}')
#     return jsonify(message=f'Toggle state is now {state}')

# game
@app.route("/game_counter", methods=["GET", "POST"])
def game_counter():
    return render_template("game_room.html")

@app.route("/stroop_game", methods=["GET", "POST"])
def stroop_game():
    return render_template("stroop.html",sound_file_url="/static/sound/stroop-bgm.mp3")

@app.route("/cam_game_count")
def cam_game_count():
    return Response(
        cam_game.gen(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )

@app.route("/game_menu" , methods=["GET","POST"])
def game_menu():
    return render_template("game_menu.html")


@app.route("/matrix_game" , methods=["GET","POST"])
def matrix_game():
    return render_template("matrix-game.html")

#infomation
@app.route("/infomation" , methods=["GET","POST"])
def infomation():
    return render_template("infomation.html")

#drawing
@app.route("/drawing" , methods=["GET","POST"])
def drawing():
    return render_template("drawing.html" ,sound_file_url="/static/sound/draw-relax.mp3")

@app.route("/memory_prev" , methods=["GET","POST"])
def memory_prev():
    return render_template("picture_game.html" ,sound_file_url="/static/sound/draw-relax.mp3")

#control game

@app.route('/video_control')
def video_control():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_message')
def get_message():
    massage = get_message()
    return jsonify(message=massage)

if __name__ == "__main__":
    
    if mode == "dev":
        app.run(debug=True,port=8080,host='0.0.0.0')
    else :
        serve(app, host='0.0.0.0', port=8080, threads=1)
