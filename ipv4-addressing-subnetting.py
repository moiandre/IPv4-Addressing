#/usr/bin/env python3

####################################################################
# Helps students understand the relationship between
# IPv4 network, first host, last host, and broadcast addresses
# in dotted decimal and binary.
#
# Demonstration mode
#
#####################################################################

import random
import sys

def welcome():
	"""Instructions"""
	
	print('\n*****************************************************************************')
	print("\nWelcome to Rick's Subnet Calculator - Demonstration Mode")
	print("\nPart 1: Major Network")
	print("1. You are prompted for an IPv4 address and subnet mask.")
	print("2. Displays the IPv4 address, subnet mask, network address, first host,")
	print("   last host and broadcast addresses in binary and dotted decimal.")
	print("3. Displays additional information such as the number of network bits,")
	print("   host bits and the number of hosts addresses for this network.")
	print("4. Generates an example of a host address on this network (optional).")
	print("\nPart 2: Subnetting (optional)")
	print("1. You are prompted for a new subnet mask to subnet the network.")
	print("2. Displays the IPv4 address, subnet mask, network address, first host,")
	print("   last host and broadcast addresses in binary and dotted decimal.")
	print("3. Displays additional information such as the number of network bits,")
	print("   host bits, the number of subnets, and the number of hosts per subnet.")
	print("4. Generates an example of a host address on this network (optional).")
	print("\nPart 3: Subnet List (optional)")
	print("1. Generates a list of all subnets.")
	print("\nNote: Use control-C to exit at any time.\n")
	print("\nNote: The program ipv4-addressing-test.pl can be used to test your knowledge")

def enter_ipv4_address():
	"""Ask user for a valid IPv4 address"""

	#Checking IP address validity
	while True:
		try:
			ipv4_address = input("\nEnter an IPv4 address: ")
		except KeyboardInterrupt:
			print('\nGood bye!\n')
			sys.exit()


		#Checking octets - split ipv4_address string into list a using "." as a delimiter           
		a = ipv4_address.split('.')

		#Diagnostics
		# print('ipv4_address = ', ipv4_address)   
		# print('type ipv4_address =')
		# type_add = type(ipv4_address)  
		# print(type_add)   
		# print('type a =')
		# type_a = type(a)  
		# print(type_a)   
		# print('a = ',a)   
		# print('len(a) =', len(a))  
		# print('a[0] = ', a[0])   
		# print('int(a[0]) = ', int(a[0]))   
		# print('int(a[1]) = ', int(a[1]))   
		# print('int(a[2]) = ', int(a[2]))   
		# print('int(a[3]) = ', int(a[3]))   

		# ipv4_address = 200.44.33.1
		# type(ipv_address) = <class 'str'>
		# type(a) = <class 'int'>
		# a = ['200', '44', '33', '1']
		# len(a) = 4
		# a[0] = 200
		# int(a[0]) = 200
		# int(a[1]) = 44
		# int(a[2]) = 33
		# int(a[3]) = 1



		if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
			break

		else:
			print ("\nThe IPv4 address is NOT a valid unicast address! Please try again!\n")
			continue

	return ipv4_address


