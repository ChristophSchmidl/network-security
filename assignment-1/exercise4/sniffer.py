#!/usr/bin/env python3

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
    """ unpack header into:
        |_ B(Version+IHL)|B(TOS)|H(TotalLength)|H(ID)
        |_ H(Flags+FragmentOffset)|B(TTL)|B(Protocol)|H(CheckSum)
        |_ 4s(Source)|4s(Destination)
        
        H = unsigned short (C Type), integer (Python type), 2 bytes (Standard size)
        B = unsigned char (C Type), integer (Python type), 1 byte (Standard size)
        s = char[] (C Type), string (Python type), char = 1 byte (Standard size)
    """

    version = packet[0] >> 4
    header_length_in_bytes = (packet[0] & 0x0F) * 4
    header = packet[:header_length_in_bytes]

    unpacked_ip_header = struct.unpack('!BBHHHBBH4s4s', header)

    total_length = unpacked_ip_header[2]
    protocol = unpacked_ip_header[6]
    source_address = unpacked_ip_header[8]
    destination_address = unpacked_ip_header[9]

    data = packet[header_length_in_bytes:]

    return header_length_in_bytes, version, total_length, protocol, source_address, destination_address, header, data


def main():
    '''
        This sniffer only picks up UDP Packages, therefore the protocol number is always 17
        For a TCP sniffer use: s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        For a ICMP sniffer use: s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

    while True:
        # packet = bytes object representing the data received
        # address = address of the socket sending the data
        packet, address = s.recvfrom(65565)

        header_length_in_bytes, version, total_length, protocol, \
            source_address, destination_address, header, data = parse_ip(packet)

        print("*** IP Protocol Information ***\n")
        print("Version: {}".format(version))
        print("Header length: {}".format(header_length_in_bytes))
        print("Total Length: {}".format(total_length))
        print("Protocol: {}".format(protocol))
        print("Source Address: {}".format(socket.inet_ntoa(source_address)))
        print("Destination Address: {}".format(socket.inet_ntoa(destination_address)))

        source_port, dest_port, data_length, checksum, data = parse_udp(data)
        print("\n*** UDP Protocol Information ***\n")
        print("Source Port: {}\nDestination Port: {}\n"
        "Data length: {}\nChecksum: {}\nSize of Data: {}\nData: {}\n".format(
            source_port, dest_port, data_length, checksum, len(data), data))


if __name__ == "__main__":
    host = "localhost"
    main()
