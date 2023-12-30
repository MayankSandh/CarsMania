const canvas = document.getElementById('myCanvas');
const context = canvas.getContext('2d');
let isDrawing = false;

function toggleDrawing() {
  isDrawing = !isDrawing;
  if (isDrawing) {
    canvas.style.cursor = 'crosshair';
    document.getElementById('drawBtn').classList.add('active');
    context.beginPath();
  } else {
    canvas.style.cursor = 'default';
    document.getElementById('drawBtn').classList.remove('active');
    context.closePath();
  }
}

function startDrawing(event) {
  if (!isDrawing || event.buttons !== 1) return;

  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;

  context.lineTo(x, y);
  context.stroke();
  context.beginPath(); 
  context.moveTo(x, y);
}

function endDrawing() {
    context.closePath();
    context.beginPath(); 
}

document.getElementById('drawBtn').addEventListener('click', toggleDrawing);
canvas.addEventListener('mousemove', startDrawing);
canvas.addEventListener('mouseup', endDrawing);