def enter_subnet_mask():
	"""Ask user for a valid IPv4 subnet mask in dotted decimal"""
	
	masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
	
	#Checking Subnet Mask validity
	while True:
		try:
			major_subnet_mask = input("Enter the current subnet mask: ")
		except KeyboardInterrupt:
			print('\nGood bye!\n')
			sys.exit()

		#Checking octets - split major_subnet_mask string into list b using "." as a delimiter                      
		b = major_subnet_mask.split('.')
		first_subnet_octet = False
		second_subnet_octet = False
		third_subnet_octet = False
		fourth_subnet_octet = False

		#print (b[0],b[1],b[2],b[3])
		if (len(b) == 4) and (int(b[0]) in masks) :
			#print('The octets are: ', b[0])
			first_subnet_octet = True
		else:
			print('Invalid mask. Exit.')
			exit()
		
		if ((int(b[1]) in masks) and (int(b[1])<int(b[0]))) or ((int(b[0])==255) and (int(b[1])==255)) :
			#print('The octets are: ', b[0], b[1])
			second_subnet_octet = True
		if ((int(b[2]) in masks) and (int(b[2])<int(b[1])) or (int(b[2])==0)) or ((int(b[1])==255) and (int(b[2])==255)):
			#print('The octets are: ', b[0], b[1], b[2])
			third_subnet_octet = True
		if ((int(b[3]) in masks) and (int(b[3])<int(b[2])) or (int(b[3])==0)) :
			#print('The octets are: ', b[0], b[1], b[2], b[3])
			fourth_subnet_octet = True

		#print (first_subnet_octet, second_subnet_octet, third_subnet_octet, fourth_subnet_octet)

		if (first_subnet_octet == True) and (second_subnet_octet == True) and (third_subnet_octet == True) and (fourth_subnet_octet == True) :
			#print ("\nThe subnet mask is valid\n")
			break
		else :
			print ("\nThe subnet mask is INVALID or is /32! Please enter the subnet mask again:\n")
			continue

	return major_subnet_mask


def convert_mask_to_binary(subnet_mask):

	#Convert mask to binary string
	mask_octets_padded = []
	mask_octets_decimal = subnet_mask.split(".")
	# print ('mask_octets_decimal = ', mask_octets_decimal)
	# print ('len(mask_octets_decimal) = ',len(mask_octets_decimal))
	# print ('\n')

	# mask_octets_decimal =  ['255', '255', '240', '0']
	# len(mask_octets_decimal) =  4
	#
	# mask_octets_decimal =  ['255', '255', '255', '0']
	# len(mask_octets_decimal) =  4

	for octet_index in range(0, len(mask_octets_decimal)):

		binary_octet = bin(int(mask_octets_decimal[octet_index])).split("b")[1]

		#Diagnostics
		# print ('octet_index = ', octet_index) 
		# print ('bin(int(mask_octets_decimal[octet_index])) = ', bin(int(mask_octets_decimal[octet_index])))  
		# print('len(binary_octet) = ', len(binary_octet)) 
		# print ('binary_octet = ', binary_octet) 		

		# octet_index =  0
		# bin(int(mask_octets_decimal[octet_index])) =  0b11111111
		# len(binary_octet) =  8
		# binary_octet =  11111111

		# octet_index =  1
		# bin(int(mask_octets_decimal[octet_index])) =  0b11111111
		# len(binary_octet) =  8
		# binary_octet =  11111111

		# octet_index =  2
		# bin(int(mask_octets_decimal[octet_index])) =  0b11110000
		# len(binary_octet) =  8
		# binary_octet =  11110000

		# octet_index =  3
		# bin(int(mask_octets_decimal[octet_index])) =  0b0
		# len(binary_octet) =  1
		# binary_octet =  0



		if len(binary_octet) == 8:
			mask_octets_padded.append(binary_octet)
		elif len(binary_octet) < 8:
			binary_octet_padded = binary_octet.zfill(8)
			mask_octets_padded.append(binary_octet_padded)


	binary_mask = "".join(mask_octets_padded)

	# Diagnostics
	# print ('mask_octets_padded =', mask_octets_padded)	
	# print ('binary_mask = ', binary_mask)

	# mask_octets_padded = ['11111111', '11111111', '11110000', '00000000']
	# binary_mask =  11111111111111111111000000000000

	no_of_zeros = binary_mask.count("0")
	no_of_ones = 32 - no_of_zeros
	no_of_hosts = abs(2 ** no_of_zeros - 2)

	# Diagnostics
	# binary_mask.count("0") Counts the number of 0s in binary_mask
	# print ('no_of_zeros = ', no_of_zeros)
	# print ('no_of_ones = 32 - no_of_zeros = ', no_of_ones)  	
	# print ('no_of_hosts = abs(2 ** no_of_zeros - 2) = ', no_of_hosts)

	# no_of_zeros =  12
	# no_of_ones = 32 - no_of_zeros =  20
	# no_of_hosts = abs(2 ** no_of_zeros - 2) =  4094

	# Return binary mask, number of ones, number of zeros, number of hosts
	return (binary_mask, no_of_ones, no_of_zeros, no_of_hosts)


