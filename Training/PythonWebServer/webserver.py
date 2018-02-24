#!/usr/bin/env python

import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer
import psutil
import datetime
import json

class SoarWebServer(SimpleHTTPRequestHandler):

    def do_POST(self):
        cpu_count = str(psutil.cpu_count())
        cpu_percent = str(psutil.cpu_percent())
        total_ram = str(psutil.virtual_memory().total)
        avail_ram = str(psutil.virtual_memory().available)
        current_time = str(datetime.datetime.now().time())
        
        ServerData = {
            "cpuCount":  cpu_count,
            "cpuPercent": cpu_percent,
            "totalRAM": total_ram,
            "availRAM": avail_ram,
            "currentTime": current_time
		}
        self.wfile.write(json.dumps(ServerData))


def main():
    port = int(sys.argv[1]) # Error check this!
    print("Starting server on port " + str(port) + "...")

    server_address = ("", port)
    httpd = HTTPServer(server_address, SoarWebServer)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
