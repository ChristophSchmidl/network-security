#!/usr/bin/env python3

'''
    UDP Version of Client
'''

import socket

host = "localhost"
port = 42424

# s = socket.create_connection((host, port))
# create_connection is no longer needed because it is tcp specific

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

stringbuf = ""
for i in range(0, 1000):
    stringbuf = stringbuf + "spam " + str(i) + "\n"

buf = stringbuf.encode("utf-8")

s.sendto(buf, (host, port))