def convert_ipv4_to_binary():  # was convert_ipv4_to_binary_and_display
	""" Convert IPv4 Address to binary """

	ip_octets_padded = []
	ip_octets_decimal = user_ipv4_address.split(".")

	# Diagnostics
	# print ('ip_octets_padded = ', ip_octets_padded)
	# print ('user_ipv4_address = ', user_ipv4_address)
	# print ('ip_octets_decimal = ', ip_octets_decimal)
	# print ('len(ip_octets_decimal) = ', len(ip_octets_decimal))
	
	# ip_octets_padded =  []
	# user_ipv4_address =  200.44.33.1
	# ip_octets_decimal =  ['200', '44', '33', '1']
	# len(ip_octets_decimal) =  4
	
	for octet_index in range(0, len(ip_octets_decimal)):

		binary_octet = bin(int(ip_octets_decimal[octet_index])).split("b")[1]

		# Diagnostics
		# print ('int(ip_octets_decimal[octet_index]) = ', int(ip_octets_decimal[octet_index]))
		# print ('binary_octet = ', binary_octet)
		
		# 1. int(ip_octets_decimal[octet_index]) =  200
		# binary_octet =  11001000

		# 2. int(ip_octets_decimal[octet_index]) =  44
		# binary_octet =  101100

		# 3. int(ip_octets_decimal[octet_index]) =  33
		# binary_octet =  100001

		# 4. int(ip_octets_decimal[octet_index]) =  1
		# binary_octet =  1


		if len(binary_octet) < 8:
			binary_octet_padded = binary_octet.zfill(8)
			ip_octets_padded.append(binary_octet_padded)

			# Diagnostics
			# print (' < 8 len(binary_octet) = ', len(binary_octet))
			# print ('binary_octet.zfill(8) = ', binary_octet.zfill(8))
			# print ('binary_octet_padded = ', binary_octet_padded)
			# print ('ip_octets_padded = ', ip_octets_padded)
			
			# 2. < 8 len(binary_octet) =  6
			# binary_octet.zfill(8) =  00101100
			# binary_octet_padded =  00101100
			# ip_octets_padded =  ['11001000', '00101100']

			# 3. < 8 len(binary_octet) =  6
			# binary_octet.zfill(8) =  00100001
			# binary_octet_padded =  00100001
			# ip_octets_padded =  ['11001000', '00101100', '00100001']
			
			# 4. < 8 len(binary_octet) =  1
			# binary_octet.zfill(8) =  00000001
			# binary_octet_padded =  00000001
			# ip_octets_padded =  ['11001000', '00101100', '00100001', '00000001']			
						
		else:
			ip_octets_padded.append(binary_octet)

			# Diagnostics 
			# print ('>=8 len(binary_octet) = ', len(binary_octet))
			# print ('ip_octets_padded = ', ip_octets_padded)

			# 1. >=8 len(binary_octet) =  8
			# ip_octets_padded =  ['11001000']

	#print ip_octets_padded

	binary_ip = "".join(ip_octets_padded)
	#print ("Your IPv4 address in binary is", binary_ip)
	return (binary_ip)  

