import time
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "192.168.1.9"
PORT = 9999
class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>HELLO</h1></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content", "app/jason")
        self.end_headers()

        date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.wfile.write(bytes(f'{date}' "utf-8"))
server = HTTPServer((HOST, PORT), NeuralHTTP)
server.serve_forever()
server.server_close()
