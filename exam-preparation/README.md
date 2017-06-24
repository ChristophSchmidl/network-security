# Network Security - Exam Preparation


## Mock Exam

1. **(20 points)** Consider a switched ethernet network (all hosts connected through a single switch) with a gateway 192.168.1.1/24 and additional hosts 192.168.1.2, 192.168.1.3, and 192.168.1.66. Assume the following MAC addresses for the computers in the network:

* ![MACAddresses](img/MACs.PNG)	

	* a) Assume that each node has a "complete" ARP cache, i.e., each node knows the IP-address-MAC-address pairs of all other nodes. Write down all the entries in the ARP cache of 192.168.1.3

		* Answer


	* b) Assume that the attacker at IP address 192.168.1.66 runs an ARP spoofing attack to become a man in the middle between 192.168.1.1 and 192.168.1.2. Assume further that the attacker uses **ARP request spoofing** with the destination MAC address set as usual for ARP requests. What ARP request messages does the attacker have to send? Give destination IP and MAC address and source IP and MAC address for all packets.

		* Answer


	* c) What does the ARP cache of 192.168.1.3 look like after the attack? **Note:** The question is **not** about the ARP cache of one of the targets of the attack!

		* Answer


	* d) How could 192.168.1.2 have prevented the attack?

		* Answer



2. **(20 points)** Consider again the network from exercise 1. Assume that a new computer joins that network (by plugging in a cable and booting up). Assume that this new computer does not know anything about the network and attempts to learn the network configuration via DHCP.

	* a) What pieces of information does the new computer need to receive via DHCP so that the user can fire up a browser, enter http://wikipedia.com in the address bar and the website of wikipedia.com actually loads?

		* Answer

	* b) Assume that an attacker with IP address 192.168.1.66 sets up a rogue DHCP server to become a man in the middle between the new computer and wikipedia.com. Which of the pieces of information from part a) could he modify to become a man in the middle? What information would he send? How would the attack proceed (if there are any further steps required)? Give all possibilities for an attack.

		* Answer
	

	* c) Why could a rogue-DHCP attack fail? What possibilities does an attacker have to increase the chances of success?

		* Answer


3. **(20 points)** For each of the following three different port scan types

	* connect scan, 
	* SYN scan,
	* idle scan

	answer the following questions:

	* a) How does it work? What packets are being sent to probe whether the port is open, what answer packet(s) are expected if the port is open, what answer packet(s) are expected if it's closed?

		* Answer

	* b) The scans are listed in increasing order of "stealthiness". Explain briefly why this is the case by explaining how a system administrator could notice those scans and attribute their origin.
	
		* Answer	