def generate_address_binary(convert_no_of_ones, convert_no_of_zeros, convert_no_of_hosts):

	# Determine network, first host, last host, and broadcast in binary
	network_address_binary = binary_ip[:(convert_no_of_ones)] + "0" * convert_no_of_zeros

	# print ('binary_ip[:(convert_no_of_ones)] = ', binary_ip[:(convert_no_of_ones)])
	# print ('+ 0 * ')
	# print ('convert_no_of_ones = ', convert_no_of_ones)	
	# print ('network_address_binary = ', network_address_binary)

	# binary_ip[:(convert_no_of_ones)] =  11001000001011000010
	# + 0 * 
	# convert_no_of_ones =  20
	# network_address_binary =  11001000001011000010000000000000

	first_host_binary = binary_ip[:(convert_no_of_ones)] + "0" * (convert_no_of_zeros - 1) + "1"

	# print ('binary_ip[:(convert_no_of_ones)] = ', binary_ip[:(convert_no_of_ones)])
	# print ('+ 0 * ')
	# print ('(convert_no_of_zeros - 1) + "1" = ', (convert_no_of_zeros - 1), '+ 1')	
	# print ('first_host_binary = ', first_host_binary)

	# binary_ip[:(convert_no_of_ones)] =  11001000001011000010
	# + 0 * 
	# (convert_no_of_zeros - 1) + "1" =  11 + 1
	# first_host_binary =  11001000001011000010000000000001

	last_host_binary = binary_ip[:(convert_no_of_ones)] + "1" * (convert_no_of_zeros -1) + "0"	

	# print ('binary_ip[:(convert_no_of_ones)] = ', binary_ip[:(convert_no_of_ones)])
	# print ('+ 1 * ')
	# print ('(convert_no_of_zeros - 1) + "0" = ', (convert_no_of_zeros - 1), '+ 0')	
	# print ('last_host_binary = ', last_host_binary)

	# binary_ip[:(convert_no_of_ones)] =  11001000001011000010
	# + 1 * 
	# (convert_no_of_zeros - 1) + "0" =  11 + 0
	# last_host_binary =  11001000001011000010111111111110

	broadcast_address_binary = binary_ip[:(convert_no_of_ones)] + "1" * convert_no_of_zeros	

	# print ('binary_ip[:(convert_no_of_ones)] = ', binary_ip[:(convert_no_of_ones)])
	# print ('+ 1 * ')
	# print ('(convert_no_of_zeros) = ', (convert_no_of_zeros ))	
	# print ('broadcast_address_binary = ', broadcast_address_binary)

	# binary_ip[:(convert_no_of_ones)] =  11001000001011000010
	# + 1 * 
	# (convert_no_of_zeros) =  12
	# broadcast_address_binary =  11001000001011000010111111111111

	return(network_address_binary,first_host_binary,last_host_binary,broadcast_address_binary)

def display_addresses_binary(binary_mask, no_of_ones, no_of_zeros, no_of_hosts, network_address_binary, first_host_binary, last_host_binary, broadcast_address_binary, net_no_of_ones, sub_no_of_ones):   

	print ('\n\tIPv4 address in binary:\t\t', binary_ip[0:8], binary_ip[8:16], binary_ip[16:24], binary_ip[24:32])   #Example: for 192.168.2.100 => 11000000101010000000001001100100
	print ('\tSubnet mask in binary:\t\t',binary_mask[0:8],binary_mask[8:16],binary_mask[16:24],binary_mask[24:32])        	
	
	if network_address_binary == binary_ip:
		print ("\nThis is a NETWORK address. There are all 0s in the host portion.")
	elif broadcast_address_binary == binary_ip:
		print ("\nThis is a BROADCAST address. There are all 1's in the host portion.")
	else:
		print ("\nThis is a HOST address. There are not all 0s nor all 1s in the host portion.")

	input('Press enter to continue...')


	# print ("\nWhat are the network, first host, last host and broadcast addresses in binary?\nHost portion:\tNetwork address - all 0s\n\t\tFirst host - all 0s and a 1\n\t\tLast host - all 1's and a 0\n\t\tBroadcast - all 1s")
	# input('Press enter to continue...')

	print ('\nIPv4 address:\t', binary_ip[0:8], binary_ip[8:16], binary_ip[16:24], binary_ip[24:32])   #Example: for 192.168.2.100 => 11000000101010000000001001100100
	print ('Subnet mask:\t',binary_mask[0:8],binary_mask[8:16],binary_mask[16:24],binary_mask[24:32])        
	print ('            \t','-----------------------------------    Copy the network bits:')
	
	#network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
	print ('\rNetwork:\t', network_address_binary[0:8], network_address_binary[8:16], network_address_binary[16:24], network_address_binary[24:32], '   Network + Host (all 0s)')

	#first_host_binary = binary_ip[:(no_of_ones)] + "0" * (no_of_zeros - 1) + "1"
	#print first_host_binary
	print ('First host:\t', first_host_binary[0:8], first_host_binary[8:16], first_host_binary[16:24], first_host_binary[24:32], '   Network + Host (all 0s + 1)')

	#last_host_binary = binary_ip[:(no_of_ones)] + "1" * (no_of_zeros -1) + "0"
	print ('Last host:\t', last_host_binary[0:8], last_host_binary[8:16], last_host_binary[16:24], last_host_binary[24:32], '   Network + Host (all 1s + 0)')

	#broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
	print ('Broadcast:\t', broadcast_address_binary[0:8], broadcast_address_binary[8:16], broadcast_address_binary[16:24], broadcast_address_binary[24:32], '   Network + Host (all 1s)')

	prefix_length = ['/',str(no_of_ones)]
	to_the_power = ['2^',str(no_of_zeros)]

	# print ("\nWhat are the number of network bits, host bits and the number of hosts? ")
	# input('Press enter to continue...')

	if sub_flag == 1:
		to_the_power_subs = ['2^',str(sub_no_of_ones - net_no_of_ones)]
		print ("\nNumber of network bits: ", no_of_ones, "bits or", ''.join(prefix_length))
		print ("Number of subnet bits: ", (sub_no_of_ones - net_no_of_ones), "bits")
		print ("Number of subnets: ", ''.join(to_the_power_subs), '=', (2**(sub_no_of_ones - net_no_of_ones)), "subnets")
		print ("Number of host bits: ", no_of_zeros, "bits")
		print ('Number of hosts per subnet: ', ''.join(to_the_power),'- 2 =', no_of_hosts, 'hosts per subnet')
	else:
		print ("\nNumber of network bits: ", no_of_ones, "bits or", ''.join(prefix_length))
		print ("Number of host bits: ", no_of_zeros, "bits")
		print ('Number of hosts : ', ''.join(to_the_power),'- 2 =', no_of_hosts, 'hosts')

	#return(network_address_binary,first_host_binary,last_host_binary,broadcast_address_binary)


