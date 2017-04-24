# Network Security - Assignment 2

Notes for this assignment:

* My Seup:
	* Macbook Pro 15''
	* Virtualbox 5.1.6
	* Ubuntu 16.04 LTS
	* Wireless USB Adapter (Alfa AWUS036NH 2000mW)
	* Known issue with Macbook Pro and USB power supply:
		* If your Macbook's power supply only relies on the battery, then your USB ports do not provide enough power for the Wireless USB Adapter. Fix: Plug in your external power supply when using the Wireless USB Adapter or use an active USB Hub.
	* To make the Wireless USB Adapter available to Virtualbox, just plug it in and on the top bar, selecet "Devices" -> "USB" and check the WLAN entry for the adapter (i.e. Ralink 802.11 n WLAN)
	* Checking in Ubuntu if the Wireless USB Adapter is working:
	```
	cs@cs-VirtualBox:~$ sudo lshw -C network
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
    ```
    * Checking the network interfaces
    ```
    cs@cs-VirtualBox:~$ sudo ifconfig
		enp0s3    Link encap:Ethernet  HWaddr 08:00:27:59:8a:48  
		          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
		          inet6 addr: fe80::f230:387:60ab:e8e8/64 Scope:Link
		          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
		          RX packets:2531 errors:0 dropped:0 overruns:0 frame:0
		          TX packets:1454 errors:0 dropped:0 overruns:0 carrier:0
		          collisions:0 txqueuelen:1000 
		          RX bytes:2831772 (2.8 MB)  TX bytes:152355 (152.3 KB)

		lo        Link encap:Local Loopback  
		          inet addr:127.0.0.1  Mask:255.0.0.0
		          inet6 addr: ::1/128 Scope:Host
		          UP LOOPBACK RUNNING  MTU:65536  Metric:1
		          RX packets:279 errors:0 dropped:0 overruns:0 frame:0
		          TX packets:279 errors:0 dropped:0 overruns:0 carrier:0
		          collisions:0 txqueuelen:1 
		          RX bytes:23113 (23.1 KB)  TX bytes:23113 (23.1 KB)

		wlx00c0ca5a50a5 Link encap:Ethernet  HWaddr 00:c0:ca:5a:50:a5  
		          UP BROADCAST MULTICAST  MTU:1500  Metric:1
		          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
		          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
		          collisions:0 txqueuelen:1000 
		          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
    ```
    * Installing packags for this assignment
    ```
    cs@cs-VirtualBox:~$ sudo apt-get install aircrack-ng wireshark dsniff
    ```
    * Ubuntu is using its own network manager which could prevent us from using the before mentioned tools. Therefore, we just disable it.
    For Ubuntu 13.10+:
    ```
    cs@cs-VirtualBox:~$ sudo service network-manager stop
    ```
    Older versions of Ubuntu:
    ```
    cs@cs-VirtualBox:~$ sudo /etc/init.d/network-manager stop
    ```
    * Putting the Wireless USB Adapter into monitor mode:
    ```
    cs@cs-VirtualBox:~$ sudo airmon-ng stop mon0


		Interface	Chipset		Driver

		mon0		Ralink RT2870/3070	rt2800usb - [phy2] (removed)
		wlx00c0ca5a50a5		Ralink RT2870/3070	rt2800usb - [phy2]

	cs@cs-VirtualBox:~$ sudo airmon-ng start wlx00c0ca5a50a5


		Found 4 processes that could cause trouble.
		If airodump-ng, aireplay-ng or airtun-ng stops working after
		a short period of time, you may want to kill (some of) them!

		PID	Name
		778	avahi-daemon
		795	avahi-daemon
		2321	wpa_supplicant
		3540	dhclient


		Interface	Chipset		Driver

		wlx00c0ca5a50a5		Ralink RT2870/3070	rt2800usb - [phy2]
						(monitor mode enabled on mon0)
    ```
    * Let the fun begin and see what is on the network:
    ```
    cs@cs-VirtualBox:~$ sudo airodump-ng mon0
    ```


