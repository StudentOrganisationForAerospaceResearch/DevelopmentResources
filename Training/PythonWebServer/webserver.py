#!/usr/bin/env python3

import http.server
import socketserver
import sys

Handler = http.server.SimpleHTTPRequestHandler


def main():
	if len(sys.argv) != 2:
		print("Please specify one argument for the port")
		return 1

	# with socketserver.TCPServer(("", PORT), Handler) as httpd:
	#     print("serving at port", PORT)
	#     httpd.serve_forever()

if __name__ == "__main__":
    main()