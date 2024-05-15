import http.server
import socketserver

from env_loader import Env

Env.load()

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

Handler = CORSRequestHandler
server = socketserver.TCPServer(('localhost', 9000), Handler)

port = Env.get_var("HTTP_SERVER_PORT")

if not port:
    port = 9000

print(f"Server running at http://0.0.0.0:{port}")
server.serve_forever()
