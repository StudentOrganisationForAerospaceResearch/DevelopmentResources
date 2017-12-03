#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys, psutil, time

class SoarWebServer(BaseHTTPRequestHandler):
    def setHeaders(self, MIME_Type): #TODO make this thing work
        print("in setHeaders MIME:" + MIME_Type)
        print("setHeaders self:" + str(self))
        sys.stdout.flush()        
        self.send_response(200)
        self.send_header("Content-Type", MIME_Type)
        self.end_headers()
        
    def do_POST(self):
        #setHeaders("text/html")
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        message = "\nCurrent server date and time is " + time.strftime("%Y-%m-%dT%H:%M:%S") + "\n"
        message += "This server has " + str(psutil.cpu_count()) + " logical CPUs\n"
        message += "Server CPU usage is at " + str(psutil.cpu_percent()) + "%\n"
        usedMem = psutil.virtual_memory().used / 2**30
        totalMem = psutil.virtual_memory().total / 2**30
        message += "Server RAM usage is at " + "{:.2f}".format(usedMem) + "GB\n"
        message += "Server total RAM is " + "{:.2f}".format(totalMem) + "GB\n"
        self.wfile.write(bytes(message, "utf-8"))
        
    def do_GET(self):
    
        #in addition to being a stupid and unexpandable way of serving files, this is also non-portable. But it works!
        #it actually not too hard to use os.sep and better path managment, but...
        if self.path == "/":
            setHeaders(self, "text/html")
            file = open(".\\index.html") #TODO wrap this in exception handling
            self.wfile.write(bytes( file.read(), "utf-8" ))     
            file.close()
        elif self.path == "/resources/stylesheet.css":
            setHeaders(self, "text/css")
            file = open(".\\resources\\stylesheet.css") #TODO wrap this in exception handling
            self.wfile.write(bytes( file.read(), "utf-8" ))     
            file.close()
        elif self.path == "/resources/index.js":
            setHeaders(self, "application/javascript")
            file = open(".\\resources\\index.js") #TODO wrap this in exception handling
            self.wfile.write(bytes( file.read(), "utf-8" ))     
            file.close()
        

def setHeaders(self, MIME_Type):
    self.send_response(200)
    self.send_header("Content-Type", MIME_Type)
    self.end_headers()
    
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
