# Network Security - Assignment 3

1. This question is about IP address spoofing. Write your answers to every subquestion to a file called **exercise1**, making sure to prefix each answer with the letter for that question.
	* a) Take a look at the RFC for the **Internet Protocol**, RFC 791 (https://www.ietf.org/rfc/rfc791.txt). Explain what IP address spoofing is, and what a host on the network must do to spoof its IP address.
		* Answer

	* b) Take a look at the RFC for the **User Datagram Protocol**, RFC 768 (http://www.ietf.org/rfc/rfc768.txt), and the RFC for **Transmission Control Protocol**, RFC 793 (https://www.ietf.org/rfc/rfc793.txt). Explain why an attacker cannot just grab any existing IP packet carrying UDP or TCP, change only the IP addresses in there, and expect the target host to accept the packet. Especially for TCP, don't read the entire RFC but focus on the header (pages 15 - 19)
		* Answer

	* c) During the lecture we explained SYN flooding attacks. Review that now (slide 10 in https://cryptojedi.org/peter/teaching/netsec2017/tcpip_print.pdf). If an attacker wants to do SYN flooding while IP spoofing, she faces a problem. Let's first consider the case where the attacker, Mallory, tries spoofing the IP of an existing host, Bob, to SYN flood her target, Alice. Using the TCP RFC, explain which packets get sent to whom when Mallory sends a SYN to Alice using Bob's address as source. Focus on the TCP three-way handshake and the Reset Generation in section 3.4, "Establishin a connection". Explain why this will cause the SYN flood attack to fail.
		* Answer

	* d) When Mallory tries to use the address of Ursula, who's currently not on the network, she does no face the problem you uncovered in the previous question. However, there is now another protocol in play which causes the attack to fail. Take a look at the RFC for the **Internet Control Message Protocol** (https://tools.ietf.org/rfc/rfc792.txt). Read the first five pages, and explain which packets get sent to whom when Mallory sends a SYN to Alice using Ursula's address as source. Explain why this will cause the SYN flood attack to fail.
		* Answer

	* e) Using what you've learned in this course so far, describe a way to make Mallory's SYN flood attack succeed against Alice, while IP spoofing using either Bob's or Ursula's address. You may assume that Mallory is in the same network as Alice. If you mae any more assumptions (e.g. Mallory is able to modify all traffic on the network) please state these.
		* Answer


2. This question is about port blocking. Write you answer to a file called **exercise2**. As a network security measure, some network administrators attempt to restrict what external serviced their users can access by blocking any outgoing connection made to all but a few well-known ports. This by itself is not a very effective measure, since it will inconvenience normal users, but it will do nothing to stop somebody in control of the external endpoint. Consider you are such a person. You know that soon you will be on a network that blocks every outgoing connection except on port 53 (DNS), 80 (HTTP), and 443 (HTTPS). What could you do to be able to access the SSH service on your external server once you are inside this network?
	* Answer

3. This exercise has you using nmap. Write your answers to separate files in a folder called **exercise3**. So for exercise 3a you should use **exercise3/exercise3a**, etc. Not that you will need root rights to execute many of the scan types nmap provides, since they use raw sockets. Connect to the homework network. You should have recovered the key in the previous exercise. If you connect using a static IP, use an IP address in the range 192.168.84.200-249. Net netmask is /24, or 255.255.255.0. The network will be present at the werkcollege, and at other times it will be reachable from the central common area on the ground floor of the Mercator 1 building. Not that some of you will be scanning each other if you're performing this exercise at the same time. This is fine. Portscans are not harmful. However, do not attack each other.

	* a) Read the manual page section on **host discovery**. Your first task is to map the network. Discover all the active hosts, and write your results to **exercise3a**. Also explain how you discovered them.Since you're scanning on a wireless network, the scan appear to be not as reliable as on a wired network. Furthermore, you're not supposed to spend hours waiting on scans to complete. Read the manual page section on timing and performance. Try to play with a higher timing template (-T), different max-retries or host-timeout, and other stuff, if hosts seem to intermittently drop from the network, or if scans take too long.
		* Answer

	* b) Read the manual page section on **OS detection**. You should have found a lot of active hosts in the range 192.168.84.1-99. However, as you should have concluded from the previous assignment, many of these hosts are the same machine with different IP addresses. Try to detect the Operating Systems running on a few hosts you found in the reanges 192.168.84.1-9, 192.168.84.10-19, 192.168.84.20-59 and 192.168.84.60-99. If there is more than one active host in a range, pick (at least) two from the range; however don't bother scanning them all. Write you results to **exercise3b**, and explain how you got them
		* Answer

	* c) Read the section on **port scanning basics**, **port scanning techniques**, and **port specification** and **scan order**. Scan for open ports on the same hosts you scanned in **3b**. Write your results to **exercise3c**, and explain your scanning techniques.
		* Answer

	* d) Read the section on **service and version detection**. Try to detect what services are running on what ports for the same hosts you scanned in 3b and 3c. List these results in **exercise3d**. Also mention which of these services are running on non-standard ports. If nmap is unable to determine what a service is, make a guess based on its port number. A list of standard ports is often available on Linux machines in /etc/services, and can also be found at the Internet Assigned NUmbers Authority (IANA) (http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml).
		* Answer

	* e) (OPTIONAL) If you were an attacker, intent on gaining access to one of these machines, which service would you attack first, and why? Write you answer to **exercise3e**.
		* Answer

4. Don't forget exercise 4 from assignment 2. Use the folder **exercise4** for that.						

