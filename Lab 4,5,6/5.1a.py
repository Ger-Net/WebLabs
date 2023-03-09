#5.1a
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
name = input("Введите имя устройства: r1 r2 sw1\n")
while(name not in "r1 r2 sw1"):
    name = input("Введите имя устройства: r1 r2 sw1")
p = input(f"Введите параметр:\n")
while(p not in "location vendor model ios ip vlans routing"):
    p = input("Введите параметр:\n")

print(london_co[name].get(p))