def convert_addresses_to_dotted(convert_network_address_binary, convert_first_host_binary, convert_last_host_binary, convert_broadcast_address_binary):

	net_ip_octets = []
	for octet in range(0, len(convert_network_address_binary), 8):
		net_ip_octet = convert_network_address_binary[octet:octet+8]
		net_ip_octets.append(net_ip_octet)

	#print net_ip_octets

	net_ip_address = []
	for each_octet in net_ip_octets:
		net_ip_address.append(str(int(each_octet, 2)))

    #print net_ip_address

	network_address = ".".join(net_ip_address)
	#print network_address



	first_ip_octets = []
	for octet in range(0, len(convert_first_host_binary), 8):
		first_ip_octet = convert_first_host_binary[octet:octet+8]
		first_ip_octets.append(first_ip_octet)        
	#print net_ip_octets

	first_ip_address = []
	for each_octet in first_ip_octets:
		first_ip_address.append(str(int(each_octet, 2)))            
	#print first_ip_address

	first_host_address = ".".join(first_ip_address)
	#print first_host_address

	last_ip_octets = []
	for octet in range(0, len(convert_last_host_binary), 8):
		last_ip_octet = convert_last_host_binary[octet:octet+8]
		last_ip_octets.append(last_ip_octet)        
	#print last_ip_octets

	last_ip_address = []
	for each_octet in last_ip_octets:
		last_ip_address.append(str(int(each_octet, 2)))            
	#print last_ip_address

	last_host_address = ".".join(last_ip_address)
	#print last_host_address

	bst_ip_octets = []
	for octet in range(0, len(convert_broadcast_address_binary), 8):
		bst_ip_octet = convert_broadcast_address_binary[octet:octet+8]
		bst_ip_octets.append(bst_ip_octet)        
	#print bst_ip_octets

	bst_ip_address = []
	for each_octet in bst_ip_octets:
		bst_ip_address.append(str(int(each_octet, 2)))            
	#print bst_ip_address

	broadcast_address = ".".join(bst_ip_address)
	#print broadcast_address

	return(network_address, first_host_address, last_host_address, broadcast_address, net_ip_address, bst_ip_address)


