# Network Security - Exam Preparation


## Mock Exam

1. (**20 points**) Consider a switched ethernet network (all hosts connected through a single switch) with a gateway 192.168.1.1/24 and additional hosts 192.168.1.2, 192.168.1.3, and 192.168.1.66. Assume the following MAC addresses for the computers in the network:

* ![MACAddresses](img/MACs.PNG)	

	* a) Assume that each node has a "complete" ARP cache, i.e., each node knows the IP-address-MAC-address pairs of all other nodes. Write down all the entries in the ARP cache of 192.168.1.3


	* b) Assume that the attacker at IP address 192.168.1.66 runs an ARP spoofing attack to become a man in the middle between 192.168.1.1 and 192.168.1.2. Assume further that the attacker uses **ARP request spoofing** with the destination MAC address set as usual for ARP requests. What ARP request messages does the attacker have to send? Give destination IP and MAC address and source IP and MAC address for all packets.


	* c) What does the ARP cache of 192.168.1.3 look like after the attack? **Note:** The question is **not** about the ARP cache of one of the targets of the attack!


	* d) How could 192.168.1.2 have prevented the attack?