#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import cgi
import os

class S(BaseHTTPRequestHandler):
    def _set_response(self, ct):
        self.send_response(200)
        self.send_header('Content-type', ct)
        self.end_headers()

    def do_GET(self):
        if self.path == "/size.txt":
            os.system("sh size.sh")
            file = open(os.environ["FS"]+"/size.txt")
            self._set_response('text/plain')
            js = file.read()
            self.wfile.write(js.encode('utf-8')) 
        elif self.path == "/start.html":
            os.system("rm -f "+os.environ["FS"]+"/stop")
            os.system("sh loadfs.sh &")
            file = open("start.html")
            self._set_response('text/html')
            self.wfile.write(file.read().encode('utf-8'))
        elif self.path == "/index.html" or self.path == "/":
            os.system("touch "+os.environ["FS"]+"/stop")
            file = open("index.html")
            self._set_response('text/html')
            self.wfile.write(file.read().encode('utf-8'))
        elif self.path == "/index.css":
            file = open("index.css")
            self._set_response('text/css')
            self.wfile.write(file.read().encode('utf-8'))
        else: 
            self._set_response('text/html')
            self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
