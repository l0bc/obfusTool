Little python tool to obfuscate IPs in hope of bypassing WAF/WebApp whitelists or blacklists
Use only for educational porpuses, pentesting/bounty Hunting or on a monitored environment 

usage: ipObf.py [-h] [-t {1,2,3,4,5,6}] [-u IPP] [-d] [-p [PADDING]] [-a]

optional arguments:
  -h, --help            show this help message and exit
  -t {1,2,3,4,5,6}, --type {1,2,3,4,5,6}
                        Type of obfuscation: 1:zero 2:octal 3:hexa 4:dword 5:binary 6:overFlow
  -u IPP, --ip-address IPP
                        IP address to be obfuscated
  -d, --dotless         Resulting IP dottless (default) i.e. 0x7f01
  -p [PADDING], --padding [PADDING]
                        How many ceros to pad
  -a, --alll            all combinations, default padding is 7
DWORD is not integrated when ussing the -a flag. (ToDo...)
	would need to compress the dword into 2 bytes to only obfuscate 1 octet of the IP

Happy Hacking!
