from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

if __name__ == '__main__':
	https_server = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)
	context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
	context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")  
	https_server.socket = context.wrap_socket(https_server.socket, server_side=True)
	https_server.serve_forever()