1. The WPA2 suite of security protocols is a (currently) secure replacement for WEP and WPA. It can operate in two modes: WPA2-Enterprise, where each client authenticates against a RADIUS master server and then exchange keys, and WPA2-Personal, or pre-shared key mode, where every client knows the network's master key. Do you think a secured network running in WPA2 pre-shared key mode using a strong random passphrase is secure against clients sniffing traffic in the network? If so, why do you think so? If not, explain in general terms the principle behin an attack. Note that you do not need to have a strong understanding of the cryptography used in WPA2; use your intuition. Write your answer to a faile called exercise1.

	* My intuition says that it is a trivial task for other clients of a WPA2 PSK network to sniff other client's traffic. They all use the same master key to authenticate with the network and I guess it is also used for the encrpytion of packets send over the air. Sending packets over the air is essentially the same as the packet routing mechanism of a network hub with physically attached network cables. Both are using some kind of broadcasting of packets to all clients but the client is responsible for only picking packets which are meant for his address. When a wifi client is using the PSK of a AP, it is the same idea as if he would plug in a network cable into a hub. Therefore I guess that after this step all well known attacks which are suitable for hub scenarios also work with a WPA2 PSK network.
	After doing some research on the security section of stackexchange, my intuition seems to have been right on point:

		* https://security.stackexchange.com/questions/8591/are-wpa2-connections-with-a-shared-key-secure
		* https://security.stackexchange.com/questions/108408/sniffing-wpa2-psk-traffic-with-the-key-but-without-association

2. a) Create a folder called exercise2. Document all the steps you take in a file in this folder called exercise2a. Now let's see what's on the network: ``` # airodump-ng mon0 ```. This will show you a listing of wireless networks, their security level, the access points' MAC addresses (BSSID), channel they operate on (CH), and some other information. **List the networks you see.** You do not have to list duplicate network names. **Identify your target network's name, the access points's MAC address, and channel.** This list will also show you wireless network clients ("stations"). Using the information you have on the target network, identify those clients that are connected to the target network. ** Write down their MAC addresses. When you look at the MAC addresses, does anything strike you as interesting or peculiar? If so, what? Try to explain it.**
	* Answer 	

	b) Now, let's go ahead and crack this network. First, exit airodump-ng. Document all the steps you take here in a file called exercise2b. Cracking WEP is done by capturing enough packets from a network to enable some cryptographic attacks on the algorithms used. Capturing is also done by airodump-ng:
		* ``` # airodump-ng -c <channel> --bssid <target BSSID> -w outputnetsec mon0 ```
	Leave this running. Collecting enough packets in the file specified will take a few minutes. Open the manual page for aircrack-ng and read what it does. Identify what option to use to select the target network. This is the only option you really need, but feel free to play around. ** Just document what you do. **	Run aircrack-ng with the option you need, and the file(s) to which airodump-ng is currently writing its output. ** Once again, document what you use. ** When the attack finally succeeds, you are provided with the WEP key. ** Also document this. ** Leave airodump to capture some more data for good measure, 200.000 frames should be more than enough for the next exercise. Then, exit airodump and put the wireless card back into normal mode ``` airmon-ng stop mon0 ```
	* Answer

