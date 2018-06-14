#!/usr/bin/python3

import os
import socket
import subprocess
import time
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer
from multiprocessing import Process

http_port = 80

class Responder(BaseHTTPRequestHandler):

    global _users
    # GET is for clients geting the predi
    def do_GET(self):

        paths = {
            '/start': self.start,
            '/update_dns': self.update,
            '/status': self.status 
        }

        # server_path = '/http://{}:{}/'.format(cfg['http_server']['host_name'],
        #                                cfg['http_server']['host_port'])
        
        # # self.path depends on local or external call. check for both
        # if len(self.path) > len(server_path):
        #     cmd = self.path[len(server_path):]
        
        # else:
        #     cmd = self.path[1:]
        
        cmd = self.path
        self.send_response(200)

        if cmd in paths:
            self.wfile.write(bytes("callback({{ {}:{} }});".format(cmd, paths[cmd]()), "utf-8"))
        else:
            self.wfile.write(bytes("callback(command {} not reckognized);".format(cmd), "utf-8"))

	# Here are the implementations of the different get functions

    def start(self):
        value = subprocess.Popen(["bash", "/vagrant/dns_files/dns_set_old.sh"])
        return value

    def update(self):
    	value = subprocess.Popen(["bash", "/vagrant/dns_files/dns_set_updated.sh"])

    def status(self):
        return 'http server up and running'

# def http_server():
#     hostName = 'dns_proxy_http'
#     hostPort = 8878

#     server = HTTPServer((hostName, hostPort), Responder())
#     print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
#     try:
#         running_server.serve_forever()
#     except KeyboardInterrupt:
#         pass

#     server.server_close()
#     print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))


def run(server_class=HTTPServer, handler_class=Responder, port=http_port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
	run()