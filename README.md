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

Notes for this assignment:

* My Seup:
	* Macbook Pro 15''
	* Virtualbox 5.1.6
	* Ubuntu 16.04 LTS
	* Wireless USB Adapter (Alfa AWUS036NH 2000mW)
	* To make the Wireless USB Adapter available to Virtualbox, just plug it in and on the top bar, selecet "Devices" -> "USB" and check the WLAN entry for the adapter (i.e. Ralink 802.11 n WLAN)
	* Checking in Ubuntu if the Wireless USB Adapter is working:
	'''
	sudo lshw -C network
  *-network               
       description: Ethernet interface
       product: 82540EM Gigabit Ethernet Controller
       vendor: Intel Corporation
       physical id: 3
       bus info: pci@0000:00:03.0
       logical name: enp0s3
       version: 02
       serial: 08:00:27:59:8a:48
       size: 1Gbit/s
       capacity: 1Gbit/s
       width: 32 bits
       clock: 66MHz
       capabilities: pm pcix bus_master cap_list ethernet physical tp 10bt 10bt-fd 100bt 100bt-fd 1000bt-fd autonegotiation
       configuration: autonegotiation=on broadcast=yes driver=e1000 driverversion=7.3.21-k8-NAPI duplex=full ip=10.0.2.15 latency=64 link=yes mingnt=255 multicast=yes port=twisted pair speed=1Gbit/s
       resources: irq:19 memory:f0000000-f001ffff ioport:d010(size=8)
  *-network
       description: Wireless interface
       physical id: 1
       bus info: usb@1:2
       logical name: wlx00c0ca5a50a5
       serial: 00:c0:ca:5a:50:a5
       capabilities: ethernet physical wireless
       configuration: broadcast=yes driver=rt2800usb driverversion=4.8.0-36-generic firmware=0.29 link=no multicast=yes wireless=IEEE 802.11
    '''	

