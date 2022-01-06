#EXERCISE_1
# Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 
# (representing three corresponding IP addresses). 
#Print these three variables to standard output using a single print statement.
# Make your print statement compatible with both Python2 and Python3.
# from __future__ import unicode_literals
# def ip_address():
#     ip_addr1 = "10.60.1.1"
#     ip_addr2 = '10.60.1.2'
#     ip_addr3 = '10.60.1.3'
#     heading = 'IP ADDRESS'

#     ip_list = [ip_addr1, ip_addr2, ip_addr3]
#     print('\n')
#     print('-' * 80)
#     print('{:^20}'.format(heading))
#     for ip in ip_list:
#         print('{:^20}'.format(ip))
#     print('-' * 80)
# ip_address()

#--------------------------------------------------------------------------------------------------

#EXERCISE_2
#Prompt a user to enter in an IP address from standard input. 
# Read the IP address in and break it up into its octets. 
# Print out the octets in decimal, binary, and hex.
# Your program output should look like the following:
#  $ python exercise2.py 
# Please enter an IP address: 80.98.100.240

#     Octet1         Octet2         Octet3         Octet4     
# ------------------------------------------------------------
#       80             98             100            240      
#    0b1010000      0b1100010      0b1100100     0b11110000   
#      0x50           0x62           0x64           0xf0      
# ------------------------------------------------------------
# Four columns, fifteen characters wide, a header column, data centered in the column.

# def format_ip():
#     ip_addr = input('Please enter an IP Address:\n')
#     octets = ip_addr.split('.')
#     heading = ['Octet1', 'Octet2', 'Octet3', 'Octet4']
#     print('{:^15} {:^15} {:^15} {:^15}'.format(*heading))
#     print('-' * 60)
#     print('{:^15} {:^15} {:^15} {:^15}'.format(*octets))
#     print('{:^15} {:^15} {:^15} {:^15}'.format(
#         bin(int(octets[0])), 
#         bin(int(octets[1])), 
#         bin(int(octets[2])), 
#         bin(int(octets[3])))
#     )
#     print('{:^15} {:^15} {:^15} {:^15}'.format(
#         hex(int(octets[0])), 
#         hex(int(octets[1])), 
#         hex(int(octets[2])), 
#         hex(int(octets[3])))
#     )
#     print('-' * 60)
# format_ip()

#--------------------------------------------------------------------------------------------------

#EXERCISE_3
#Create three different variables 
# The first variable should use all lower case characters with underscore ( _ ) as the word separator. 
# The second variable should use all upper case characters with underscore as the word separator. 
# The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.
# Make all three variables be strings that refer to IPv6 addresses.
# Use the from future technique so that any string literals in Python2 are unicode.
# compare if variable1 equals variable2
# compare if variable1 is not equal to variable3

# def ip_comp():

#     ipv6_ipaddr = "7aa7:8eea:5257:b97c:593e:2212:53d4:354d"
#     IPV6_ipaddr = "1c1c:8c2f:c3be:d412:327c:905c:d969:6cbd"
#     Ipv6_IpAddR = "340e:6122:6b36:971c:8874:02ab:936d:6be5"

#     print("Is variable 1 equal to variable 2: {}".format(ipv6_ipaddr == IPV6_ipaddr))
#     print("Is variable 1 equal to variable 3: {}".format(ipv6_ipaddr == Ipv6_IpAddR))

# ip_comp()

#--------------------------------------------------------------------------------------------------

#EXERCISE_4
# Create a show_version variable that contains the following

# show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 
# Remove all leading and trailing whitespace from the string.
# Split the string and extract the model and serial_number from it.
# Check if 'Cisco' is contained in the model string (ignore capitalization).
# Check if '881' is in the model string.
# Print out both the serial number and the model.

# def device_info():
#     show_version = "*0        CISCO881-SEC-K9       FTX0000038X    ".strip()
#     list_version = show_version.split()
#     model = list_version[1]
#     serial = list_version[2]

#     cisco_vendor = 'cisco' in model.lower()
#     print('Checking if model contains Cisco: {}'.format(cisco_vendor))

#     model_num = '881' in model.lower()
#     print('Checking to see if model is 881: {}'.format(model_num))

#     print('Serial Number is: {}'.format(serial))

# device_info()

#EXERCISE_5
#You have the following three variables from the arp table of a router:
# mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
# mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
# mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"
# Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:
#              IP ADDR          MAC ADDRESS
# -------------------- --------------------
#         10.220.88.29       5254.abbe.5b7b
#         10.220.88.30       5254.ab71.e119
#         10.220.88.32       5254.abc7.26aa
# Two columns, 20 characters wide, data right aligned, a header column.

def arp_table():
    mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
    mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
    mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

    mac1_list = mac1.split()
    mac2_list = mac2.split()
    mac3_list = mac3.split()

    print('{:>20} {:>20}'.format('IP ADDR', 'MAC ADDR'))
    print('{:>20} {:>20}'.format('-' * 20, '-' * 20))
    print('{:>20} {:>20}'.format(mac1_list[1], mac1_list[3]))
    print('{:>20} {:>20}'.format(mac2_list[1], mac2_list[3]))
    print('{:>20} {:>20}'.format(mac3_list[1], mac3_list[3]))

arp_table()