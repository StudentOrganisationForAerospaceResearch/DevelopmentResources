#!/usr/bin/env python

from http.server import SimpleHTTPRequestHandler, HTTPServer
import sys

class SoarWebServer(SimpleHTTPRequestHandler):

    def do_POST(self):
        self.wfile.write("Send your POST response here!")


def main():

    if len(sys.argv)<2:
        print("No Port Specified")
        doNotStart()

    try:
        port = int(sys.argv[1])
    except:
        print("Cannot create server on port " + str(sys.argv[1]))
        doNotStart()

    if (port<1024) or (port>49152):
        print("Please specify a port between 1024 and 49152 (8000 recommended)")
        doNotStart()

    print("Starting server on port " + str(port) + "...")

    server_address = ("", port)
    httpd = HTTPServer(server_address, SoarWebServer)
    httpd.serve_forever()


def doNotStart():
    print("Webserver will not start")
    exit()



if __name__ == "__main__":
    main()
