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
