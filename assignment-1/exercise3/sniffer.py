#!/usr/bin/env python3

'''
    Note for myself: continue at 3d
'''

import socket
import struct


def parse_udp(packet):
    header_length = 8
    header = packet[:header_length]
    data = packet[header_length:]

    (source_port, dest_port,
     data_length, checksum) = struct.unpack("!HHHH", header)

    return source_port, dest_port, data_length, checksum, data


def parse_ip(packet):
    header_length_in_bytes = (packet[0] & 0x0F) * 4
    header = packet[:header_length_in_bytes]
    data = packet[header_length_in_bytes:]
    return header_length_in_bytes, header, data


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

    while True:
        packet = s.recvfrom(65565)
        header_length_in_bytes, header, data = parse_ip(str(packet).encode("utf-8"))

        source_port, dest_port, data_length, checksum, data = parse_udp(data)

        print("Source Port: {}\nDestination Port: {}\n"
        "Data length: {}\nChecksum: {}\nSize of Data: {}\nData: {}\n".format(
        source_port, dest_port, data_length, checksum, len(data), data))




if __name__ == "__main__":
    host = "localhost"
    main()