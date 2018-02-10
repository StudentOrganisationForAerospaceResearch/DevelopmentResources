#!/usr/bin/env python

from http.server import SimpleHTTPRequestHandler, HTTPServer
import sys
import psutil
from datetime import datetime
import pytz
import json

class SoarWebServer(SimpleHTTPRequestHandler):

    def do_POST(self):
        #Send your POST response here!

        time = datetime.now(tz=pytz.timezone('America/Edmonton')).strftime('%H:%M:%S');
        cpu_count = str(psutil.cpu_count()).ljust(2);
        cpu_percent = str(psutil.cpu_percent(interval=1)).ljust(5);
       	virtual_memory_total= str(round(psutil.virtual_memory().total/(2**30), 2)).ljust(5);
        virtual_memory_used = str(round(psutil.virtual_memory().used/(2**30), 2)).ljust(4);

        pythonData = {  
	        "Time": time,
	        "Total CPUs": cpu_count,
	        "CPU Usage": cpu_percent,
	        "Total RAM": virtual_memory_total,
	        "Used RAM": virtual_memory_used
        }
        json_string = json.dumps(pythonData)
        self.wfile.write(bytes(json_string, "utf-8"));

def main():
    port = int(sys.argv[1]) # Error check this!

    server_address = ("", port)
    httpd = HTTPServer(server_address, SoarWebServer)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
