from http.server import BaseHTTPRequestHandler, HTTPServer
import threading, json

hostname = "192.168.1.156"
port = str(input("port: "))
if not port:
    port = 8000

class server(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(open("site"+self.path,"r").read(),"utf-8"))
        except:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes(open("conf/code/404").read(), "utf-8"))
    def do_POST(self):
        self.send_response(201)
        length = int(self.headers['Content-Length'])
        message = self.rfile.read(length).decode("utf-8")
        print("client sent: "+message)
        with open("site/board.txt","a") as outfile:
            outfile.write(message.removeprefix("\"").removesuffix("\""))

if __name__ == "__main__":        
    webserver = HTTPServer((hostname, port), server)
    print("Server started http://%s:%s" % (hostname, port))

    try:
        threading.Thread(target=webserver.serve_forever()).start()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server stopped.")