def display_first_last_broadcast_dotted(network_address, first_host_address, last_host_address, broadcast_address):
	"""Print dotted decimal network, first, last broadcast, number of hosts"""


	#Print the results for selected IP/mask
	# print("\nWhat are the network, first host, last host and broadcast addresses in dotted decimal?")
	# input('Press enter to continue...')

	print ("\nAddresses in dotted decimal notation:")
	print ("Network address is: %s" % network_address)
	print ("First host is: %s" % first_host_address)
	print ("Last host is: %s" % last_host_address)
	print ("Broadcast address is: %s" % broadcast_address)
	print("\n")

	#return(net_ip_address, bst_ip_address, network_address)


def generate_random_ipv4(net_ip_address, bst_ip_address):
	"""Generation of random IPv4 for the subnet"""

	while True:
		try:
			generate = input("Generate a random IPv4 host address from subnet? (y/n)")
		except KeyboardInterrupt:
			print('\nGood bye!\n')
			sys.exit()


		if generate == "y":
			generated_ip = []

			#Obtain available IP address in range, based on the difference between octets in broadcast address and network address
			for indexb, oct_bst in enumerate(bst_ip_address):
				#print indexb, oct_bst
				for indexn, oct_net in enumerate(net_ip_address):
					#print indexn, oct_net
					if indexb == indexn:
						if oct_bst == oct_net:
							#Add identical octets to the generated_ip list
							generated_ip.append(oct_bst)
						else:
							#Generate random number(s) from within octet intervals and append to the list
							generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))

			#IP address generated from the subnet pool
			#print generated_ip
			y_iaddr = ".".join(generated_ip)
			#print y_iaddr

			print ("Random IPv4 host address for this network is: %s" % y_iaddr)
			continue

		else:
			break


def display_major_network(network_address, network_address_binary, net_subnet_mask, binary_mask):
	"""Display the major network information to be subnetted"""

	print("\nThe current network address and subnet mask are:")
	print("\tNetwork address: \t", network_address, "\t", network_address_binary[0:8], network_address_binary[8:16], network_address_binary[16:24], network_address_binary[24:32])
	print("\tSubnet mask:\t\t",net_subnet_mask,"\t", binary_mask[0:8],binary_mask[8:16],binary_mask[16:24],binary_mask[24:32])


def subnet_major_network(net_binary_mask):
	"""Ask user for the subnet mask and generate subnet information"""
	
	while True:
		print ('\nThe new subnet mask must have additional 1 bits by borrowing bits from the host address.')
		try:
			new_subnet_mask = input("\nEnter a different subnet mask to subnet the previous network: ")
		except KeyboardInterrupt:
			print('\nGood bye!\n')
			sys.exit()

		new_binary_mask, new_no_of_ones, new_no_of_zeros, new_no_of_hosts = convert_mask_to_binary(new_subnet_mask)
		#print("new2", new_binary_mask, new_no_of_ones, new_no_of_zeros, new_no_of_hosts)

		# Check to see if new mask is longer than network mask

		print("\tPrevious subnet mask:\t",net_subnet_mask,"\t", net_binary_mask[0:8],net_binary_mask[8:16],net_binary_mask[16:24],net_binary_mask[24:32])
		print("\tYour new subnet mask:\t",new_subnet_mask,"\t", new_binary_mask[0:8],new_binary_mask[8:16],new_binary_mask[16:24],new_binary_mask[24:32])

		if new_binary_mask <= net_binary_mask:
			print("\nInvalid mask. The subnet mask must have more 1 bits than current network mask. Please try again...")
		else:
			more_sub_bits = new_no_of_ones - net_no_of_ones
			# print ('new and net = ', new_binary_mask, net_binary_mask)
			print("\nThis is a valid subnet mask because it has", more_sub_bits, "more bit(s) than the current network mask.")
			break
		
	return(new_binary_mask, new_no_of_ones, new_no_of_zeros, new_no_of_hosts, new_subnet_mask)



