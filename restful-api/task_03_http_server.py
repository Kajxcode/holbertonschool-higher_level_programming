#!/usr/bin/python3
"""this module defines a class and runs a server on port 8000"""
import http.server
import json
from http import HTTPStatus


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """defines class for handling get requests"""
    def do_GET(self):

        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == '/data':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        
        else:
            """unknown endpoints handling"""
            self.send_response(404)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            message = "Endpoint not found"
            self.wfile.write(message.encode("utf-8"))


if __name__ == '__main__':
    PORT = 8000
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Serving HTTP on port {PORT}...")
    httpd.serve_forever()
