var input, button;
const url = "192.168.1.156:8000"


function setup() {
  createCanvas(100, 20);
  text("chattr v1.2",0,10)
  input = createInput();
  button = createButton("SEND");
  button.mousePressed(send(input.value()));
}

function send(msg) {
  httpPost(url,"text",str(msg)+"\n");
}