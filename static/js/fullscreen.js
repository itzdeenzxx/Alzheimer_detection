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

let toggleState = false;
 
function toggleCamera() {
    // toggleState = !toggleState;
    // var xhr = new XMLHttpRequest();
    // xhr.open('POST', '/toggle', true);
    // xhr.setRequestHeader('Content-Type', 'application/json');
    // xhr.onreadystatechange = function () {
    // if (xhr.readyState === 4 && xhr.status === 200) {
    //     console.log('Response from server: ' + xhr.responseText);
    //     }
    // };
    // var data = JSON.stringify({"state": toggleState});
    //  xhr.send(data);

    if (!cameraStarted) {
        video.src = "/video_feed";
        // button.style.backgroundColor = "red";
        playSoundBasedOnCount(1)
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
    var start_ex = document.getElementById('start_ex');
    var one_set_finish = document.getElementById('one_set_finish');
    var last_finish = document.getElementById('last_finish');
    var five_finish = document.getElementById('five_finish');
    var finish_jib = document.getElementById('finish_jib');
    var finish_thumb = document.getElementById('finish_thumb');
    var finish_header = document.getElementById('finish_header');
    var finish_ear_head = document.getElementById('finish_ear_head');
    var finish_collar_bone = document.getElementById('finish_collar_bone');
    var ten_later = document.getElementById('ten_later');
    var finish_time = document.getElementById('finish_time');
    
    console.log("play sound!!")

    if (count === 1) {
        start_ex.play();
    } else if (count === 2) {
        one_set_finish.play();
    } else if (count === 3) {
        last_finish.play();
    } else if (count === 4) {
        five_finish.play();
    } else if (count === 5) {
        finish_jib.play();
    } else if (count === 6) {
        finish_thumb.play();
    } else if (count === 7) {
        finish_header.play();
    } else if (count === 8) {
        finish_ear_head.play();
    } else if (count === 9) {
        finish_collar_bone.play();
    } else if (count === 10) {
        ten_later.play();
    }else if (count === 11) {
        finish_time.play();
    }
}
    


setInterval(checkFingerCount, 1000);