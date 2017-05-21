# Network Security - Assignment 5

In this exercise you will be using dig, drill, or similar DNS query tools:
* http://www.isc.org/downloads/bind/
* https://www.nlnetlabs.nl/projects/ldns/

1. This exercise is about DDOS attacks using **DNS amplification**. Create a folder **exercise1** to contain the files with your answers.

	* a) Using any tool, script or program you want, figure out the UDP DNS query that gives you the largest DNS amplification. E.g. a query that's 100 bytes and generates a response of 1000 bytes gives you an amplification factor of 10. You are not allowed to use DNS servers under your own control for this, but apart from that you are free to pick any server and any query you want. To make sure that we can verify your answer, make a packet capture of the outgoing query and the incoming response. Members of the group with the largest amplification will get a prize: a copy of "Ghost in the Wires: My Adventures as the World's Most Wanted Hacker" by Kevin Mitnick. In the case of a tie, the first submission in Blackboard wins. Don't spend all your time doing this, however. Find a reasonable query, then do the other exercises before coming back to improve on this answer. Write your answer, preferably as a **dig** or **drill** query, to **exercise1a**. Also store the packet capture as **exercise1a.cap**. If you programmed something for this, include the source code.
		
		* ``` cs@cs-VirtualBox:~$ sudo drill -Db 4096 ANY @89.163.210.121 isc.org ```
		* See also: https://blog.cloudflare.com/deep-inside-a-dns-amplification-ddos-attack/
		* https://technet.microsoft.com/de-de/security/hh972393.aspx

	* b) Now imagine that you are in a LAN with a non-NATing gateway router. Explain how you would use this DNS query to take down a server which has been annoying you for a while, e.g. blackboard.ru.nl. Describe the packet you need to craft, and its relevant features, at DNS level, UDP level, IP level and ethernet level. Do not actually perform the attack. Write your answer to **exercise1b**.

		* To get the most amplification, I'd first need to find a domain with many DNS records. If the domain is example.com and it has subdomains like subdomain1.example.com until subdomain99.example.com, then one DNS request would result into 99 DNS replies based on the amount of DNS records. By using features like EDNS0 and DNSSEC (https://technet.microsoft.com/de-de/security/hh972393.aspx), I would also be able to amplify the attack by a factor above 60. If I wanted to craft such a spoofed DNS request, I had to exchange the MAC address of the source in the ethernet header for the MAC address of the victim. Furthermore, I had to exchange the destination (ip) in the ip header and also had to recalculate the header checksum to make it valid. Next, I had to alter the UDP package. The source port would remain at port 53 (DNS) but I probably had to change the source port because it is different than port 53. At this moment I am not certain how the source port gets chosen. I assume that I also had to alter the UDP checksum after altering the header information. The actual DNS query does not contain any source or destination addresses. I assume that I do not have to alter anything here if the program (dig/drill) already configured everything right through paramter settings. If I had to alter it manually, then I would set the "Recursion desired" flag to 1, query for ANY type and also query all additional records, enable DNSSEC and EDNS0.

	* c) Suppose you are the administrator of this network. You want to make sure that, from the LAN, nobody can use this kind of DNS amplification attack. The LAN network is 203.0.113.0/24, the gateway's internal IP address is 203.0.113.1, and its external IP address is 198.51.100.78. What firewall measures (iptables rules) would be effective in preventing this kind of attack without impeding normal operation of the network? Describe these measure in detail, and also try to come up with actual iptables rules for them. Write your answer to **exercise1c**.

		* ``` 

		# Set default chain policies
		sudo iptables -P INPUT ACCEPT
		sudo iptables -P FORWARD DROP
		sudo iptables -P OUTPUT DROP

		# Accept on localhost. Important, otherwise strange things happen.
		sudo iptables -A INPUT -i lo -j ACCEPT
		sudo iptables -A OUTPUT -o lo -j ACCEPT

		# Only allow outgoing traffic when the source is inside the given ip range of the subnet. DNS Amplificaiton with Ip Spoofing is therefore not possible.
		sudo iptables -A OUTPUT -m iprange --src-range 192.168.1.0-192.168.1.255 -j ACCEPT
		``` 


	
2. Create a folder called **exercise2**. Assume you're an attacker who wants to trick a DNS cache into believing your server is actually hosting blackboard.ru.nl. You try to race a legitimate DNS server to provide the answer faster.

	* a) How would you ensure that you can predict the queries that the cache is going to produce, and how would you ensure that your answers will be accepted (i.e. pass the bailiwick check)? Describe the setup and/or process. Write your answer to **exercise2a**.

		* Answer

	* b) QID randomization and port randomization are (somewhat) effective countermeasures against cache poisoning. If you craft a single blind response, to a single DNS query, what are the odds that you guess right if the DNS cache is only using QID randomization in its queries? What are the odds if the cache is also using source port randomization? Write your answers to **exercise2b**.
	
		* Answer

	* c) Imagine that on top of that, these DNS servers also deploy 0x20 randomization (see slides, the random capital letters in the query). What are the odds now that you will guess right on a query for the blackboard.ru.nl host? Write your answer to **exercise2c**.

		* Answer

	* d) How could you still try to get a good success rate, even though your odds of guessing correctly are low? Describe the general idea behind the attack, exact calculations of probability are not required. Write your answer to **exercise2d**.	

		* Answer

	* e) Explain in your own words, why all these countermeasures do not work against the easy DNS attack, i.e. against a passive MitM attacker. Write your answer to **exercise2e**.
	
		* Answer

	* f) As a completely optional bonus, calculate the number of queries the cache needs to make on average for your attack from 2d to succeed with a 90% success rate, assuming you win every race (i.e. for each query it makes, you successfully inject your own response), for all three situations of only QID randomization, QID and port randomization, and QID, port, and 0x20 randomization on blackboard.ru.nl. Write your answers to **exercise2bonus**.

		* Answer


3. The firewall configuration you made in assignment 4, exercise 1a, should still allow DNS conversations. However, DNS usually runs over UDP and UDP is a connectionless protocol. Try to explain how the firewall still knows that it should allow this DNS traffic. Feel free to consult iptables documentation for this. Write your answer to **exercise3**. 

	* Answer			


