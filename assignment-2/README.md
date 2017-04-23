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