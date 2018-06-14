#!/usr/bin/python3

import os
import socket
import subprocess
import time
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer
from multiprocessing import Process

http_port = 80
_status = 'initialized'
directory = "/home/ubuntu/"

class Responder(BaseHTTPRequestHandler):

    # GET is for clients geting the predi
    def do_GET(self):

        paths = {
            'start': self.start,
            'update_dns': self.update,
            'status': self.status,
            'stop': self.stop,
            'simple': self.simple,
            'set_dns': self.set_dns
        }
        
        cmds = self.path.split('/')
        cmd = self.path.split('/')[1]
        if len(cmds) > 2:
            args = cmds[2:]
        else:
            args = None
        self.send_response(200)

        if cmd in paths:            
            self.wfile.write(bytes("callback({{ {}:{} }});".format(cmd, paths[cmd](args)), "utf-8"))
        else:
            self.wfile.write(bytes("callback(command {} not reckognized);".format(cmd), "utf-8"))

	# Here are the implementations of the different GETs
    def start(self, args):
        global _status
        _status = 'proxy running, dns old'
        value = subprocess.Popen(["bash", directory + "dns_files/dns_set_old.sh"])
        return _status

    def update(self, args):
        global _status
        _status = 'proxy running,  dns updated'
        value = subprocess.Popen(["bash", directory + "dns_files/dns_set_updated.sh"])
        return _status

    def status(self, args):
        return _status

    def stop(self, args):
        global _status
        _status = 'proxy not running'
        value = subprocess.Popen(["bash", directory + "dns_files/dns_stop.sh"])
        return _status

    def simple(self, args):
        global _status
        _status = 'proxy running, all dns forwarded to 8.8.8.8'
        value = subprocess.Popen(["bash", directory + "dns_files/dns_set_google.sh"])
        return _status

    def set_dns(self, args):
        if len(args)<2:
            return 'set_dns needs 2 arguments, domain and ip'
        domain = args[0]
        ip = args[1]
        subprocess.Popen(["bash", directory + "dns_files/dns_set_spec.sh", domain, ip])
        global _status
        _status = 'dns running, {} points to {}'.format(domain, ip)
        return _status

def run(server_class=HTTPServer, handler_class=Responder, port=http_port):
    server_address = ('', port)
    handler_class.start(handler_class, None)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    while True:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('KeyboardInterrupt. Returning to simple dns proxy')
            handler_class.simple(handler_class, None)
            break

if __name__ == "__main__":
	run()
