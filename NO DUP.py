# https://open.kattis.com/problems/nodup
list = []
list2 = []
d = "y"
x = input().split()
for i in x:
    list.append(i)
for i in list:
    b = i
    list2 = list
    list2.remove(i)
    for y in list2:
        if b == y:
            d = "n"
if d == "y":
    print("yes")
elif d == "n":
    print("no")
    
        
        
    
    
    
