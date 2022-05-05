import json
from http.server import BaseHTTPRequestHandler
from recipes.urls import get_path, post_path, put_patch_path


class HttpHandler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    # Get method for our HttpHandler
    def do_GET(self):
        status, response = get_path(
            url=self.path,
            request=self.command,
            authentication=self.headers.get('Authorization')
        )
        self.respond(status, response)
    
    # Post method for our HttpHandler
    def do_POST(self):
        data_string = self.rfile.read(int(self.headers.get('Content-Length')))
        data = json.loads(data_string)
        status, response = post_path(
            url=self.path,
            request=self.command,
            authentication=self.headers.get('Authorization'),
            data=data,
        )
        self.respond(status, response)

    # Delete method for our HttpHandler
    do_DELETE = do_GET

    # PUT method for our HttpHandler
    def do_PUT(self):
        data_string = self.rfile.read(int(self.headers.get('Content-Length')))
        data = json.loads(data_string)
        status, response = put_patch_path(
            url=self.path,
            request=self.command,
            authentication=self.headers.get('Authorization'),
            data=data,
        )
        self.respond(status, response)

    # PATCH method for our HttpHandler
    do_PATCH = do_PUT

    # set header and content information for a response
    def handle_http(self, status, data):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        content = json.dumps(data)
        return bytes(content, 'UTF-8')

    # Method made to send repond back to user on postman
    def respond(self, status, data=None):
        response = self.handle_http(status, data)
        self.wfile.write(response)