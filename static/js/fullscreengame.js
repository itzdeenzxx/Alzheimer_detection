function toggleFullscreengame() {
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

$(document).ready(function(){
  
    $('.button-tutorail').on('click', function(){
      $('.tutorial-popup').fadeIn('slow');
      return false;
    });
    
    // $('.tutorial-bg').on('click', function(){
    //   $('.tutorial-popup').slideUp('slow');
    //   return false;
    // });
    
     $('.close-btn').on('click', function(){
       $('.tutorial-popup').fadeOut('slow');
        return false;
     });
    
  });

  function CheckTime() {
    fetch('/time_check')
        .then(response => response.json())
        .then(data => {
            console.log("Data : ", data.count)
            if(data.count >= 60){
                window.location.href = "/cert_game"
            }
        })
        .catch(error => console.error('Error:', error));
  }
  setInterval(CheckTime, 1000);
