'''create empty dict
use while loop limit 5
    read network alias name from stdin (eg host01)
    read an ip address from stdin (eg 192.168.1.1)
    add input alias and ip address to an existing dict
    network alias key
    ipaddress value
display list host details for loop
read any hostname from stdin
    test input host is exists or not -ignore it
                          | modify ip address-127.0.0.1
                            display updated network details'''
details={}
i=0
while i<2:
    network_alias=input("Enter alias name:")
    ip_address=input("Enter ip address:")
    details[network_alias]=ip_address
    i=i+1

for j in details:
    print(j,details[j])
host=input("Enter hostname:")
if host in details:
    details[host]='127.0.0.1'
    for j in details:
        print(j,details[j])
else:
    print("hostname not exist")

# print(details)