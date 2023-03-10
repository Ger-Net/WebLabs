ip = input("Введите адресс в формате xxx.xxx.xxx.xxx: ")

while ip.count(".") != 3:
    print("Неправильный IP-адрес")
    ip = input("Введите адресс в формате xxx.xxx.xxx.xxx: ")
    
ip = ip.split(".")
for i in ip:
    while True:
        if i.isdigit() != True or int(i) < 0 or int(i) > 255:
            print("Неправильный IP-адрес")
            ip = input("Введите адресс в формате xxx.xxx.xxx.xxx: ")
        else:
            break

if ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
elif 1 <= int(ip[0]) <= 223:
    print("unicast")
elif 224 <= int(ip[0]) <= 239:
    print("multicast")
else:
    print("unused")