var = input()
list = []
b = 0
c = 0
d = ""
hasA = False

for i in var:
    if i == "a" or hasA == True:
        hasA = True
        d = d + i
print(d)
    
"""
for i in var:
    if i != "a":
        b = b + 1
        c = c + 1 
    if i == "a":
        c = c + 1
        for var in range(b,c):
            print(var)
              
"""        
        
