from http.server import SimpleHTTPRequestHandler

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

if __name__ == '__main__':
    from http.server import HTTPServer
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, NoCacheHandler)
    print('listen at ',  httpd.server_port)
    httpd.serve_forever()

