#!/usr/bin/env python

from http.server import SimpleHTTPRequestHandler, HTTPServer
import sys
import time
import psutil

class SoarWebServer(SimpleHTTPRequestHandler):

    def do_POST(self):
        self.wfile.write("Send your POST response here!")

def main():
    localTime = time.strftime("%H:%M:%S")
    cpuCount = psutil.cpu_count()
    cpuPercentage = psutil.cpu_percent(interval = 1)
    ram = psutil.virtual_memory()
    totalRam = ram[0]
    totalRam = totalRam / 1e9
    totalRam = round(totalRam, 2)
    usedRam = ram[3]
    usedRam = usedRam/1e9
    usedRam = round(usedRam, 2)

    try:
        port = int(sys.argv[1])
    except Exception as e:
        print("Failed to Connect: Exception", e)
        sys.exit()

    print("Starting server on port " + str(port) + "...")

    server_address = ("", port)
    httpd = HTTPServer(server_address, SoarWebServer)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
