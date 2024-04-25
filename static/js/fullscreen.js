function toggleFullscreen() {
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

function toggleCamera() {
    if (!cameraStarted) {
        video.src = "/video_feed";
        // button.style.backgroundColor = "red";
        button.textContent = "พักการออกกำลังกาย";
        cameraStarted = true;
    } else {
        video.src = "static/img/pre-fitness-test.jpg";
        // button.style.backgroundColor = "";
        button.textContent = "เริ่มออกกำลังกาย";
        cameraStarted = false;
    }
}


// ตรวจสอบรูปไหนที่กำลังอยู่หน้าสไลด์

function openPopup() {
    document.getElementById("videoPopup").style.display = "block";
  }
  
  // ฟังก์ชันเพื่อปิดป็อปอัพ
  function closePopup() {
    document.getElementById("videoPopup").style.display = "none";
  }
