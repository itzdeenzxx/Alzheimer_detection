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
    if(userInput.trim() === "") {
      alert("กรุณากรอกชื่อ");
    } else {
      if(confirm("ยืนยันการส่งชื่อ\n\n" + userInput)) {
        closePopup();
      }
    }
  }
  

  var canvas = document.getElementById('canvas')
  var ctx = canvas.getContext('2d')
  var nameInput = document.getElementById('name')
  var downloadBtn = document.getElementById('download-btn')
  
  var image = new Image()
  image.crossOrigin="Nerosafezone";
  image.src = "https://i.ibb.co/KL87YJm/certificate.jpg" //เป็นลิ้งบน website
  image.onload = function () {
      drawImage()
  }
  
  function drawImage() {
      ctx.drawImage(image, 0, 0, canvas.width, canvas.height)
      ctx.font = '15px Prompt, sans-serif';
      ctx.fillStyle = '#000'
      ctx.fillText(nameInput.value, 120, 290)
    }
  
  
  nameInput.addEventListener('input', function () {
      drawImage()
  })
  
  downloadBtn.addEventListener('click', function () {
      downloadBtn.href = canvas.toDataURL('image/jpg')
      downloadBtn.download = nameInput.value
  })





// var canvas = document.getElementById('canvas')
// var ctx = canvas.getContext('2d')
// var nameInput = document.getElementById('name')
// var downloadBtn = document.getElementById('download-btn')

// var image = new Image()
// image.crossOrigin="anonymous";
// image.src = 'certificate.jpg'
// image.onload = function () {
// 	drawImage()
// }

// function drawImage() {
// 	// ctx.clearRect(0, 0, canvas.width, canvas.height)
// 	ctx.drawImage(image, 0, 0, canvas.width, canvas.height)
// 	ctx.font = '40px monotype corsiva'
// 	ctx.fillStyle = '#29e'
// 	ctx.fillText(nameInput.value, 40, 180)
// }

// nameInput.addEventListener('input', function () {
// 	drawImage()
// })

// downloadBtn.addEventListener('click', function () {
// 	downloadBtn.href = canvas.toDataURL('image/jpg')
// 	downloadBtn.download = 'Certificate - ' + nameInput.value
// })
