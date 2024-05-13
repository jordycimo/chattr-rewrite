let textinput;
let fr = new FileReader();
let url = "192.168.40.193";

function send(msg) {
  httpPost(url,"text",msg+"\n");
}

function setup() {
  frameRate(5)
  createCanvas(100, 20);
  text("chattr v1.2",0,10)
  textinput = createInput();
}

function funcbutton() {
  send(textinput.value())
  location.reload()
}

function keyPressed() {
  if(keyCode == 13) {
    funcbutton();
  }
}