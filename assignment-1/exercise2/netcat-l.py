#!/usr/bin/env python3

'''
    UDP Version of Server
    
    UDP is a connectionless and non-stream oriented protocol. 
    It means a UDP server just catches incoming packets from 
    any and many hosts without establishing a reliable pipe 
    kind of connection
'''

import socket

def handlestring(datastring, length, delimiter):
    stringlist = datastring.split(sep=delimiter)
    filteredlist = []

    for string in stringlist:
        filteredlist.append(string[length:])
    filteredstring = delimiter.join(filteredlist)
    return filteredstring


def main():
    # The SOCK_DGRAM specifies datagram (udp) sockets.
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    # Since udp sockets are non connected sockets,
    # communication is done using the socket functions
    # sendto and recvfrom.

    for i in range(0, 3):
        # 65507 bytes seem to be the maximum size of a udp package
        data, clientaddress = s.recvfrom(65507)
        print(handlestring(data.decode("utf-8"), len("spam "), "\n"))
    s.close()


if __name__ == "__main__":
    host = "localhost"
    port = 42424
    backlog = 5  # number of concurrent connections
    size = 1024  # receive a maximum of 1024 bytes of data
    main()