3. a) We now have the WEP key, but we also have a generous chunk of data from the network to work with.	Let's work with that and see what we can learn from the network. In exercise 2 you had airodump-ng write its output to a few files, all prefixed with "outputnetsec". In the folder where you ran airodump, you should now see at least a file called outputnetsec-01.cap. Start wireshark. Since we're not going to capture anything, you can run it as a normal user. In wireshark, open the file outputnetsec-01.cap. ** Create a folder called exercise3. Describe what you see in wireshark, after opening the capture file, in a file called exercise3a in that folder. Try to explain why there is very little useful information in this capture file.
	* Answer

	b) There is some useful information, however, and we are going to try to extract that. Wireshark has several very nice analysis tools built into it. They can be accessed in the ** Analyze** and **Statistics** menus. Play around with the tools in the top part of the **Statistics** menu. **Document which clients appear to be most active on the network and whom they seem to be communicating with, in a file called exercise3b. Also add the output from the Comments Summary tool, and try to explain why the Protocol Hierarchy looks the way it does.** If you see more than a few very active clients, limit your description to the clients you identified in the previous exercise as connected to the network. If you protocol hierarchy contains more than a few reasonably explainable protocols, there's something wrong with your encrypted capture.
	* Answer

	c) Now, to solve the problem identified in exercise3a, aircrack-ng has the tool airdecap-ng. Open its manual page (man airdecap-ng), identify what options you need to pass, then run it with these options on outputnetsec-01.cap. This will create a file outputnetsec-01-dec.cap. Close the file you currently have open in wireshark, then open this new file. **Once again, describe what you see in wireshark, now in exercise3c. Explain why this is different from what you saw in exercise3a.**
	* Answer

	d) **Similar to exercise3b, using the statistics tools, document which clients are communicating with whom, in a file called exercise3d. Also include their IP addresses. Something should immediately strike you as peculiar when doing this. What do you think is going on here?** You should be able to go into much more details this time. Therefore, this time, also zoom in on the conversations themselved (if you right-click on a conversation in the output from the Conversations tool, you can apply this conversation as a filter so that you only see its packets). There will likely be more than just a few conversations. Pick a few larger ones, or ones that look interesting. **Briefly describe what each conversation is, whether it looks interesting, and why.**
	* Answer

	e) **There should be at least one connection which is consistently being rejected. See if you can find it. Document how you did this in exercise3e.** Not you can filter out conversations which you are not interested in by simply right-clicking on that conversation in the Conversations tool, and preparing a filter. Filter out multiple conversations by using the ... and not ... entry on each. Then, apply the filter. Most of the time, you'll simply want to build filters using the graphical interface, but for more documentation on their syntax, see https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html.
	* Answer

	f) Finally, there should be several conversations which, when you look at the packets' contents, are obviously interesting for you. Find them. **Document the process in exercise3f, and also include why you think they are interesting.**
	* Answer

4. a) Run wireshark with root rights, and let it sniff you wireless interface. It should not use either monitor or promiscuous mode. Ping one of the other clients you identified in exercise 3, and see whether these pings show up in wireshark. Note that you may have to specify which interface to ping on, use the manual page (man ping) to figure out how. If this works, enable IP forwarding: ``` # echo 1 > /proc/sys/net/ipv4/ip_forward ```. If using sudo, you will need a slighty different command: ``` $ sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward" ``` or ``` $ echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward ```	This is due to nuances in when shell redirection happens. Now you can use arpspoof to trick the sending endpoint in the conversation to send its data to you instead of the receiving endpoint, and your machine will forward the data. Use the manual page of arpspoof (man arpspoof) for details on how to use it. Note that you need to keep arpspoof running as long as you want traffic to be redirected, and you should close it down as soon as you're done. Note that you will need to tell arpspoof what interfaces to use, since that determines how and where it spoofs the targets. Verfiy that the traffic of that conversation is flowing through your machine. You should see, among other things, two identical sets of IPv4 packets, interleaved. One set should have as a source address the MAC address of the endpoint you just started ARP spoofing to, and as destination address your own MAC address. The other set should have as source address your own MAC address and as destination address the MAC address of the original receiving endpoint of the conversation. If you do not see the second set, IP forwarding is not working. If you do not see the first set, spoofing is not working. **If this works, turn off arpspoof. Save the wireshark capture to a file called exercise4a.cap in the folder exercise4. Document the commands you used in a file called exercise4a, and explain why you're seeing these two sets of packets in wireshark.** Turn off IP forwarding: ``` # echo 0 > /proc/sys/net/ipv4/ip_forward ``` or ``` $ sudo sh -c "echo 0 > /proc/sys/net/ipv4/ip_forward" ``` or ``` $ echo 0 | sudo tee /proc/sys/net/ipv4/ip_forward ```
	* Answer