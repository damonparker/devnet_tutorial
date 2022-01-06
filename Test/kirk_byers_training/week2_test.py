from pprint import pprint

#Week 2 Exercises
#Uses show_version.txt

#Exercise1
# Open the "show_version.txt" file for reading. 
# Use the .read() method to read in the entire file contents to a variable. 
# Print out the file contents to the screen. 
# Also print out the type of the variable (you should have a string at this point).
# Close the file.
# Open the file a second time using a Python context manager (with statement). 
# Read in the file contents using the .readlines() method. 
# Print out the file contents to the screen. 
# Also print out the type of the variable (you should have a list at this point).

# def read_file():
#     f = open("show_version.txt")
#     output = f.read()
#     print(output)
#     print(type(output))
#     f.close()

#     with open("show_version.txt") as f:
#         output = f.readlines()
#         print(output)
#         print(type(output))
#         print(output1)


# read_file()

#Exercise2
# Create a list of five IP addresses.
# Use the .append() method to add an IP address onto the end of the list. 
# Use the .extend() method to add two more IP addresses to the end of the list.
# Use list concatenation to add two more IP addresses to the end of the list.
# Print out the entire list of ip addresses. 
# Print out the first IP address in the list. 
# Print out the last IP address in the list.
# Using the .pop() method to remove the first IP address in the list and the last IP address in the list.
# Update the new first IP address in the list to be '2.2.2.2'. 
# Print out the new first IP address in the list.

# def ip_list():
#     with open("ip_list.txt") as f:
#         list_ip = f.readlines()
#       
#         list_ip = [line.rstrip() for line in list_ip]
#         print(list_ip)
#         print(type(list_ip))

#         list_ip.append("10.60.3.40")
#         print(list_ip)

#         list_ip.extend(["10.60.3.45", "10.60.3.50"])
#         print(list_ip)

#         secondary_list_ip = ["10.8.9.12", "10.8.9.13"]
#         comb_list = list_ip + secondary_list_ip
#         print(comb_list)
#         print(comb_list[0])
#         print(comb_list[-1])
#         comb_list.pop(0)
#         print(comb_list)
#         comb_list.pop(-1)
#         print(comb_list)
#         comb_list.insert(0, "2.2.2.2")
#         print(comb_list[0])

# ip_list()

#Exercise3
# Read in the "show_arp.txt" file using the readlines() method. 
# Use a list slice to remove the header line.
# Use pretty print to print out the resulting list to the screen, syntax is: 
# from pprint import pprint
# pprint(some_var)
# Use the list .sort() method to sort the list based on IP addresses.
# Create a new list slice that is only the first three ARP entries.
# Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.
# Write this string containing the three ARP entries out to a file named "arp_entries.txt".

# def arp_it():
#     with open("show_arp.txt") as f:
#         output = f.readlines()
#         print(output)
#         output1 = output[1:]
#         pprint(output1)
#         output1.sort()
#         pprint(output1)
#         output2 = output[1:4]
#         print(output2)
#         output3 = "\n".join(output2)
#         new_file = open("arp_entries.txt", "w")
#         new_file.write(output3)
#         new_file.flush
#         print(output3)

# arp_it()

#Exercise4
# Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.
# Obtain the list entry associated with the FastEthernet4 interface. 
# You can just hard-code the index at this point since we haven't covered for-loops or regular expressions. 
# Use the string .split() method to obtain both the IP address and the corresponding interface associated with the IP.
# Create a two element tuple from the result (intf_name, ip_address).
# Print that tuple to the screen.
# Use pycodestyle on this script. 
# Get the warnings/errors to zero. 
# You might need to 'pip install pycodestyle' on your computer (you should be able to type this from the shell prompt). 
# Alternatively, you can type 'python -m pip install pycodestyle'.

# def show_int():
#     with open("show_ip_int_brief.txt", "r") as f:
#         output = f.readlines()
#         print(output)
#         output1 = output[-2].split()
#         print(output1)
#         sh_int = tuple(output1[0:2]) 
#         print(sh_int)
      
#show_int()

#Exercise5

# Read the 'show_ip_bgp_summ.txt' file into your program. 
# From this BGP output obtain the first and last lines of the output.
# From the first line use the string .split() method to obtain the local AS number.
# From the last line use the string .split() method to obtain the BGP peer IP address.
# Print both local AS number and the BGP peer IP address to the screen.

with open("show_ip_bgp_summ.txt") as f:
    bgp_summ = f.read()
bgp_summ = bgp_summ.splitlines()

#print(bgp_summ)

first_line = bgp_summ[0]
#print(first_line)
as_num = first_line.split()[-1]
print("AS Num is {}".format(as_num))

second_line = bgp_summ[-1]
peer_ip = second_line.split()[0]
print("Peer IP is: {}".format(peer_ip))