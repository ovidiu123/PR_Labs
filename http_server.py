from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        content_type = self.headers['Content-Type']

        if content_type == "application/json":
            print("Received JSON:", post_data.decode())
        elif content_type == "application/xml":
            print("Received XML:", post_data.decode())
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Unsupported Content-Type")
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Success")

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MyServer)
    print("Server running on port 8000...")
    httpd.serve_forever()
