const canvas = document.getElementById('canvas');

        const context = canvas.getContext('2d');
        let isDrawing = false;
        let lastX = 0;
        let lastY = 0;
        let hue = '#000000';
        let brushSize = 5;
        let opacity = 1;
        let drawingHistory = [];
        let eraser = false
        context.fillStyle = '#FFFFFF';
        context.fillRect(0, 0, canvas.width, canvas.height);

        function draw(e) {
            if (!isDrawing) return;
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            context.strokeStyle = hue;
            context.lineWidth = brushSize;
            context.lineJoin = 'round';
            context.lineCap = 'round';
            context.globalAlpha = opacity;
            // console.log(opacity)
            context.beginPath();
        
            context.moveTo(lastX, lastY);
        
            context.lineTo(x, y);
            context.stroke();
            [lastX, lastY] = [x, y];
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
            const rect = canvas.getBoundingClientRect();
            const x = e.touches[0].clientX - rect.left;
            const y = e.touches[0].clientY - rect.top;
            [lastX, lastY] = [x, y];
        });
        
        canvas.addEventListener('touchmove', (e) => {
            e.preventDefault();
            draw({ clientX: e.touches[0].clientX, clientY: e.touches[0].clientY });
        });
        
        canvas.addEventListener('touchend', () => {
            isDrawing = false;
            saveDrawingState();
        });

        function clearCanvas() {
            context.globalAlpha = 1
            document.getElementById('eraser').style.backgroundColor = '#FFFFFF'
            context.clearRect(0, 0, canvas.width, canvas.height);
            context.fillStyle = '#FFFFFF';
            context.fillRect(0, 0, canvas.width, canvas.height);
            context.globalAlpha = opacity
            saveDrawingState();
        }

        function undo() {
            document.getElementById('eraser').style.backgroundColor = '#FFFFFF'
            if (drawingHistory.length > 1) {
                drawingHistory.pop();
                context.clearRect(0, 0, canvas.width, canvas.height);
                context.putImageData(drawingHistory[drawingHistory.length - 1], 0, 0);
            } else {
                clearCanvas()
            }
        }

        function setColor(color) {
            canvas.style.cursor = 'url("/static/img/cursor/pen.svg"), auto';
            document.getElementById('eraser').style.backgroundColor = '#FFFFFF'
            hue = color;
            document.getElementById('colorPicker').value = color;
        }

        const colorPicker = document.getElementById('colorPicker');
        colorPicker.addEventListener('input', () => {
            document.getElementById('eraser').style.backgroundColor = '#FFFFFF'
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
        function erase() {
            // eraser = !eraser
            canvas.style.cursor = 'url("/static/img/cursor/eraser.svg"), auto';
            if(!eraser) {
                document.getElementById('eraser').style.backgroundColor = '#39818f'
                hue = '#fff';
                
            }
        }