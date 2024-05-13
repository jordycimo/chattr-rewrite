from http.server import BaseHTTPRequestHandler, HTTPServer
import threading, os

os.remove("site/board.txt")
open("site/board.txt","x")
hostname = open("site/conf/server_url","r").read()
try:
    port = input("port: ")
    port = int(port)
except:
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
            self.wfile.write(bytes(open("site/conf/code/404").read(), "utf-8"))
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-Length'])
        message = self.rfile.read(length).decode("utf-8")
        print("client sent: "+message)
        with open("site/board.txt","a") as outfile:
            outfile.write("["+self.client_address[0]+"]: "+(message.removeprefix("\"").removesuffix("\""))+"<br>")
        self.wfile.write(bytes("ok","utf-8"))

if __name__ == "__main__":
    try:        
        webserver = HTTPServer((hostname, port), server)
    except:
        print("WOAH AN ERROR!!!!")
        Exception("Is the address correct? Maybe the firewall blocked it.")
    
    print("Server started http://%s:%s" % (hostname, port))

    try:
        threading.Thread(target=webserver.serve_forever()).start()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server stopped.")