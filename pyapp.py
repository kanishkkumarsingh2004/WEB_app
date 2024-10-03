# app.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, world!")


httpd= HTTPServer(('', PORT), MyHandler)
print("serving at port", PORT)
httpd.serve_forever()

