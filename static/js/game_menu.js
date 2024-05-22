document.addEventListener("DOMContentLoaded", function() {
    const memorySelect = document.getElementById('memory-select');
    const observerSelect = document.getElementById('observer-select');
    const relaxSelect = document.getElementById('relax-select');

    const memoryMode = document.getElementById('memory-mode');
    const observerMode = document.getElementById('observer-mode');
    const relaxMode = document.getElementById('relax-mode');

    const modeSelect = document.getElementById('mode-select');

    const memoryBack = document.getElementById('memory-back');
    const observerBack = document.getElementById('observer-back');
    const relaxBack = document.getElementById('relax-back');

    const backHomeBtn = document.getElementById('back-home-btn');
    const backModeBtn = document.getElementById('back-mode-btn');
    const mainTitle = document.getElementById('main-title');

    function hideAllModes() {
        memoryMode.style.display = 'none';
        observerMode.style.display = 'none';
        relaxMode.style.display = 'none';
    }

    function setModeTitle(title) {
        mainTitle.textContent = title;
    }

    memorySelect.addEventListener('click', function() {
        modeSelect.style.display = 'none';
        hideAllModes();
        memoryMode.style.display = 'block';
        setModeTitle('ด้านความจำ');
        backHomeBtn.style.display = 'none';
        backModeBtn.style.display = 'inline-block';
    });

    observerSelect.addEventListener('click', function() {
        modeSelect.style.display = 'none';
        hideAllModes();
        observerMode.style.display = 'block';
        setModeTitle('ด้านการสังเกต');
        backHomeBtn.style.display = 'none';
        backModeBtn.style.display = 'inline-block';
    });

    relaxSelect.addEventListener('click', function() {
        modeSelect.style.display = 'none';
        hideAllModes();
        relaxMode.style.display = 'block';
        setModeTitle('มุมผ่อนคลาย');
        backHomeBtn.style.display = 'none';
        backModeBtn.style.display = 'inline-block';
    });

    backModeBtn.addEventListener('click', function() {
        hideAllModes();
        modeSelect.style.display = 'flex';
        setModeTitle('รายการเกมฝึกสมอง');
        backHomeBtn.style.display = 'inline-block';
        backModeBtn.style.display = 'none';
    });
});