#!/usr/bin/env python

from http.server import SimpleHTTPRequestHandler, HTTPServer
import sys

class SoarWebServer(SimpleHTTPRequestHandler):

    def do_POST(self):
        self.wfile.write("Send your POST response here!")


def main():
    if (len(sys.argv) == 1):
        print("Enter the port number! eg \"webserver.py 80\"")
        return
    port = int(sys.argv[1])
    if (port < 0 or port > 59151): #I honestly have NO CLUE what restrictions to put on the port number
        print("The port entered is invalid!")
        return
    
    print("Starting server on port " + str(port) + "...")
    sys.stdout.flush() #I seem to need this for it to print
    server_address = ("", port)
    httpd = HTTPServer(server_address, SoarWebServer)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
