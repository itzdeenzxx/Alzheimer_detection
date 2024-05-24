const thaiLetters = ['ก', 'ข', 'ค', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ญ', 'ด', 'ต', 'ถ', 'ท', 'น', 'บ', 'ป', 'ผ', 'พ', 'ฟ', 'ม', 'ย', 'ร', 'ล', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'อ'];
const similarThaiWords = ['ภาระ', 'ภาระกิจ', 'ราชา', 'ราฃา', 'สะบาย', 'สบาย', 'นาน', 'บาน', 'พบ', 'ฟบ', 'พอ', 'ฟอ', 'สว่าง', 'สว่างงาม', 'เมือง', 'เนือง'];
const images = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg']; // Add the paths to your images here
const newImages = ['newimage1.jpg', 'newimage2.jpg', 'newimage3.jpg', 'newimage4.jpg', 'newimage5.jpg']; // Add the paths to your new images here

let currentItem = '';
let previousItem = '';
let score = 0;
let correctAnswers = 0;
let wrongAnswers = 0;
let wrongAnswersLog = [];
let rounds = 0;
const totalRounds = 20;
const yesRounds = 6;
let scheduledYesRounds;
let timer;
let countdown;
let gameType = '';

const letterContainer = document.getElementById('letter-container');
const yesBtn = document.getElementById('yes-btn');
const noBtn = document.getElementById('no-btn');
const message = document.getElementById('message');
const scoreboard = document.getElementById('scoreboard');
const startBtn = document.getElementById('start-btn');
const backBtn = document.getElementById('back-btn');
const timerDisplay = document.getElementById('timer');
const modeSelection = document.getElementById('mode-selection');
const gameContainer = document.getElementById('game-container');
const modeButtons = document.querySelectorAll('.mode-btn');
const keyHint = document.getElementById('key-hint');

modeButtons.forEach(button => {
    button.addEventListener('click', () => {
        gameType = button.dataset.mode;
        modeSelection.classList.add('hidden');
        gameContainer.classList.remove('hidden');
        resetGame();
        detectDevice();
        // Hide the start button until a mode is selected
        startBtn.classList.remove('hidden');
    });
});

function detectDevice() {
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    if (!isMobile) {
        keyHint.classList.remove('hidden');
    } else {
        keyHint.classList.add('hidden');
    }
}

function getRandomItem() {
    if (gameType === 'thai-letters') {
        return thaiLetters[Math.floor(Math.random() * thaiLetters.length)];
    } else if (gameType === 'similar-thai-words') {
        return similarThaiWords[Math.floor(Math.random() * similarThaiWords.length)];
    } else if (gameType === 'images') {
        return images[Math.floor(Math.random() * images.length)];
    } else if (gameType === 'new-images') {
        return newImages[Math.floor(Math.random() * newImages.length)];
    }
}

function scheduleYesRounds() {
    let yesRounds = new Set();
    while (yesRounds.size < 6) {
        yesRounds.add(Math.floor(Math.random() * (totalRounds - 1)) + 1); // ตั้งค่าให้เป็น "ใช่" อย่างน้อย 6 รอบ
    }
    return yesRounds;
}

function resetGame() {
    score = 0;
    correctAnswers = 0;
    wrongAnswers = 0;
    wrongAnswersLog = [];
    rounds = 0;
    scheduledYesRounds = scheduleYesRounds();
    letterContainer.textContent = '';
    message.textContent = '';
    scoreboard.classList.add('hidden');
    yesBtn.disabled = false;
    noBtn.disabled = false;
    clearTimeout(timer);
    clearInterval(countdown);
}

function startGame() {
    startBtn.classList.add('hidden');
    nextRound(true);
}

function nextRound(isFirstRound = false) {
    clearTimeout(timer);
    clearInterval(countdown);
    if (rounds >= totalRounds) {
        endGame();
        return;
    }
    previousItem = currentItem;
    if (scheduledYesRounds.has(rounds)) {
        currentItem = previousItem;
    } else {
        currentItem = getRandomItem();
        while (currentItem === previousItem) {
            currentItem = getRandomItem();
        }
    }
    if (gameType === 'images' || gameType === 'new-images') {
        letterContainer.innerHTML = `<img src="${currentItem}" alt="Image">`;
    } else {
        letterContainer.textContent = currentItem;
    }
    message.textContent = '';
    rounds++;
    
    if (isFirstRound) {
        yesBtn.disabled = true;
        noBtn.disabled = true;
        timerDisplay.textContent = 'เวลา: 5';
        countdown = startCountdown(5, () => {
            yesBtn.disabled = false;
            noBtn.disabled = false;
            nextRound();
        });
    } else {
        timerDisplay.textContent = 'เวลา: 5';
        countdown = startCountdown(5, () => {
            handleAnswer(false, true);
        });
    }
}

function startCountdown(seconds, callback) {
    let remainingTime = seconds;
    timerDisplay.textContent = `เวลา: ${remainingTime}`;
    const interval = setInterval(() => {
        remainingTime--;
        timerDisplay.textContent = `เวลา: ${remainingTime}`;
        if (remainingTime <= 0) {
            clearInterval(interval);
            callback();
        }
    }, 1000);
    return interval;
}

function handleAnswer(isCorrect, isTimeout = false) {
    clearInterval(countdown);
    if (isCorrect) {
        correctAnswers++;
        message.textContent = 'ถูกต้อง!';
    } else {
        wrongAnswers++;
        message.textContent = isTimeout ? 'หมดเวลา!' : 'ผิด!';
        wrongAnswersLog.push({ correctItem: previousItem, selectedItem: currentItem });
    }
    updateScoreboard();
    nextRound();
}

function updateScoreboard() {
    scoreboard.textContent = `รอบที่: ${rounds}/${totalRounds}`;
}

function endGame() {
    message.textContent = `เกมจบแล้ว!`;
    const scoreMessage = `คะแนนสุดท้าย: ${correctAnswers} จากทั้งหมด ${totalRounds} รอบ`;
    let mistakeMessage = `ไม่มีข้อผิดพลาด`;
    if (wrongAnswers > 0) {
        mistakeMessage = 'ข้อผิดพลาด:';
        wrongAnswersLog.forEach((log, index) => {
            mistakeMessage += `<br>${index + 1}. `;
            if (gameType === 'images' || gameType === 'new-images') {
                mistakeMessage += `รูปภาพที่ถูกแสดง: <img src="${log.correctItem}" alt="Image" style="height: 50px;">, รูปภาพที่ถูกเลือก: <img src="${log.selectedItem}" alt="Image" style="height: 50px;">`;
            } else {
                mistakeMessage += `คำหรือรูปภาพที่ถูกแสดง: ${log.correctItem}, คำหรือรูปภาพที่ถูกเลือก: ${log.selectedItem}`;
            }
        });
    }
    scoreboard.classList.remove('hidden');
    scoreboard.innerHTML = `<p>${scoreMessage}</p><p>${mistakeMessage}</p>`;
    startBtn.classList.remove('hidden');
}

yesBtn.addEventListener('click', () => {
    clearTimeout(timer);
    clearInterval(countdown);
    handleAnswer(currentItem === previousItem);
});

noBtn.addEventListener('click', () => {
    clearTimeout(timer);
    clearInterval(countdown);
    handleAnswer(currentItem !== previousItem);
});

startBtn.addEventListener('click', startGame);

backBtn.addEventListener('click', () => {
    gameContainer.classList.add('hidden');
    modeSelection.classList.remove('hidden');
    startBtn.classList.add('hidden');
});

document.addEventListener('keydown', (event) => {
    if (event.code === 'ShiftLeft' && !noBtn.disabled) {
        noBtn.click();
    }
    if (event.code === 'ShiftRight' && !yesBtn.disabled) {
        yesBtn.click();
    }
});
 