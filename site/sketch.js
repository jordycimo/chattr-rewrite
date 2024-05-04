var board;
const url = "192.168.1.156:8000"

function preload() {
    board = loadJSON("board.json");
}

function setup() {
  createCanvas(800, 600);
}

function draw() {
  background(220);
  stroke(0);
  for(var i=0;i<board.messages.length;i++) {
    text(board.messages[i],0,(i+1)*10);
  }
}

function send(msg) {
  httpPost(url,"text",str(msg));
}