window.onload = function() {
    openPopup();
  };
  
  // Function to open popup
  function openPopup() {
    document.getElementById("popup").style.display = "block";
  }
  
  // Function to close popup
  function closePopup() {
    document.getElementById("popup").style.display = "none";
  }
  
 // Function to submit text
function submitText() {
    var userInput = document.getElementById("name").value;
    var fileInput = document.getElementById('customFileInput');
    if(userInput.trim() === "") {
      alert("กรุณากรอกชื่อ");
    } else if (fileInput.files.length === 0) {
      alert('กรุณาเลือกรูปภาพ');
    }
    else {
      if(confirm("ยืนยันการส่งชื่อ\n\n" + userInput)) {
        closePopup();
      }
    }
  }
  

  var canvas = document.getElementById('canvas')
  var ctx = canvas.getContext('2d')
  var nameInput = document.getElementById('name')
  var overlayInput = document.getElementById('customFileInput')
  var downloadBtn = document.getElementById('download-btn')
  
  var image = new Image()
  image.crossOrigin="Nerosafezone";
  image.src = "static/img/certificate-ez.jpg"
  image.onload = function () {
      drawImage()
  }
  
  function drawImage() {
      ctx.drawImage(image, 0, 0, canvas.width, canvas.height)
      ctx.font = 'bold 30px Prompt, sans-serif';
      ctx.fillStyle = '#294B29'
      ctx.fillText(nameInput.value, 110, 120)
      var currentDate = new Date();
      var dateString = currentDate.toLocaleDateString('th-TH', { year: 'numeric', month: 'long', day: 'numeric' });

      ctx.font = 'italic 18px Prompt, sans-serif';
      ctx.fillStyle = '#FFECBF';
      ctx.fillText(dateString, 140, 465);

      if (overlayInput.files && overlayInput.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var overlayImage = new Image();
            overlayImage.onload = function() {
                cropImage(overlayImage, function(croppedImage) {
                    ctx.drawImage(croppedImage, 90, 150, 225, 225);
                });
            };
            overlayImage.src = e.target.result;
        };
        reader.readAsDataURL(overlayInput.files[0]);
    }
}
    
  
function cropImage(image, callback) {
      var canvasTemp = document.createElement('canvas');
      var ctxTemp = canvasTemp.getContext('2d');
      var minSize = Math.min(image.width, image.height);
      canvasTemp.width = minSize;
      canvasTemp.height = minSize;
      var offsetX = (image.width - minSize) / 2;
      var offsetY = (image.height - minSize) / 2;
      ctxTemp.drawImage(image, offsetX, offsetY, minSize, minSize, 0, 0, minSize, minSize);
      var croppedImage = new Image();
      croppedImage.onload = function() {
          callback(croppedImage);
      };
      croppedImage.src = canvasTemp.toDataURL('image/png');
  }

nameInput.addEventListener('input', function () {
  drawImage()
})

overlayInput.addEventListener('change', function () {
  drawImage()
})

downloadBtn.addEventListener('click', function () {
  downloadBtn.href = canvas.toDataURL('image/jpg')
  downloadBtn.download = "NRSZ - " + nameInput.value
})





function handleFileUpload(event) {
  const fileName = event.target.files[0].name;
  this.fileName = fileName;
  this.uploadStatus = "เสร็จสิ้น";
} 

document.getElementById('customFileInput').addEventListener('change', function (e) {
  var fileName = e.target.files[0].name;
  document.getElementById('customFileLabel').innerText = fileName;
});

document.addEventListener('DOMContentLoaded', function() {
  const fileInput = document.getElementById('customFileInput');

  fileInput.addEventListener('change', function() {
    const file = this.files[0];
    const fileType = file.type.split('/')[0];
    if (fileType !== 'image') {
      alert('กรุณาเลือกไฟล์รูปภาพเท่านั้น');
      this.value = '';
      document.getElementById('customFileLabel').innerText = "เลือกไฟล์";
    }
  });
});

var isPlaying = false;
    function playSound_cert(line) {
      if (!isPlaying && document.getElementById('customFileLabel').innerText != "เลือกไฟล์") {
        isPlaying = true;
        var audio = new Audio(line);

        audio.pause();
        audio.currentTime = 0;
        audio.play();

        audio.onended = function () {
          isPlaying = false;
        };
      }
    }
 
    