def display_all_subnets(sum_net_network_address, sum_net_network_address_binary, sum_sub_no_of_ones, sum_net_no_of_ones, sum_sub_no_of_zeros, sum_net_no_of_zeros):

	# print ('\rNetwork:    ',sum_net_network_address,'\t', sum_net_network_address_binary[0:8], sum_net_network_address_binary[8:16], sum_net_network_address_binary[16:24], sum_net_network_address_binary[24:32])

	last_bit = sum_sub_no_of_ones
	subnet_bits = sum_sub_no_of_ones - sum_net_no_of_ones
	first_bit = sum_sub_no_of_ones - (sum_sub_no_of_ones - sum_net_no_of_ones)


	# print ('First and last bit:: ', first_bit,last_bit)
	# print ('Subs:    ', sum_net_network_address_binary[first_bit:last_bit])

	#for value in range(1,subnet_bits**2):
		#print ('Subs:    ', sum_net_network_address_binary[first_bit:last_bit])


	zero_filler = []
	for value in range(0,subnet_bits):
		zero_filler.append(0)
		
	# print ("net + sub ", sum_net_network_address_binary[0:last_bit], sum_net_network_address_binary[first_bit:last_bit])
	# print ('zero filler', zero_filler)

	# Diagnostics
	# Network:     200.44.32.0 	 11001000 00101100 00100000 00000000
	# First and last bit::  20 24
	# Subs:     0000
	# net + sub  110010000010110000100000 0000
	# zero filler [0, 0, 0, 0]


	filler_length = 32 - sum_sub_no_of_zeros
	# filler = 0
	# filler_zeros = filler.zfill(filler_length)
	# print(filler)

	num_sub_bits = sum_sub_no_of_ones - sum_net_no_of_ones 
	subnet_string =  sum_net_network_address_binary[first_bit:last_bit]
	subnet_binary = bin(int(subnet_string)).split("b")[1]
	subnet_binary_fill = subnet_binary.zfill(num_sub_bits)

	hosts_binary_fill = subnet_binary.zfill(sub_no_of_zeros)
	
	# print ('num_sub_bits = ', num_sub_bits)
	# print ('subnet_string =', subnet_string)
	# print ('subnet_binary = ', subnet_binary)
	# print ('subnet_binary_fill = ', subnet_binary_fill)
	# print ('hosts_binary_fill = ', hosts_binary_fill)
	# print ('sum_sub_no_of_zeros = ', sum_sub_no_of_zeros)

	# subnet_binary_fill = subnet_binary_fill + bin(1)
	# print('subnet_binary_fill + 1 =', subnet_binary_fill)

	try:
		input('\nFor a listing of ALL SUBNETS, press any key to continue...')
	except KeyboardInterrupt:
		print('\nExited program')
		sys.exit()

	print ('\nSubnets in dotted decimal and binary')
	print ('Subnets: Common network bits (the same) - Subnet (increment by 1) - Host (all 0s)')
	print ('-----------------------------------------------------------------------------------')

	for x in range(2 ** num_sub_bits):
		# print (sum_net_network_address_binary[0:first_bit], bin(x)[2:].zfill(num_sub_bits), hosts_binary_fill)
		binary_address = sum_net_network_address_binary[0:first_bit] + bin(x)[2:].zfill(num_sub_bits) + hosts_binary_fill
		# print ('binary address = ', binary_address)

		net_ip_octets = []
		for octet in range(0, len(binary_address), 8):
			net_ip_octet = binary_address[octet:octet+8]
			net_ip_octets.append(net_ip_octet)

			#print net_ip_octets

			net_ip_address = []
			for each_octet in net_ip_octets:
				net_ip_address.append(str(int(each_octet, 2)))

			#print net_ip_address

			network_address = ".".join(net_ip_address)
			# print ('network address = ', network_address, sum_net_network_address_binary[0:first_bit], bin(x)[2:].zfill(num_sub_bits), hosts_binary_fill)

		print (network_address, '\t',  sum_net_network_address_binary[0:first_bit], bin(x)[2:].zfill(num_sub_bits), hosts_binary_fill)



##########################################################################
#### MAIN PROGRAM
#### MAJOR NETWORK
##########################################################################

# mode = "a"
sub_flag = 0

# mode = input("\nDo you want (l)earner mode or (a)nswer mode? (l/a)? ")

# Welcome and Instructions
welcome()

print('\nPart 1: Major Network')
print('-----------------------')

