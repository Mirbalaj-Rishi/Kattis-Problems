list = ["1","2","3","4","5"]

print(list[3])
list[3] = 3
print(list)

for i in list:
    list[i] = int(list[i])
