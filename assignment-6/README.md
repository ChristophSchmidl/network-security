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

		* Answer

	* b) Connect to the network. There should be a DHCP server running. If not, use an IP address in the range of 192.168.84.200 - 249, with a netmask 255.255.255.0 and gateway 192.168.84.10. Use nmap to scan this network. Find the hosts in the range 192.168.84.1 - 80. Disable reverse DNS lookup to speed up things. There should be many hosts, apart from the gateways (192.168.84.1 - 20). Write which hosts you find to **exercise1b**.
	
		* Answer

	* c) From this point onwards you will need to coordinate with other groups, since there is only a limited number of hosts to arpspoof. Do not get in each others way. Pick one of the hosts that are not the gateways (192.168.84.1 - 20). Its gateway is matched modulo 20 (so 192.168.84.32 and 192.168.84.52 both have gateway 192.168.84.12, whereas 192.168.84.23 has gateway 192.168.84.3). Using arpspoofing and wireshark, figure out which websites this host is contacting. Save the network capture in **exercise1c.cap**. Write the URLs to **exercise1c**. Note that you may need to also arpspoof its gateway. NOTE: There is some delay between requests in order to not abuse the target website. This delay is approximately 300 seconds as of this writing.
	
		* Answer

	* d) Now, use sslstrip (http://www.thoughtcrime.org/software/sslstrip/) to strip out SSL from its web traffic. The documentation and explanation on the websites should be enough to get it to work. Look at the traffic in wireshark and figure out the login credentials to use. Save the network capture in **exercise1d.cap** and write the login credentials you found to **exercise1d.creds**.

		* Answer

	* e) Finally, log in to the website, find your grades, and edit them to your desired result. After that, write your student numbers and the result you set to **exercise1e**.
	
		* Answer


2. Create a folder called **exercise2**. This exercise is intended to teach you the basic use of OpenVPN. There is an abundance of documentation on the internet. A lot of good documentation is on the project's website, https://openvpn.net/index.php/open-source/documentation.html

	* a) CNCZ provides an OpenVPN-based Science VPN. Instruction for this are at http://wiki.science.ru.nl/cncz/index.php?title=Vpn&setlang=en#OpenVPN_.5Bvoor.5D.5Bfor.5D_Linux_.26_MacOS. See if you can get this to work with your Science account. Look up in the OpenVPN man page (man openvpn) what each line of the configuration file means. For easy searching, append "--" to the first word on the line. So searching for "dev" becomes "--dev". Perform traceroutes (traceroute) to blackboard.ru.nl, www.google.com, www.cs.ru.nl, and to the VPN server itself, with and without the VPN running. Paste the commands you used and their output in a file called **exercise2a**. Look at the routing table (ip route show), and paste it as well. Explain the differences between traceroutes, paying special attention to the one to the VPN itself. In particular, explain why it is not straightforward to run other services on the OpenVPN server and contact them via the VPN tunnel. Can you thing of a solution for this problem?

		* Answer


	* b) Create a subfolder called **exercise2b** to hold your answers and configuration files. Using the OpenVPN documentation you must set up an OpenVPN network between two machines. These can be physical machines, e.g. yours and your lab partner's laptops, but you can also use virtual machines. Virtualbox and KVM/QEMU are decent options in this regard. Note that you may not be able to reach other's machines through eduroam, but a direct link using an ehternet cable or ad ad-hoc WiFi network usually works. Setting up a virtual machine with e.g. Ubuntu is covered in tutorials so we will not cover that here. The bootable USB iso image downloadable at https://www.cs.ru.nl/~paubel/netsec/2017/netsec-debian-usb-image-20170411.img.gz (with credentials root:root, sutdent:student) should also be directly bootable as a virtual machine disk. The minimum setup you should get working is a VPN with a static, pre-distributed key. You should use layer 3 tunneling (tun devices), not layer 2 (tap devices). Document the commands you use in a text file **commands**. Also include configuration files for both hosts, if applicable. Note that the client does not need to tunnel all its network traffic over the VPN, it only needs to be able to reach the other endpoint through the VPN. Also perform a set of short packet captures on both ends of the connection, while doing a ping from the VPN server to the VPN client and vice versa. The packetm captures on each end should be done on two interfaces: one capture on the tun-interface created for the VPN, and another capture on the network interface that is actually carrying the VPN-tunneled traffic ( either your normal network , or a virtual interface created by e.g. virtualbox). So there should be fours captures in total. Include these captures, and name them along the lines of **client-tun.cap** and **server-wlan0.cap**. Also include the commands and (partial) output of the ping command and other commands you used during the capture in the file **commands**.

		* Answer


	* c) Create a subfolder called **exercise2c** to hold your answers and configuration files. Using the OpenVPN documentation and the previous exercise's answers, try to set up the VPN so that the VPN client uses the VPN for all its network traffic. This is a fairly common usage scenario, to it is fairly well covered in the basic documentation. Document the commands in a text file **commands**. Include configuration files for both hosts. Perform the same kind of packet capture as in exercise 2b, however, this time the VPN client should ping some host on the internet (e.g. www.google.com) instead of the VPN server. You can use traceroute or mtr to figure out whether traffic is actually going through the VPN or whether it's taking the normal route to the internet. Include the commands and output of the ping and traceroute commands you used during the capture in the file **commands**. If you have network issues during the exercise, one thing to do would be to look at your routing table (ip r show; route -n) and see if you can figure out why traffic is or is not going through the VPN. Of course, send an e-mail or drop by Pol's office (M1.03.20) if you're stuck.

		* Answer

	