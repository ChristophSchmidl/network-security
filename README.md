# Network Security

![alt tag](https://imgs.xkcd.com/comics/network.png)

This repository contains all assignments for the course "Network Security" (NWI-IBC022) given at the Radboud University.

## Assignment 1 - Network Sniffer (Ethernet, IP, TCP, UDP, ICMP, ARP)

Topics covered:

* Sockets
* conversion of c types to python types (see struct.unpack()) 
* Bit shift
* Structure of Ethernet, IP, TCP, UDP, ICMP, ARP
* Conversion of endianness (see socket.htons())

Useful tutorial regarding assignment 1: https://www.youtube.com/playlist?list=PL6gx4Cwl9DGDdduy0IPDDHYnUx66Vc4ed


## Assignment 2 - Wireless Network Cracking (aircrack-ng, wireshark, arpspoof)

Topics covered:

* Usage of the following tools: aircrack-ng, wireshark, dsniff
* Switching wifi card into monitor-mode and capturing traffic
* Cracking WEP
* Working with capture files (*.cap) and Wireshark
* Apply ARP spoofing to redirect traffic to your own machine
* ARP replay and disassociation

## Assignment 3 - Network Scanning

Topics covered:

* Usage of the following tools: nmap
* IP spoofing
* SYN flooding
* Port blocking
* Port scanning
* OS fingerprinting
* Host discovery
* Service and version detection

## Assignment 4 - Firewalls (iptables), VPN

Topics covered:

* Usage of the following tools: iptables, sshuttle, openvpn
* Restricting network traffic using iptables
* iptables chains like: PREROUTING, INPUT, OUTPUT, POSTROUTING
* Tunneling traffic through sshuttle
* TUN and TAP devices
* the route command
* DHCP leases
* NAT and ICMP
* ICMP related attacks

## Assignment 5 - DNS

Topics covered:

* Usage of the following tools: bind, dig, drill
* DNS amplification
* Authoritive and recursive DNS servers
* DNS records
* Preventing DNS attacks using iptables
* DNS cache poisoning
* Kaminskys DNS Bug
* QID- , port-, 0x20 randomization
* bailiwick test

## Assignment 6 - Combination of previous assignments

Topics covered:

* Usage of the following tools: aircrack-ng, arpspoof, nmap, sslstrip, openvpn, wireshark
* Cracking WPA2 networks using aircrack-ng and wordlists
* Discovering hosts on the networks using nmap
* ARP spoofing
* Using sslstrip in combination with arp spoofing
* Setting up OpenVPN
* Using traceroute, route to check if traffic is tunneled through openvpn


