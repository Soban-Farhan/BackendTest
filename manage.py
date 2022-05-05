from http.server import HTTPServer
from servers.server import HttpHandler
from settings.settings import ALLOWED_HOSTS, PORT


if __name__ == '__main__':
    httpd = HTTPServer((ALLOWED_HOSTS, PORT), HttpHandler)
    
    # Start the server and leave it running
    try:
        print('RecipeAPI started on - %s:%s' % (ALLOWED_HOSTS, PORT))
        httpd.serve_forever()
    
    # On KeyboardInterrupt close the server
    except KeyboardInterrupt:
        httpd.server_close()
        print('RecipeAPI stopped on - %s:%s' % (ALLOWED_HOSTS, PORT))
    