##################################################################
## Part 1: Major Network
##################################################################

# Ask the user to enter a valid IPv4 address - return IPv4 address in dotted
user_ipv4_address = enter_ipv4_address()

# Ask the user to enter a valid subnet mask - return subnet mask in dotted
net_subnet_mask = enter_subnet_mask()

# Convert the subnet mask from dotted decimal to binary - return mask in binary, num of ones, zeros, and hosts (These are now values outside the funtion)
net_binary_mask, net_no_of_ones, net_no_of_zeros, net_no_of_hosts = convert_mask_to_binary(net_subnet_mask)

# Convert user entered dotted address to binary
binary_ip = convert_ipv4_to_binary()

# Generate network, first host, last host, broadcast to binary
net_network_address_binary, net_first_host_binary, net_last_host_binary, net_broadcast_address_binary = generate_address_binary(net_no_of_ones, net_no_of_zeros, net_no_of_hosts)

# Convert addresses to dotted decimal
net_network_address, net_first_host_address, net_last_host_address, net_broadcast_address, net_net_ip_address, net_bst_ip_address = convert_addresses_to_dotted(net_network_address_binary, net_first_host_binary, net_last_host_binary, net_broadcast_address_binary)

# if mode in ("l", "L"):

# Display binary network, first host, last host, broadcast addresses
display_addresses_binary(net_binary_mask, net_no_of_ones, net_no_of_zeros, net_no_of_hosts, net_network_address_binary, net_first_host_binary, net_last_host_binary, net_broadcast_address_binary, net_no_of_ones, net_no_of_ones)

# Displaying net , first, last, broadcast in dotted
display_first_last_broadcast_dotted(net_network_address, net_first_host_address, net_last_host_address, net_broadcast_address)

# Generate a random IPv4 address for this subnet
generate_random_ipv4(net_net_ip_address, net_bst_ip_address)

##################################################################
## Part 2: Subnetting
##################################################################

print('\nPart 2: Subnetting (optional)')
print('--------------------------------')

try_subnetting = input("\nDo you want to subnet this network? (y/n)")
if try_subnetting == "n":
	print("\nThanks for learning more about IPv4 addressing!\n")
	exit()

display_major_network(net_network_address, net_network_address_binary, net_subnet_mask, net_binary_mask)

sub_flag = 1

sub_binary_mask, sub_no_of_ones, sub_no_of_zeros, sub_no_of_hosts, sub_subnet_mask = subnet_major_network(net_binary_mask)

# Generate network, first host, last host, broadcast to binary
sub_network_address_binary, sub_first_host_binary, sub_last_host_binary, sub_broadcast_address_binary = generate_address_binary(sub_no_of_ones, sub_no_of_zeros, sub_no_of_hosts)

# Convert addresses to dotted decimal
sub_network_address, sub_first_host_address, sub_last_host_address, sub_broadcast_address, sub_net_ip_address, sub_bst_ip_address = convert_addresses_to_dotted(sub_network_address_binary, sub_first_host_binary, sub_last_host_binary, sub_broadcast_address_binary)

# if mode in ("l", "L"):

# Display binary network, first host, last host, broadcast addresses
display_addresses_binary(sub_binary_mask, sub_no_of_ones, sub_no_of_zeros, sub_no_of_hosts, sub_network_address_binary, sub_first_host_binary, sub_last_host_binary, sub_broadcast_address_binary, net_no_of_ones, sub_no_of_ones)

# Displaying net , first, last, broadcast in dotted
display_first_last_broadcast_dotted(sub_network_address, sub_first_host_address, sub_last_host_address, sub_broadcast_address)

# Generate a random IPv4 address for this subnet
generate_random_ipv4(sub_net_ip_address, sub_bst_ip_address)

###################################################################
# Part 3: Subnet List
####################################################################


print("\nPart 3: Subnet List")
print("-----------------------")

display_all_subnets(net_network_address, net_network_address_binary, sub_no_of_ones, net_no_of_ones, sub_no_of_zeros, net_no_of_zeros)

print ("\nIPv6 is so much easier!\n")


####################################################################
# END OF MAIN PROGRAM
####################################################################