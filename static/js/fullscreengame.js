function toggleFullscreengame() {
    const element = document.getElementById('fullscreen-cam');
    if (document.fullscreenElement) {
        document.exitFullscreen();
    } else {
        element.requestFullscreen().catch(err => {
            console.error(`Error attempting to enable full-screen mode: ${err.message}`);
        });
    }
}
function checkOrientation() {
    if (window.orientation === 90 || window.orientation === -90) {
        const fullscreenElement = document.getElementById('fullscreen-cam');
        if (fullscreenElement.requestFullscreen) {
            fullscreenElement.requestFullscreen().catch(err => {
                console.error(`Error attempting to enable full-screen mode: ${err.message}`);
            });
        } else if (fullscreenElement.mozRequestFullScreen) {
            fullscreenElement.mozRequestFullScreen().catch(err => {
                console.error(`Error attempting to enable full-screen mode: ${err.message}`);
            });
        } else if (fullscreenElement.webkitRequestFullscreen) {
            fullscreenElement.webkitRequestFullscreen().catch(err => {
                console.error(`Error attempting to enable full-screen mode: ${err.message}`);
            });
        } else if (fullscreenElement.msRequestFullscreen) {
            fullscreenElement.msRequestFullscreen().catch(err => {
                console.error(`Error attempting to enable full-screen mode: ${err.message}`);
            });
        }
    } else {
        if (document.fullscreenElement) {
            document.exitFullscreen();
        }
    }
}
window.addEventListener('load', checkOrientation);
window.addEventListener('orientationchange', checkOrientation);

var video = document.getElementById('fullscreen-cam');
var button = document.getElementById('toggle_camera');
var cameraStarted = false;

function toggleCameragame() {
    if (!cameraStarted) {
        video.src = "/cam_game_count";
        button.innerHTML = "พักการเล่นเกม";
        cameraStarted = true;
    } else {
        video.src = "static/img/bg-game-count.jpg";
        button.innerHTML = "เริ่มเล่นเกม";
        cameraStarted = false;
    }
}


// ตรวจสอบรูปไหนที่กำลังอยู่หน้าสไลด์


