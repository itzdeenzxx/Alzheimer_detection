function toggleFullscreen() {
    const element = document.getElementById('fullscreen-cam');
    if (isSafari()) {
        alert("ขออภัย คุณกำลังใช้ Safari ซึ่งไม่สามารถเปิดหน้าเต็มจอได้ในบางกรณี กรุณาลองใช้เบราว์เซอร์อื่นเพื่อเปิดเต็มจอ");
    }
    if (document.fullscreenElement) {
        document.exitFullscreen();
    } else {
        element.requestFullscreen().catch(err => {
            console.error(`Error attempting to enable full-screen mode: ${err.message}`);
        });
    }
}
function isSafari() {
    return /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
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




$(document).ready(function(){
  
    $('.popup-btn').on('click', function(){
      $('.video-popup').fadeIn('slow');
      return false;
    });
    
    $('.popup-bg').on('click', function(){
      $('.video-popup').slideUp('slow');
      return false;
    });
    
     $('.close-btn').on('click', function(){
       $('.video-popup').fadeOut('slow');
        return false;
     });
    
  });

  let lastPlayedCount = 0;

function checkFingerCount() {
    fetch('/sound_on_cam')
        .then(response => response.json())
        .then(data => {
            console.log("Data : ", data.count)
            console.log("Last Data : ",lastPlayedCount)
            if (data.count !== lastPlayedCount) {
                lastPlayedCount = data.count;
                playSoundBasedOnCount(data.count);

            }
        })
        .catch(error => console.error('Error:', error));
}

function playSoundBasedOnCount(count) {
    var bellSound = document.getElementById('bellSound');
    var duckSound = document.getElementById('duckSound');
    var carSound = document.getElementById('carSound');

    if (count === 1) {
        bellSound.play();
    } else if (count === 2) {
        duckSound.play();
    } else if (count === 3) {
        carSound.play();
    }
}

setInterval(checkFingerCount, 1000);