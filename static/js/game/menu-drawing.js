var card_main = document.getElementById('card-container')
var card_btn_draw = document.getElementById('card-btn-draw')
var card_btn_paint = document.getElementById('card-btn-paint')
var paint = document.getElementById('select_paint')
var canvas_container = document.getElementById('canvasContainer')
var tools = document.getElementById('tools')

function select_draw(){
    card_main.style.display = 'none'
    canvas_container.style.display = 'block'
    tools.style.display = 'flex'    
}

function select_paint(){
    card_main.style.display = 'none'
    paint.style.display = 'block'
}

let input = document.getElementById('input');

const handleSearch = (e) => {
  let inputValue = e.target.value.toLowerCase();
  let array = document.getElementsByClassName('item')

  for (let i = 0; i < array.length; i++) {
    let image = array[i]
    let caption = image.getAttribute('data-caption').toLowerCase()
    let title = image.getAttribute('title').toLowerCase()
    caption.includes(inputValue) || title.includes(inputValue)? image.style.display = 'inline' : image.style.display = 'none'
  }
}
input.addEventListener('keyup', handleSearch);

window.addEventListener("load", function () {
            baguetteBox.run(".gallery", {
              captions: true,
              buttons: "auto",
              animation: "fadeIn",
            });
})

window.addEventListener("load", function () {
    baguetteBox.run(".gallery");
  });