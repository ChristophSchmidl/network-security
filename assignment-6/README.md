# Network Security - Assignment 6

In this assignment you will be using the following tools:

* aircrack-ng http://www.aircrack-ng.org/
* arpspoof http://www.monkey.org/~dugsong/dsniff/
* nmap http://nmap.org/
* sslstrip http://www.thoughtcrime.org/software/sslstrip/, https://pypi.python.org/pypi/sslstrip/0.9.2
* openvpn https://openvpn.net/index.php/open-source/documentation.html
* wireshark, tshark or tcpdump for packet capturing https://www.wireshark.org/
* optinally virtualbox https://www.virtualbox.org/

1. Create a folder called **exercise1**. This exercise is a multi-stage attack. Somewhere, there's a website containing your grades for this exercise. Everybody starts out with an O. It is up to you to give yourself the grade you want. You are not allowed to sniff the general network traffic in order to eavesdrop on other groups performing the attack. Also, please do not change other people's grades while performing this exercise, and don't do anything else on the target website.

	* a) Although WPA2 is more secure than WEP, just like any other good cryptographic system it is only as strong as the key material in use. To demonstrate this, you will use aircrack-ng to crack the passphrase of the wireless network where the course administrator is working. We have already take care of capturing the WPA2 connection handshakes, you can download it as http://www.cs.ru.nl/~paubel/netsec/2017/handshake.cap. To crack WPA2 passphrases, you need wordlists. A tutorial on how to crack WPA is on http://www.aircrack-ng.org/doku.php?id=cracking_wpa. Ignore the stuff about injecting packets, capturing the handshake etc. We'va already taken care of that. The interesting part is section 4. Pointers on where to find wordlists are on http://www.aircrack-ng.org/doku.php?id=faq#how_can_i_crack_a_wpa-psk_network. Since it is not our intention to have you spend hours on WPA cracking, use the wordlist at http://gdataonline.com/downloads/GDict/GDict_v2.0.7z. Note that you have to unzip it first (7z x GDict_v2.0.7z). The bssid of the network is **00:0f:c9:0c:f7:93**. If you want to decrypt the capture to see whether you have the correct key, you also need the essid. This is **netsec-wpa**. The capture should contain a single DHCP packet. Beware of the Ubuntu decryption bug, however: if you see other stuff you may still have the correct key. The best way to check is to try to connect to the network. Keep in mind that the network may not have a running DHCP server so if you fail to connect, try to set a static IP address in the 192.168.84.200 - 249 range, with netmask 255.255.255.0 and gateway 192.168.84.1. Write the passphrase you found to a file called **exercise1a**.

		* ```
			cs@cs-VirtualBox:~$ aircrack-ng -w GDict_v2.txt -b 00:0f:c9:0c:f7:93 handshake.cap
			Opening handshake.cap
			Reading packets, please wait...

			                                 Aircrack-ng 1.2 beta3


			                   [00:00:02] 10548 keys tested (4155.81 k/s)


			                           KEY FOUND! [ <OC@(OL4 ]


			      Master Key     : A2 3E 89 CC EF EC 87 9A BF AC 4D 39 C2 80 31 C4 
			                       BA 90 75 29 06 E4 D3 C7 19 C5 BD A1 32 8A 42 FE 

			      Transient Key  : A3 CA 24 30 C0 54 2D 08 02 F9 CA 20 A7 DB 67 62 
			                       22 3F B3 03 C1 EA FC 95 FE 10 C3 EB D2 EF 13 E9 
			                       AA C4 FD 70 A1 29 D8 68 4C 04 FD 40 4B 47 B1 22 
			                       3C C6 DB A8 98 CD 18 D5 8C D1 F3 76 64 39 DB 61 

			      EAPOL HMAC     : 9F 32 CA 85 04 F8 71 A1 B6 FA D2 87 FF 68 B1 69

			cs@cs-VirtualBox:~$ airdecap-ng -e 'netsec-wpa' -p '<OC@(OL4' handshake.cap
			
				Total number of packets read            99
				Total number of WEP data packets         0
				Total number of WPA data packets         5
				Number of plaintext data packets         0
				Number of decrypted WEP  packets         0
				Number of corrupted WEP  packets         0
				Number of decrypted WPA  packets         1 

		* WPA2 passphrase: <OC@(OL4	  
		

	* b) Connect to the network. There should be a DHCP server running. If not, use an IP address in the range of 192.168.84.200 - 249, with a netmask 255.255.255.0 and gateway 192.168.84.10. Use nmap to scan this network. Find the hosts in the range 192.168.84.1 - 80. Disable reverse DNS lookup to speed up things. There should be many hosts, apart from the gateways (192.168.84.1 - 20). Write which hosts you find to **exercise1b**.
	
		* ``` nmap -sP 192.168.84.1/24 ```
		* See: https://security.stackexchange.com/questions/36198/how-to-find-live-hosts-on-my-network
		* TODO: discover actual hosts

	* c) From this point onwards you will need to coordinate with other groups, since there is only a limited number of hosts to arpspoof. Do not get in each others way. Pick one of the hosts that are not the gateways (192.168.84.1 - 20). Its gateway is matched modulo 20 (so 192.168.84.32 and 192.168.84.52 both have gateway 192.168.84.12, whereas 192.168.84.23 has gateway 192.168.84.3). Using arpspoofing and wireshark, figure out which websites this host is contacting. Save the network capture in **exercise1c.cap**. Write the URLs to **exercise1c**. Note that you may need to also arpspoof its gateway. NOTE: There is some delay between requests in order to not abuse the target website. This delay is approximately 300 seconds as of this writing.
	
		* Answer

	* d) Now, use sslstrip (http://www.thoughtcrime.org/software/sslstrip/) to strip out SSL from its web traffic. The documentation and explanation on the websites should be enough to get it to work. Look at the traffic in wireshark and figure out the login credentials to use. Save the network capture in **exercise1d.cap** and write the login credentials you found to **exercise1d.creds**.

		* Answer

	* e) Finally, log in to the website, find your grades, and edit them to your desired result. After that, write your student numbers and the result you set to **exercise1e**.
	
		* Answer


2. Create a folder called **exercise2**. This exercise is intended to teach you the basic use of OpenVPN. There is an abundance of documentation on the internet. A lot of good documentation is on the project's website, https://openvpn.net/index.php/open-source/documentation.html

	* a) CNCZ provides an OpenVPN-based Science VPN. Instruction for this are at http://wiki.science.ru.nl/cncz/index.php?title=Vpn&setlang=en#OpenVPN_.5Bvoor.5D.5Bfor.5D_Linux_.26_MacOS. See if you can get this to work with your Science account. Look up in the OpenVPN man page (man openvpn) what each line of the configuration file means. For easy searching, append "--" to the first word on the line. So searching for "dev" becomes "--dev". Perform traceroutes (traceroute) to blackboard.ru.nl, www.google.com, www.cs.ru.nl, and to the VPN server itself, with and without the VPN running. Paste the commands you used and their output in a file called **exercise2a**. Look at the routing table (ip route show), and paste it as well. Explain the differences between traceroutes, paying special attention to the one to the VPN itself. In particular, explain why it is not straightforward to run other services on the OpenVPN server and contact them via the VPN tunnel. Can you thing of a solution for this problem?

		* openvpn-science.ovpn
		* ```
			client  # Indicating that we are using the client mode and not the server mode.
			proto tcp  # We want to communicate with the remote host through tcp.
			dev tun  # Telling which device type we want to use. tun (OSI layer 3) or tan (OSI layer 2).
			ca /etc/ssl/certs/DigiCert_Assured_ID_Root_CA.pem  # Path to the Certificate authority (CA) file.
			remote-cert-tls server  # This is a useful security option for clients, to ensure that the host they connect to is a designated server. The --remote-cert-tls server option is equivalent to --remote-cert-ku a0 88 --remote-cert-eku "TLS Web Server Authentication".
			auth-user-pass  # Tells the client that he needs username/password to authenticate at the server.
			cipher AES-256-CBC  # Encryption/Decryption of IP packets by using the AES-256-CBC cipher.
			verify-x509-name openvpn.science.ru.nl name  # Enforcing a stricter certificate check. For client configurations you can add this parameter where you provide for example the certificate subject of the server. This will ensure that only a server who identifies itself as a particular server will be accepted. 
			auth SHA256  # Authenticate packets with HMAC using message digest algorithm SHA256
			comp-lzo  # Using LZO compression to speed things up.
			verb 3  # Verbose model level 3 for logging purposes.
			remote openvpn.science.ru.nl 443  # The OpenVPN client will try to connect to the server openvpn.science.ru.nl at port 443 (HTTPS (Hypertext Transfer Protocol over SSL/TLS))
		* Traceroute with OpenVPN
		* ```
			cs@cs-VirtualBox:~$ sudo traceroute -I blackboard.ru.nl
			traceroute to blackboard.ru.nl (131.174.57.69), 30 hops max, 60 byte packets
			 1  openvpn-gw.science.ru.nl (131.174.224.129)  27.148 ms  53.599 ms  53.614 ms
			 2  dr-huyg.net.science.ru.nl (131.174.16.129)  53.618 ms  53.622 ms  53.647 ms
			 3  * * *
			 4  192.168.23.25 (192.168.23.25)  53.621 ms  53.609 ms  53.598 ms
			 5  192.168.23.67 (192.168.23.67)  53.622 ms  81.682 ms  81.688 ms
			 6  blackboard.ru.nl (131.174.57.69)  81.582 ms  63.915 ms  80.421 ms

			cs@cs-VirtualBox:~$ sudo traceroute -I google.com
			traceroute to google.com (172.217.16.174), 30 hops max, 60 byte packets
			 1  openvpn-gw.science.ru.nl (131.174.224.129)  27.232 ms  57.587 ms  57.604 ms
			 2  dr-huyg.net.science.ru.nl (131.174.16.129)  57.610 ms  57.615 ms  57.621 ms
			 3  * * *
			 4  192.168.23.25 (192.168.23.25)  57.656 ms  57.636 ms  57.626 ms
			 5  192.168.23.17 (192.168.23.17)  57.608 ms  57.613 ms  57.651 ms
			 6  AE8.1117.JNR01.Asd001A.surf.net (145.145.8.81)  84.478 ms  70.350 ms  59.307 ms
			 7  google-router1.peering.surf.net (145.145.166.82)  59.273 ms  43.180 ms  43.126 ms
			 8  108.170.241.226 (108.170.241.226)  43.110 ms  43.115 ms  43.113 ms
			 9  209.85.240.225 (209.85.240.225)  43.086 ms  43.101 ms  66.114 ms
			10  108.170.234.11 (108.170.234.11)  66.115 ms  90.299 ms  90.841 ms
			11  108.170.235.144 (108.170.235.144)  87.194 ms  87.196 ms  87.194 ms
			12  216.239.47.53 (216.239.47.53)  87.140 ms  87.132 ms  87.131 ms
			13  216.239.63.255 (216.239.63.255)  87.138 ms  87.155 ms  87.165 ms
			14  fra15s11-in-f14.1e100.net (172.217.16.174)  90.338 ms  90.284 ms  82.759 ms 

			cs@cs-VirtualBox:~$ sudo traceroute -I cs.ru.nl
			traceroute to cs.ru.nl (131.174.8.6), 30 hops max, 60 byte packets
			 1  openvpn-gw.science.ru.nl (131.174.224.129)  27.524 ms  29.774 ms  29.806 ms
			 2  dr-huyg.net.science.ru.nl (131.174.16.129)  29.870 ms  29.875 ms  56.527 ms
			 3  cs.ru.nl (131.174.8.6)  29.806 ms  29.813 ms  29.819 ms

			cs@cs-VirtualBox:~$ sudo traceroute -I openvpn.science.ru.nl
			traceroute to openvpn.science.ru.nl (131.174.16.141), 30 hops max, 60 byte packets
			 1  10.0.2.2 (10.0.2.2)  0.119 ms  0.095 ms  0.071 ms
			 2  * * *
			 3  * * *
			 4  * * *
			 5  * * *
			 6  * * *
			 7  * * *
			 8  * * *
			 9  * * *
			10  * * *
			11  * * *
			12  openvpn.science.ru.nl (131.174.16.141)  26.977 ms  26.918 ms  25.671 ms 

		* Traceroute without OpenVPN
		* ```
			cs@cs-VirtualBox:~$ sudo traceroute -I blackboard.ru.nl
			traceroute to blackboard.ru.nl (131.174.57.69), 30 hops max, 60 byte packets
			 1  10.0.2.2 (10.0.2.2)  0.563 ms  0.515 ms  0.494 ms
			 2  * * *
			 3  62.155.244.66 (62.155.244.66)  13.500 ms  13.487 ms  13.539 ms
			 4  217.239.48.138 (217.239.48.138)  20.964 ms  20.953 ms  20.929 ms
			 5  80.157.204.62 (80.157.204.62)  26.177 ms  26.149 ms  26.220 ms
			 6  xe-4-0-2.cr0-ams2.ip4.gtt.net (141.136.108.253)  22.839 ms  23.400 ms  23.337 ms
			 7  surfnet-gw.ip4.gtt.net (77.67.76.34)  23.643 ms  21.990 ms  21.966 ms
			 8  ru-router.customer.surf.net (145.145.8.82)  25.384 ms  25.815 ms  25.806 ms

			cs@cs-VirtualBox:~$ sudo traceroute -I google.com
			traceroute to google.com (172.217.16.174), 30 hops max, 60 byte packets
			 1  10.0.2.2 (10.0.2.2)  0.103 ms  0.061 ms  0.033 ms
			 2  * * *
			 3  62.155.244.66 (62.155.244.66)  12.531 ms  12.561 ms  12.634 ms
			 4  f-ee7-i.F.DE.NET.DTAG.DE (62.156.131.90)  19.493 ms  19.465 ms  19.437 ms
			 5  72.14.196.17 (72.14.196.17)  20.748 ms  20.968 ms  20.928 ms
			 6  216.239.46.63 (216.239.46.63)  21.113 ms  21.294 ms  21.266 ms
			 7  64.233.175.171 (64.233.175.171)  18.657 ms  18.693 ms  18.656 ms
			 8  fra15s11-in-f14.1e100.net (172.217.16.174)  18.689 ms  19.359 ms  19.208 ms 

			cs@cs-VirtualBox:~$ sudo traceroute -I cs.ru.nl
			traceroute to cs.ru.nl (131.174.8.6), 30 hops max, 60 byte packets
			 1  10.0.2.2 (10.0.2.2)  1.245 ms  1.210 ms  1.190 ms
			 2  * * *
			 3  62.155.244.66 (62.155.244.66)  12.056 ms  12.144 ms  12.136 ms
			 4  f-ed5-i.F.DE.NET.DTAG.DE (217.5.95.58)  19.057 ms  19.088 ms  19.182 ms
			 5  80.157.204.62 (80.157.204.62)  19.165 ms  19.432 ms  19.430 ms
			 6  xe-4-0-2.cr0-ams2.ip4.gtt.net (141.136.108.253)  21.987 ms  21.994 ms  22.274 ms
			 7  surfnet-gw.ip4.gtt.net (77.67.76.34)  22.484 ms  22.284 ms  22.211 ms
			 8  ru-router.customer.surf.net (145.145.8.82)  25.654 ms  25.633 ms  25.770 ms
			 9  * * *
			10  * * *
			11  * * *
			12  cs.ru.nl (131.174.8.6)  25.827 ms  25.748 ms  25.704 ms 

			cs@cs-VirtualBox:~$ sudo traceroute -I openvpn.science.ru.nl
			traceroute to openvpn.science.ru.nl (131.174.16.141), 30 hops max, 60 byte packets
			 1  10.0.2.2 (10.0.2.2)  0.442 ms  0.423 ms  0.422 ms
			 2  * * *
			 3  62.155.244.66 (62.155.244.66)  12.145 ms  12.166 ms  12.311 ms
			 4  f-ed5-i.F.DE.NET.DTAG.DE (217.5.95.58)  19.327 ms  19.322 ms  19.303 ms
			 5  80.157.204.62 (80.157.204.62)  20.271 ms  20.266 ms  20.374 ms
			 6  xe-4-0-2.cr0-ams2.ip4.gtt.net (141.136.108.253)  22.581 ms  21.417 ms  21.373 ms
			 7  surfnet-gw.ip4.gtt.net (77.67.76.34)  21.433 ms  22.139 ms  22.117 ms
			 8  ru-router.customer.surf.net (145.145.8.82)  25.542 ms  24.874 ms  24.860 ms
			 9  * * *
			10  * * *
			11  * * *
			12  openvpn.science.ru.nl (131.174.16.141)  24.755 ms  25.045 ms  26.079 ms

		* ip route with OpenVPN
		* ```
			cs@cs-VirtualBox:~$ sudo ip route show
			0.0.0.0/1 via 131.174.224.129 dev tun0 
			default via 10.0.2.2 dev enp0s3  proto static  metric 100 
			default via 192.168.2.1 dev enp0s8  proto static  metric 101 
			10.0.2.0/24 dev enp0s3  proto kernel  scope link  src 10.0.2.15  metric 100 
			128.0.0.0/1 via 131.174.224.129 dev tun0 
			131.174.16.141 via 10.0.2.2 dev enp0s3 
			131.174.224.128/27 dev tun0  proto kernel  scope link  src 131.174.224.151 
			169.254.0.0/16 dev enp0s3  scope link  metric 1000 
			192.168.2.0/24 dev enp0s8  proto kernel  scope link  src 192.168.2.117  metric 100

		* ip route without OpenVPN
		* ```
			cs@cs-VirtualBox:~$ sudo ip route show
			default via 10.0.2.2 dev enp0s3  proto static  metric 100 
			default via 192.168.2.1 dev enp0s8  proto static  metric 101 
			10.0.2.0/24 dev enp0s3  proto kernel  scope link  src 10.0.2.15  metric 100 
			169.254.0.0/16 dev enp0s3  scope link  metric 1000 
			192.168.2.0/24 dev enp0s8  proto kernel  scope link  src 192.168.2.117  metric 100




	* b) Create a subfolder called **exercise2b** to hold your answers and configuration files. Using the OpenVPN documentation you must set up an OpenVPN network between two machines. These can be physical machines, e.g. yours and your lab partner's laptops, but you can also use virtual machines. Virtualbox and KVM/QEMU are decent options in this regard. Note that you may not be able to reach other's machines through eduroam, but a direct link using an ehternet cable or ad ad-hoc WiFi network usually works. Setting up a virtual machine with e.g. Ubuntu is covered in tutorials so we will not cover that here. The bootable USB iso image downloadable at https://www.cs.ru.nl/~paubel/netsec/2017/netsec-debian-usb-image-20170411.img.gz (with credentials root:root, sutdent:student) should also be directly bootable as a virtual machine disk. The minimum setup you should get working is a VPN with a static, pre-distributed key. You should use layer 3 tunneling (tun devices), not layer 2 (tap devices). Document the commands you use in a text file **commands**. Also include configuration files for both hosts, if applicable. Note that the client does not need to tunnel all its network traffic over the VPN, it only needs to be able to reach the other endpoint through the VPN. Also perform a set of short packet captures on both ends of the connection, while doing a ping from the VPN server to the VPN client and vice versa. The packetm captures on each end should be done on two interfaces: one capture on the tun-interface created for the VPN, and another capture on the network interface that is actually carrying the VPN-tunneled traffic ( either your normal network , or a virtual interface created by e.g. virtualbox). So there should be fours captures in total. Include these captures, and name them along the lines of **client-tun.cap** and **server-wlan0.cap**. Also include the commands and (partial) output of the ping command and other commands you used during the capture in the file **commands**.

		* Answer


	* c) Create a subfolder called **exercise2c** to hold your answers and configuration files. Using the OpenVPN documentation and the previous exercise's answers, try to set up the VPN so that the VPN client uses the VPN for all its network traffic. This is a fairly common usage scenario, to it is fairly well covered in the basic documentation. Document the commands in a text file **commands**. Include configuration files for both hosts. Perform the same kind of packet capture as in exercise 2b, however, this time the VPN client should ping some host on the internet (e.g. www.google.com) instead of the VPN server. You can use traceroute or mtr to figure out whether traffic is actually going through the VPN or whether it's taking the normal route to the internet. Include the commands and output of the ping and traceroute commands you used during the capture in the file **commands**. If you have network issues during the exercise, one thing to do would be to look at your routing table (ip r show; route -n) and see if you can figure out why traffic is or is not going through the VPN. Of course, send an e-mail or drop by Pol's office (M1.03.20) if you're stuck.

		* Answer

	