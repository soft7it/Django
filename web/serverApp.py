# server handling logic
# from http.server import HTTPServer, SimpleHTTPRequestHandler
from http.server import HTTPServer, CGIHTTPRequestHandler
# enable CGI executeion
import cgitb 
cgitb.enable()

# config root directory
CGIHTTPRequestHandler.cgi_directories = ['/']

#create the server object
webServer = HTTPServer(
    ("127.0.0.1", 8000),
    # SimpleHTTPRequestHandler  # Factory Patern -- static page
    CGIHTTPRequestHandler  # Factory Patern  dinamic page
    )

print('Server runing...')

# run the server
webServer.serve_forever()