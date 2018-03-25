import sys
import re

def ip_convert_to_bits(a_Ip):
	#print(a_Ip)
	a_Ip_bin = [None]*4
	a_Ip_bin[0] = bin(int(a_Ip[0]))[2:]
	a_Ip_bin[1] = bin(int(a_Ip[1]))[2:]
	a_Ip_bin[2] = bin(int(a_Ip[2]))[2:]
	a_Ip_bin[3] = bin(int(a_Ip[3]))[2:]
	return a_Ip_bin

def main(argv):
	s_Ip = argv[0]
	#ipv4 and ipv6 patterns
	ipv4_pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
	ipv6_pattern = re.compile("(?<![:.\w])(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}(?![:.\w])")
	if(ipv4_pattern.match(s_Ip)):
		print('ipv4 found')	
		a_Ip = s_Ip.split(".")
		print(ip_convert_to_bits(a_Ip))
	
	elif(ipv6_pattern.match(s_Ip)):
		print("can't handle ipv6, yet... exiting...")
		#CANT HANDLE IPV6
		sys.exit()
	else:
		print('invalid IP format... exiting...')
		sys.exit()
	
if __name__ == "__main__":
	main(sys.argv[1:]); 
