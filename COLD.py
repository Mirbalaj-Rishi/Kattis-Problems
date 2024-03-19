input()
x = input()
count = 0
list = []
for i in x.split():
    list.append(int(i))
for i in list:
    if i < 0:
        count = count + 1
print(count)
