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
result = list(set(res1) & set(res2))
result.sort()
print(result)

print("-" * 30)

#4.6
print("4.6")
ospf_route = "10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
config = ospf_route.replace(",","").replace("via","").split()
prefix = config[0]
ad = config[1].replace('[','').replace(']','')
next_hop = config[2]
last = config[3]
interface = config[4]
result = "Prefix{:>29}\nAD/Metric{:>20}\nNext-Hop{:>24}\nLast update{:>17}\nOutbound Interface{:>20}".format(prefix,ad,next_hop,last,interface)
print(result)


print("-" * 30)

#4.7
print("4.7")
mac = "AAAA:BBBB:CCCC"
symbols = {'A':10,
           'B':11,
           'C':12}
result = ""
for i in mac.replace(":",""):
    num = symbols[i]
    result += bin(num)
    
result = result.replace("0b","")
print(result)

print("-" * 30)

#4.8
print("4.8")
ip = "192.168.3.1"
numbers = ip.split('.')
print("{:<10}{:<10}{:<10}{:<10}".format(numbers[0],numbers[1],numbers[2],numbers[3]))
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print("{:08b}  {:08b}  {:08b}  {:08b}".format(numbers[0],numbers[1],numbers[2],numbers[3]))
    
