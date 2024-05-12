const canvas = document.getElementById('canvas');
        const context = canvas.getContext('2d');
        let isDrawing = false;
        let lastX = 0;
        let lastY = 0;
        let hue = '#000000';
        let brushSize = 5;
        let opacity = 1;
        let drawingHistory = [];
        context.fillStyle = '#FFFFFF';
        context.fillRect(0, 0, canvas.width, canvas.height);

        function draw(e) {
            if (!isDrawing) return;
            context.strokeStyle = hue;
            context.lineWidth = brushSize;
            context.lineJoin = 'round';
            context.lineCap = 'round';
            context.globalAlpha = opacity;
            context.beginPath();

            context.moveTo(lastX, lastY);

            context.lineTo(e.offsetX, e.offsetY);
            context.stroke();
            [lastX, lastY] = [e.offsetX, e.offsetY];
        }

        canvas.addEventListener('mousedown', (e) => {
            isDrawing = true;
            [lastX, lastY] = [e.offsetX, e.offsetY];
        });
        canvas.addEventListener('mousemove', draw);
        canvas.addEventListener('mouseup', () => {
            isDrawing = false;
            saveDrawingState();
        });
        canvas.addEventListener('mouseout', () => {
            isDrawing = false;
        });


        canvas.addEventListener('touchstart', (e) => {
            isDrawing = true;
            [lastX, lastY] = [e.touches[0].clientX, e.touches[0].clientY];
        });
        canvas.addEventListener('touchmove', (e) => {
            e.preventDefault();
            draw({ offsetX: e.touches[0].clientX, offsetY: e.touches[0].clientY });
        });
        canvas.addEventListener('touchend', () => {
            isDrawing = false;
            saveDrawingState();
        });

        function clearCanvas() {
            context.clearRect(0, 0, canvas.width, canvas.height);
            context.fillStyle = '#FFFFFF';
            context.fillRect(0, 0, canvas.width, canvas.height);
            saveDrawingState();
        }

        function undo() {
            if (drawingHistory.length > 1) {
                drawingHistory.pop();
                context.clearRect(0, 0, canvas.width, canvas.height);
                context.putImageData(drawingHistory[drawingHistory.length - 1], 0, 0);
            } else {
                clearCanvas()
            }
        }

        function setColor(color) {
            hue = color;
            document.getElementById('colorPicker').value = color;
        }

        const colorPicker = document.getElementById('colorPicker');
        colorPicker.addEventListener('input', () => {
            hue = colorPicker.value;
        });

        const brushSizeInput = document.getElementById('brushSize');
        brushSizeInput.addEventListener('input', () => {
            brushSize = brushSizeInput.value;
        });

        const opacityInput = document.getElementById('opacity');
        opacityInput.addEventListener('input', () => {
            opacity = opacityInput.value;
        });

        function saveDrawingState() {
            let currentState = context.getImageData(0, 0, canvas.width, canvas.height);
            drawingHistory.push(currentState);
        }
        function downloadCanvas() {
            const dataURL = canvas.toDataURL('image/png');
            const link = document.createElement('a');
            link.href = dataURL;
            link.download = 'drawing-nrsz.png';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }