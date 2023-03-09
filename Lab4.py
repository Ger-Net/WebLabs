# 4.1
print("4.1")
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat = nat.replace("Fast","Gigabit")
print(nat)

print("-" * 30)

#4.2
print("4.2")
mac = "AAAA:BBBB:CCCC"
mac = mac.replace(":",".")
print(mac)

print("-" * 30)

#4.3
print("4.3")
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
commands = config.split()
result = commands[-1].split(',')
print(result)

print("-" * 30)

#4.4
print("4.4")
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = list(set(vlans))
result.sort()
print(result)

print("-" * 30)

#4.5
print("4.5")
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
conf1 = command1.split()
res1 = conf1[-1].split(",")
conf2 = command2.split()
res2 = conf2[-1].split(",")
result = list(set(res1) & set(res2)).sort()
print(result)

