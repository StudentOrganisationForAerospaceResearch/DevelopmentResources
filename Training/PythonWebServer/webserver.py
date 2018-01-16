#!/usr/bin/env python

from http.server import SimpleHTTPRequestHandler, HTTPServer
import sys
import psutil
from datetime import datetime
import pytz

class SoarWebServer(SimpleHTTPRequestHandler):

    def do_POST(self):
        #Send your POST response here!
        s0 = str(datetime.now(tz=pytz.timezone('America/Edmonton')).strftime('%H:%M:%S'));
        s1 = str(psutil.cpu_count());
        s2 = str(psutil.cpu_percent(interval=1));
       	s3 = str(round(psutil.virtual_memory().total/(2**30), 2));
        s4 = str(round(psutil.virtual_memory().used/(2**30), 2));

        self.wfile.write(bytes(s0, "utf-8"));
        self.wfile.write(bytes(s1, "utf-8"));
        self.wfile.write(bytes(s2, "utf-8"));
        if(len(s2)==3):
        	self.wfile.write(bytes(" ", "utf-8"));
        if(len(s2)==2):
        	self.wfile.write(bytes("  ", "utf-8"));
        self.wfile.write(bytes(s3, "utf-8"));
        if(len(s4)==3):
        	self.wfile.write(bytes("  ", "utf-8"));
        if(len(s3)==4):
        	self.wfile.write(bytes(" ", "utf-8"));
        self.wfile.write(bytes(s4, "utf-8"));
        if(len(s4)==3):
        	self.wfile.write(bytes("  ", "utf-8"));
        if(len(s4)==4):
        	self.wfile.write(bytes(" ", "utf-8"));


def main():
    port = int(sys.argv[1]) # Error check this!

    server_address = ("", port)
    httpd = HTTPServer(server_address, SoarWebServer)
    httpd.serve_forever()

if __name__ == "__main__":
    main()