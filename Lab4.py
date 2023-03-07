# 4.1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat = nat.replace("Fast","Gigabit")
print(nat)

print("-" * 30)

#4.2
mac = "AAAA:BBBB:CCCC"
mac = mac.replace(":",".")
print(mac)

print("-" * 30)

#4.3
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
commands = config.split()
result = commands[-1].split(',')
print(result)

print("-" * 30)

#4.4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = list(set(vlans))
result.sort()
print(result)