from __future__ import unicode_literals

# ipv6_addr1 = "2001:db8:1234::1"
# IPV6_ADDR2 = "2001:db8:1234::2"
# iPv6_AdDr3 = "2001:db8:1234::3"

# print("")
# print("Is Var1 equal to Var2: {}".format(ipv6_addr1 == IPV6_ADDR2))
# print("Is Var1 equal to Var2: {}".format(ipv6_addr1 != iPv6_AdDr3))
# print("-" * 60)

# show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 
# print(show_version.strip())

# fields = show_version.split()
# model = fields[1]
# serial = fields[2]
# print()

# vendor_cisco = "cisco" in model.lower()
# print("Is the model Cisco: {}".format(vendor_cisco))

# model_881 = "881" in model
# print("Is it a 881: {}".format(model_881))
# print("Model: {}".format(model))
# print("Serial: {}".format(serial))

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

fields = mac1.split()
ip1 = fields[1]
mac1 = fields[3]

fields = mac2.split()
ip2 = fields[1]
mac2 = fields[3]

fields = mac3.split()
ip3 = fields[1]
mac3 = fields[3]

print()
print("{:^20} {:^20}".format("IP ADDRESS", "MAC ADDRESS"))
print("{:^20} {:^20}".format("-" *20, "-" * 20))
print("{:^20} {:^20}".format(ip1, mac1))
print("{:^20} {:^20}".format(ip2, mac2))
print("{:^20} {:^20}".format(ip3, mac3))
print()



