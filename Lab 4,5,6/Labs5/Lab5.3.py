access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

IW = {
    "acces" : access_template,
    "trunk" : trunk_template
}

interface_work = input("Введите режим работы интерфейса (access/trunk): ")
interface_type = input("Введите тип и номер интерфейса: ")
vlans = input("Введите номер влан(ов): ")

print(f"interface {interface_type}")
print('\n'.join(IW[interface_work]).format(vlans))