L = input()
D = input()
X = input()

L = int(L)
D = int(D)
X = int(X)
z = 0 
min = 5000000000000
max = -1
list = []
B = D + 1
for c in range(L,B):
    y = str(c)
    list = []
    z = 0
    for i in y:
        list.append(i)
    for i in list:
        i = int(i)
        z = z + i
        print(i)
    if z == X:
        if c < min:
            min = c
            print("New Min")
        if c > max:
            max = c
            print("new max")
print(min)
print(max)
        
