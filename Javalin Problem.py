x = int(input())
list = []
total = 0
minus = 0
for i in range(x):
    y = input()
    y = float(y)
    list.append(y)
for i in list:
    total = i + total
    minus = minus + 1
minus = minus - 1
total = total - minus
print(int(total))
