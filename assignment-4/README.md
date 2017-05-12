# Network Security - Assignment 4

In this exercise you will be using the following tools:
	* iptables: http://netfilter.org/projects/iptables/index.html
	* sshuttle: https://github.com/apenwarr/sshuttle

1. In this exercise you will use iptables to create two firewall configurations: one for a client machine, one for a masquerading server. You are encouraged to test your configuration on your own (virtual) machine. You can use the commands ```iptables-save``` and ```iptables-restore``` to save and restore iptables rules to and from a file, respectively. Usage: ```# iptables-save > filename``` stores the firewall configuration in the file ```filename```. ```# iptables-restore < filename``` restores the firewall configuration from filename.
It might be a good idea to run ```iptables-save``` on the firewall configuration you have before starting this exercise. If you get in unrecoverable trouble, you can completely reset the firewall configuration by running the following commands:
* ```
	# iptables -F
	# iptables -X
	# iptables -t nat -F
	# iptables -t nat -X
	# iptables -t mangle -F
	# iptables -t mangle -X
	# iptables -P INPUT ACCEPT
	# iptables -P FORWARD ACCEPT
	# iptables -P OUTPUT ACCEPT

This will flush (-F) all built-in chains and delete (-X) all user-defined chains in the standard tables, and set the default policy (-P) to accept. Create a folder called **exercise1** to hold the answers to this exercise. Note that under some Linux distributions (most notably Ubuntu), you may have to add a rule allowing traffic from localhost to localhost in order to allow some local processes to communicate.

* a) Use the iptables manpage (**man iptables**), the netfilter documentation on http://www.netfilter.org/documentation/index.html#documentation-howto (especially the Packet Filtering HOWTO), the lecture slides, and any sources you want to build a client firewall that does the following:
	* Allow all outgoing traffic.
	* Deny all incoming traffic, except
		* traffic that belongs to an established connection, and
		* incoming SSH traffic (filter on transport protocol and port).
	* Allow all ICMP traffic, except ICMP redirects.	

	If you use tutorials or examples, please make sure you understand what the rules do. Write your firewall configuration, preferably dumped by ```# iptables-save```, to **exercise1a.fw**

	* Answer


* b) If you felt exercise 1a was easy, try your hand at this one. Otherwise, skip to exercise 2 and come back if you have time left over. Do the same for a masquerading server / router with two network cards: eth0 with IP address 198.51.100.42 and eth1 with address 10.0.0.1/24. eth1 is the internal card, the internal network should be obvious from its address. eth0 is the external card, which is the link to the Internet. The firewall should do the following:
	
	* Masquerade traffic coming from the local network going to the Internet.
	* Allow outgoing traffic to the Internet that’s forwarded from the local network.
	* Block all outgoing traffic from the machine itself to the Internet, except for ICMP and traffic that belongs to an established connection.
	* Allow all incoming ICMP traffic.
	* Allow all outgoing traffic from the machine itself to the local network.
	* Block all incoming traffic from the Internet, except traffic that belongs to an established connection.
	* Accept incoming TCP connections on port 80 (let’s say that’s a webinterface) and port 22 from the Internet.
	* Forward TCP and UDP traffic on port 2222 and 8080 to some other host in the local network. Feel free to pick that host yourself.

Since you likely cannot test this, simply give it your best shot. This is the type of configuration you’d use if you use a Linux machine as your home router. Write your firewall configuration, preferably dumped by ```# iptables-save```, to **exercise1b.fw**
	* Answer



2. In this exercise you will use sshuttle to set up a secure tunnel to the lilo login server of the Faculty of Science, and then inspect and analyze the resulting iptables rules. For this, you will need to use your Faculty of Science account. If you do not have one, and do not have access to an alternative SSH server on which sshuttle works, send me an e-mail as soon as possible. Use the manpage of sshuttle (**man sshuttle**) to figure out the command to route everything through the VPN. The remote host to use is **username**@lilo.science.ru.nl, where **username** is your Science login name. Write the command you use to **exercise2**. Remember to run sshuttle as root. Now, view the resulting iptables configuration using either ```# iptables -t <table> -L``` for each table listed in the manual page, or use ```# iptables-save```. Write the rules to **exercise2**, and explain what they do and why they route everything through the VPN. Try e.g. looking for the port number you see in a listing of listening ports. Feel free to play with other configurations (e.g. routing only certain networks through the VPN, or using exceptions) and explain what the different firewall rules for these configurations do as well.

	* Answer

