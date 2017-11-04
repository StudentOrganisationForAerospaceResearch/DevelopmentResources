#!/usr/bin/env python

from http.server import SimpleHTTPRequestHandler, HTTPServer
import sys

class SoarWebServer(SimpleHTTPRequestHandler):

    def do_POST(self):
        self.wfile.write("Send your POST response here!")


def main():
    port = int(sys.argv[1]) # Error check this!
    print("Starting server on port " + str(port) + "...")

    server_address = ("", port)
    httpd = HTTPServer(server_address, SoarWebServer)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
