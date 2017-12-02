#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys, psutil, time

class SoarWebServer(BaseHTTPRequestHandler):
    def setHeaders(self, MIME_Type): #TODO make this thing work
        self.send_response(200)
        self.send_header("Content-Type", MIME_Type)
        self.end_headers()
        
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("\nSend your POST response here!", "utf-8"))
        
    def do_GET(self):
        #setHeaders(self, "text/html")
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        
        #self.wfile.write(bytes("<!doctype html><body><p>This is a test.</p></body></html>", "utf-8"))
        myIndex = open("index.html") #TODO wrap this in exception handling
        self.wfile.write(bytes( myIndex.read(), "utf-8" ))
        myIndex.close();

    
def main():
    if (len(sys.argv) == 1):
        print("Enter the port number! eg \"webserver.py 80\"")
        return
    port = int(sys.argv[1])
    if (port < 0 or port > 59151): #I honestly have NO CLUE what restrictions to put on the port number
        print("The port entered is invalid!")
        return
    
    psutil.cpu_percent() #call this once to warm it up (returns zero first time)
    print("Starting server on port " + str(port) + "...")
    sys.stdout.flush() #I seem to need this for it to print
    server_address = ("", port)
    httpd = HTTPServer(server_address, SoarWebServer)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
