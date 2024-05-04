from http.server import BaseHTTPRequestHandler, HTTPServer
import threading, json

hostname = "192.168.1.156"
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
            self.wfile.write(bytes(open("conf/code/error").read(), "utf-8"))
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        message = self.rfile.read(length).decode("utf-8")
        print("client sent: "+message)
        json_msg = json.dumps(message, indent=4)
        with open("board.json","w") as outfile:
            outfile.write(json_msg)
        self.send_response(200)

if __name__ == "__main__":        
    webserver = HTTPServer((hostname, port), server)
    print("Server started http://%s:%s" % (hostname, port))

    try:
        threading.Thread(target=webserver.serve_forever()).start()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server stopped.")