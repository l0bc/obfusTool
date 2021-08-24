<h1>Obfus Tool</h1>

Little python tool to obfuscate IPs in hope of bypassing WAF/WebApp whitelists or blacklists
<br>Use only for educational porpuses, pentesting/bounty Hunting or on a monitored environment 

<h2>USAGE</h2> <code><h4>ipObf.py [-h] [-t {1,2,3,4,5,6}] [-u IPP] [-d] [-p [PADDING]] [-a]</h4>

	optional arguments:<br>
	-h, --help            show this help message and exit<br>
	-t {1,2,3,4,5,6}, --type {1,2,3,4,5,6}<br>
	                      Type of obfuscation: 1:zero 2:octal 3:hexa 4:dword 5:binary 6:overFlow<br>
	-u IPP, --ip-address IPP<br>
	                       IP address to be obfuscated<br>
	-d, --dotless         Resulting IP dottless (default) i.e. 0x7f01<br>
	-p [PADDING], --padding [PADDING]<br>
	                      How many ceros to pad<br>
	-a, --alll            all combinations, default padding is 7<br>
</code>
<h3>ToDo</h3><br>
DWORD is not integrated when ussing the -a flag. (ToDo...)<br>would need to compress the dword into 2 bytes to only obfuscate 1 octet of the IP<br>

Happy Hacking!
