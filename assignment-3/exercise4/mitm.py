#!/usr/bin/env python3

import socket
import struct


def get_ip_protocol_name(protocol_number):
    '''
        *** Important IP Protocol Numbers*** 

        1 = ICMP (Internet Control Message Protocol)
        2 = IGMP (Internet Group Management)
            IGMP is interesting because then the length of the IP header
            is 24 bytes long and not 20 bytes (using options and padding)
        4 = IPv4 (IPv4 encapsulation)
        6 = TCP (Transmission Control Protocol)
        17 = UDP (User Datagram Protocol)
        41 = IPv6 (IPv6 encapsulation)
        58 = IPv6-ICMP (ICMP for IPv6)
    '''
    if protocol_number == 1:
        return "ICMP"
    elif protocol_number == 2:
        return "IGMP"
    elif protocol_number == 4:
        return "IPv4"
    elif protocol_number == 6:
        return "TCP"
    elif protocol_number == 17:
        return "UDP"
    elif protocol_number == 41:
        return "IPv6"
    elif protocol_number == 58:
        return "IPv6-ICMP"


    return "Unknown"


def get_eth_protocol_name(bytes_representation):
    '''
        *** Important EtherTypes *** 

        0x0800 = Internet Protocol version v (IPv4) *
        0x0806 = Address Resolution Protocol (ARP) *
        0x8100 = VLAN-tagged frame (IEEE 802.1Q) and Shortest Path Bridging IEEE 802.1aq
        0x8137 = IPX (Good old StarCraft times)
        0x86DD = Internet Protocol Version 6 (IPv6) *
    '''
    if bytes_representation == b'\x08\x00':
        return "IPv4"
    elif bytes_representation == b'\x08\x06':
        return "ARP"
    elif bytes_representation == b'\x81\x00':
        return "IEEE 802.1Q"
    elif bytes_representation == b'\x81\x37':
        return "IPX"
    elif bytes_representation == b'\x86\xdd':
        return "IPv6"

    return "Unknown"


def get_mac_address(bytes_address):
    # return properly formatted MAC address (AA:BB:CC:DD:EE:FF)
    bytes_str = map("{:02X}".format, bytes_address)
    return ":".join(bytes_str)


def parse_udp(packet):
    header_length = 8
    header = packet[:header_length]
    data = packet[header_length:]

    (source_port, dest_port,
     data_length, checksum) = struct.unpack("!HHHH", header)

    return source_port, dest_port, data_length, checksum, data


def parse_tcp(packet):
    (source_port, destination_port, sequence,
     acknowledgement, offset_reserved_flags) = struct.unpack("!HHLLH", packet[:14])

    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1

    return source_port, destination_port, sequence, acknowledgement, flag_urg, flag_ack, \
           flag_psh, flag_rst, flag_syn, flag_fin, packet[offset:]


def parse_icmp(packet):
    header_length = 4
    header = packet[:header_length]
    data = packet[header_length:]

    icmp_type, code, checksum = struct.unpack("!BBH", header)

    return icmp_type, code, checksum, data


def parse_arp(packet):
    '''
    struct arp_header {
        unsigned short hardware_type; (H = 2byte)
        unsigned short protocol_type; (H = 2byte)
        unsigned char hardware_len; (B = 1byte)
        unsigned char protocol_len; (B = 1byte)
        unsigned short opcode; (H = 2byte)
        unsigned char sender_mac[MAC_LENGTH]; (6s = 6byte)
        unsigned char sender_ip[IPV4_LENGTH]; (4s = 4byte)
        unsigned char target_mac[MAC_LENGTH]; (6s = 6byte)
        unsigned char target_ip[IPV4_LENGTH]; (4s = 4byte)
    }; 
    '''

    header_length = 28
    header = packet[:header_length]
    # there is no payload or data, the data just seems to be the addresses

    (hardware_type, protocol_type, hardware_length,
     protocol_length, operation, sender_mac_address,
     sender_protocol_address, target_mac_address,
     target_protocol_address) = struct.unpack("!HHBBH6s4s6s4s", header)

    # This field specifies the internetwork protocol for which the ARP request is intended.
    # For IPv4, this has the value 0x0800.
    protocol_type = header[2:4]

    return hardware_type, protocol_type, hardware_length, protocol_length, \
           operation, get_mac_address(sender_mac_address), socket.inet_ntoa(sender_protocol_address), \
           get_mac_address(target_mac_address), socket.inet_ntoa(target_protocol_address)


