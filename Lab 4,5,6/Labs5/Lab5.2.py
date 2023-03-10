#5.2
info = input("Введите ip сеть в формате: xxx.xxx.xxx.xxx/xx \n")
info = info.split('/')
network = info[0]
mask = info[1]

numbers = network.split('.')
print("Network:")
print("{:<10}{:<10}{:<10}{:<10}".format(numbers[0],numbers[1],numbers[2],numbers[3]))
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print("{:08b}  {:08b}  {:08b}  {:08b}".format(numbers[0],numbers[1],numbers[2],numbers[3]))

print("Mask:")
print(f"/{mask}")
mask = int(mask)
zero = 32 - mask
binmask = "1" * mask + "0" * zero
n = 8
binmask = [binmask[i:i+n] for i in range(0, len(binmask), n)]
print("{:<10}{:<10}{:<10}{:<10}".format(int(binmask[0],2),int(binmask[1],2),int(binmask[2],2),int(binmask[3],2)))
print("{:<8}  {:<8}  {:<8}  {:<8}".format(binmask[0],binmask[1],binmask[2],binmask[3]))