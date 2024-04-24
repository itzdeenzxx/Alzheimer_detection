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
      alert("Please enter some text before submitting.");
    } else {
      if(confirm("Are you sure you want to submit the following text?\n\n" + userInput)) {
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
  image.src = "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1nACq6.img?w=696&h=392&m=6" //เป็นลิ้งบน website
  image.onload = function () {
      drawImage()
  }
  
  function drawImage() {
      // ctx.clearRect(0, 0, canvas.width, canvas.height)
      ctx.drawImage(image, 0, 0, canvas.width, canvas.height)
      ctx.font = '30px K2D'
      ctx.fillStyle = '#29e'
      ctx.fillText(nameInput.value, 40, 180)
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