def parse_ip(packet):
    ''' unpack header into:
        |_ B(Version+IHL)|B(TOS)|H(TotalLength)|H(ID)
        |_ H(Flags+FragmentOffset)|B(TTL)|B(Protocol)|H(CheckSum)
        |_ 4s(Source)|4s(Destination)
        
        H = unsigned short (C Type), integer (Python type), 2 bytes (Standard size)
        B = unsigned char (C Type), integer (Python type), 1 byte (Standard size)
        s = char[] (C Type), string (Python type), char = 1 byte (Standard size)
    '''

    version = packet[0] >> 4
    header_length_in_bytes = (packet[0] & 0x0F) * 4
    header = packet[:header_length_in_bytes]

    unpacked_ip_header = None

    if header_length_in_bytes == 20:
        unpacked_ip_header = struct.unpack('!BBHHHBBH4s4s', header)
    elif header_length_in_bytes == 24:
        # This means that the Header also contains options + padding
        print("*** Uncommon IP Header Length detected ***")
        unpacked_ip_header = struct.unpack('!BBHHHBBH4s4s4s', header)

    total_length = unpacked_ip_header[2]
    ttl = unpacked_ip_header[5]
    protocol_number = unpacked_ip_header[6]
    protocol_name = get_ip_protocol_name(protocol_number)
    source_address = socket.inet_ntoa(unpacked_ip_header[8])
    destination_address = socket.inet_ntoa(unpacked_ip_header[9])

    data = packet[header_length_in_bytes:]

    return header_length_in_bytes, version, total_length, ttl, protocol_name, \
        protocol_number, source_address, destination_address, header, data


def parse_ethernet(data):
    ethernet_header_length = 14  # 14 bytes
    ethernet_header_binary = data[:ethernet_header_length]

    ethernet_header_unpacked = struct.unpack('!6s6sH', ethernet_header_binary)

    destination_mac_address = ethernet_header_unpacked[0]
    source_mac_address = ethernet_header_unpacked[1]
    raw_protocol = data[12:14]
    protocol_name = get_eth_protocol_name(raw_protocol)
    converted_protocol = socket.htons(ethernet_header_unpacked[2])

    # Check for 802.1Q tag
    if protocol_name == "IEEE 802.1Q":
        # See https://en.wikipedia.org/wiki/IEEE_802.1Q for a nice illustration
        ethernet_header_length = 18  # 14 bytes
        ethernet_header_binary = data[:ethernet_header_length]

        ethernet_header_unpacked = struct.unpack('!6s6s4sH', ethernet_header_binary)

        destination_mac_address = ethernet_header_unpacked[0]
        source_mac_address = ethernet_header_unpacked[1]
        raw_protocol = data[17:19]
        protocol_name = get_eth_protocol_name(raw_protocol)
        converted_protocol = socket.htons(ethernet_header_unpacked[2])

    return get_mac_address(destination_mac_address), get_mac_address(source_mac_address), \
        protocol_name, raw_protocol, converted_protocol, data[ethernet_header_length:]


