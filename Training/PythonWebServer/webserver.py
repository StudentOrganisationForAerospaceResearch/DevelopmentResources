#!/usr/bin/env python

import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer
from datetime import datetime
import json

import psutil


class SoarWebServer(SimpleHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        msg = json.dumps({
            'time': str(datetime.now())[11:19],
            'total_cpus': str(psutil.cpu_count()),
            'cpu_usage': str(psutil.cpu_percent(interval=1)),
            'total_ram': "{0:.2f}".format(
                psutil.virtual_memory().total / 1024 / 1024 / 1024),
            'used_ram': "{0:.2f}".format(
                psutil.virtual_memory().used / 1024 / 1024 / 1024)
        })
        self.wfile.write(msg.encode(encoding='utf-8'))


def main():
    if len(sys.argv) != 2:
        print("Please specify one argument for the port")
        return 1

    port = int(sys.argv[1])
    print('Starting server on port ' + str(port) + '...')

    server_address = ('', port)
    httpd = HTTPServer(server_address, SoarWebServer)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
