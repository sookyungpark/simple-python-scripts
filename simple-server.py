#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer

import json
import logging

class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, address, server):
        BaseHTTPRequestHandler.__init__(self, request, address, server)

    def do_GET(self):
        path, _, query_string = self.path.partition('?')
        logging.info("path: " + path + ", query string:" + query_string)

        response_body = json.dumps({"foo": "bar"}).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response_body)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        logging.info("request body:" + data.decode('utf-8'))

        response_body = json.dumps({"status": "success"}).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response_body)

def run(server_class=HTTPServer, handler=RequestHandler, port=8080):
    logging.basicConfig(level=logging.INFO)
    server = server_class(("", port), handler)
    logging.info("server starting....")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    logging.info("server closing....")
    server.server_close()

if __name__ == '__main__':
    run()