def main():
    '''
        *** Welcome to the World of Endianness ***

        Endianess has to do with the order in which bytes are stored in memory.
        Many devices store numbers in little-endian format which means that the 
        least significant byte comes first. The socket library provides a 
        function named htons() which stands for host-to-network short. This means
        it works on 16-bit short integers, i.e. 2 bytes. This function swaps the 
        endianness of a short and makes sure the numbers are stored in memory in
        network byte order which is the most significant byte first/at the lowest
        address (big-endian).

        socket.ntohs(0x0003) = make it compatible with all machines and that
        the byte order is correct. Converting big- and little-endian
        in the correct way automatically
    '''

    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

    while True:
        # raw_data = bytes object representing the data received
        # address = address of the socket sending the data
        raw_data, address = s.recvfrom(65536)  # biggest possible buffer size

        eth_destination_address, eth_source_address, eth_protocol_name, \
            eth_protocol_raw, eth_protocol_converted, eth_payload = parse_ethernet(raw_data)

        print("\nEthernet Frame:")
        print("\t- Source: {}, Destination: {}, Protocol: {}, {}, {}".format(eth_source_address,
                                                                             eth_destination_address,
                                                                             eth_protocol_name,
                                                                             eth_protocol_converted,
                                                                             eth_protocol_raw))

        if eth_protocol_name == "IPv4":

            ip_header_length_in_bytes, ip_version, ip_total_length, ip_ttl, ip_protocol_name, ip_protocol_number, \
                ip_source_address, ip_destination_address, ip_header, ip_data = parse_ip(eth_payload)

            print("\t- IPv4 Packet:")
            print("\t\t- Version: {}, Header Length: {}, Total Length: {}, TTL: {}".format(ip_version,
                                                                                        ip_header_length_in_bytes,
                                                                                        ip_total_length,
                                                                                           ip_ttl))
            print("\t\t- Protocol Name: {}, Protocol Number: {}".format(ip_protocol_name, ip_protocol_number))
            print("\t\t- Source: {}, Destination: {}".format(ip_source_address, ip_destination_address))


            if ip_protocol_name == "ICMP":
                icmp_type, code, checksum, data = parse_icmp(ip_data)

                print("\t\t- ICMP Segment:")
                print("\t\t\t- ICMP Type: {}, ICMP Code: {}, Checksum: {}".format(icmp_type, code, checksum))
                print("\t\t\t- Data: {}".format(data))


            if ip_protocol_name == "UDP":
                source_port, dest_port, data_length, checksum, data = parse_udp(ip_data)

                print("\t\t- UDP Segment:")
                print("\t\t\t- Source Port: {}, Destination Port: {}".format(source_port, dest_port))
                print("\t\t\t- Payload Length: {}, Checksum: {}".format(data_length, checksum))
                print("\t\t\t- Data: {}".format(data))

            elif ip_protocol_name == "TCP":

                source_port, dest_port, sequence, acknowledgement, flag_urg, flag_ack, \
                flag_psh, flag_rst, flag_syn, flag_fin, data = parse_tcp(ip_data)

                print("\t\t- TCP Segment:")
                print("\t\t\t- Source Port: {}, Destination Port: {}".format(source_port, dest_port))
                print("\t\t\t- Sequence: {}, Acknowledgement: {}".format(sequence, acknowledgement))
                print("\t\t\t- Flags:\n\t\t\t- URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN: {}".format(
                    flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin))
                print("\t\t\t- Data: {}".format(data))

        elif eth_protocol_name == "ARP":

            hardware_type, protocol_type, hardware_length, protocol_length, \
            operation, sender_mac_address, sender_protocol_address, \
            target_mac_address, target_protocol_address = parse_arp(eth_payload)

            print("\t- ARP Packet:")
            print("\t\t- Hardware Type: {}, Protocol Type: {}".format(hardware_type, protocol_type))
            print("\t\t- Hardware Length: {}, Protocol Length: {}".format(hardware_length, protocol_length))
            print("\t\t- Operation: {}".format(operation))
            print("\t\t- Sender MAC Address: {}, Sender Protocol Address: {}".format(sender_mac_address,
                                                                                 sender_protocol_address))
            print("\t\t- Target MAC Address: {}, Target Protocol Address: {}".format(target_mac_address, target_protocol_address))

        elif eth_protocol_name == "IPX":
            print("*** For Aiur! ***")
        elif eth_protocol_name == "IPv6":
            pass
            # print("*** IPv6: not implemented ***")


if __name__ == "__main__":
    host = "localhost"
    main()
