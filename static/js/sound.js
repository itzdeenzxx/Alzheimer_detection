var isPlaying = false;
    function playSound(line) {
      if (!isPlaying) {
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

   