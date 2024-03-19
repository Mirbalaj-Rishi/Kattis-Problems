x = input()
y = input()
z = x + y 
list = []
for i in z:
    list.append(i)
list.sort(reverse=True)
t = ""
for i in list:
    t = i + t
print(t)
