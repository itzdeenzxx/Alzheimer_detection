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
    return { color, text , textth };
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
    countdown = setInterval(function() {
        if (timeLeft <= 0) {
            clearInterval(countdown);
            document.getElementById("container").style.display = "none";
            document.getElementById("score").style.display = "block";
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
}

function startGame() {
    totalQuestions = 0;
    correctAnswers = 0;
    document.getElementById("container").style.display = "inline-block";
    document.getElementById("startButton").style.display = "none";
    updateStroop();
    updateScore();
    startCountdown(30);
}

// Initial setup
updateStroop();
updateScore();