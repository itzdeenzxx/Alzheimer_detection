const colors = ["red", "blue", "green", "yellow", "purple", "orange"];
const texts = ["red", "blue", "green", "yellow", "purple", "orange"];
const textsth = ["แดง", "น้ำเงิน", "เขียว", "เหลือง", "ม่วง", "ส้ม"];
let totalQuestions = 0;
let correctAnswers = 0;
let countdown;

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function generateRandomStroop() {
    const colorIndex = getRandomInt(colors.length);
    const textIndex = getRandomInt(texts.length);
    const color = colors[colorIndex]; 
    const text = texts[textIndex];
    const textth = textsth[textIndex]
    return { color, text, textth };
}

function updateStroop() {
    const stroop = generateRandomStroop();
    const textElement = document.getElementById("text");
    const textElement_en = document.getElementById("text-en");
    textElement_en.textContent = stroop.text;
    textElement.textContent = stroop.textth;
    textElement.style.color = stroop.color;
}

function checkAnswer(buttonClicked) {
    totalQuestions++;
    const textElement = document.getElementById("text");
    const textElement_en = document.getElementById("text-en");
    const colorOfText = textElement.style.color;
    const textContent = textElement_en.textContent;
    console.log(colorOfText)
    console.log(textContent)
    const isCorrect = (buttonClicked === "Correct" && textContent === colorOfText) ||
        (buttonClicked === "Incorrect" && textContent !== colorOfText);

    if (isCorrect) {
        correctAnswers++;
    }

    updateScore();
    updateStroop();
}

function updateScore() {
    const totalElement = document.getElementById("total");
    const correctElement = document.getElementById("correct");
    const percentageElement = document.getElementById("percentage");

    totalElement.textContent = totalQuestions;
    correctElement.textContent = correctAnswers;
    const percentage = (correctAnswers / totalQuestions) * 100 || 0;
    percentageElement.textContent = percentage.toFixed(2);
}

function startCountdown(seconds) {
    let timeLeft = seconds;
    countdown = setInterval(function () {
        if (timeLeft <= 0) {
            clearInterval(countdown);
            document.getElementById("container").style.display = "none";
            document.getElementById("score").style.display = "block";
            document.getElementById("restart-btn").style.display = "none"
        } else {
            document.getElementById("time").textContent = timeLeft;
            timeLeft--;
        }
    }, 1000);
}

function restartGame() {
    totalQuestions = 0;
    correctAnswers = 0;
    clearInterval(countdown);
    document.getElementById("container").style.display = "none";
    document.getElementById("score").style.display = "none";
    document.getElementById("startButton").style.display = "inline-block";
    document.getElementById("popup-btn").style.display = "block"
    document.getElementById("restart-btn").style.display = "none"
    document.getElementById("box-tutorial").style.display = "block"

} 

function startGame() {
    // audio_start.pause()
    totalQuestions = 0;
    correctAnswers = 0;
    document.getElementById("container").style.display = "inline-block";
    document.getElementById("startButton").style.display = "none";
    document.getElementById("popup-btn").style.display = "none"
    document.getElementById("restart-btn").style.display = "block"
    document.getElementById("box-tutorial").style.display = "none"
    
    updateStroop();
    updateScore();
    startCountdown(30);
}

updateStroop();
updateScore();

document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const dotSize = parseInt(getComputedStyle(body).getPropertyValue('--dot-size'));
    const dotSpace = parseInt(getComputedStyle(body).getPropertyValue('--dot-space'));
    
    const numCols = Math.ceil(window.innerWidth / dotSpace);
    const numRows = Math.ceil(window.innerHeight / dotSpace);

    for (let i = 0; i < numCols; i++) {
      for (let j = 0; j < numRows; j++) {
        const dot = document.createElement('div');
        dot.classList.add('dot');
        dot.style.left = `${i * dotSpace}px`;
        dot.style.top = `${j * dotSpace}px`;
        body.appendChild(dot);
      }
    }

    body.addEventListener('mousemove', (e) => {
      const dots = document.querySelectorAll('.dot');
      dots.forEach(dot => {
        const rect = dot.getBoundingClientRect();
        const distance = Math.hypot(e.clientX - rect.left, e.clientY - rect.top);

        if (distance < 150) {
          const angle = Math.atan2(rect.top - e.clientY, rect.left - e.clientX);
          const moveDistance = 25;
          dot.style.transform = `translate(${Math.cos(angle) * moveDistance}px, ${Math.sin(angle) * moveDistance}px)`;
        } else {
          dot.style.transform = '';
        }
      });
    });

    body.addEventListener('mouseleave', () => {
      const dots = document.querySelectorAll('.dot');
      dots.forEach(dot => {
        dot.style.transform = '';
      });
    });
  });
   

  function playSound(line) {
      var audio = new Audio(line);

      audio.pause();
      audio.currentTime = 0;
      audio.play();

    }


    // var audio_start = new Audio('{{ sound_file_url }}');
    // audio_start.loop = true;
    // audio_start.volume = 0.3;
    // window.onload = function () {
    //   console.log("Page loaded. Playing audio...");
    //   audio_start.play().then(function () {
    //     console.log("Audio played successfully!");
    //   }).catch(function (error) {
    //     console.error("Error playing audio:", error);
    //   });
    // };

 