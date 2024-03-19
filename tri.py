# https://open.kattis.com/problems/tri

x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

def addition(x,y):
    z = x + y
    return z
def subtraction(x,y):
    z = x - y
    return z
def muti(x,y):
    z = x*y
    return z
def div(x,y):
    z = x/y
    z = int(z)
    return z 

def checkIt(x,y,z):
    if addition(x,y) == z:
        print(f"{x}+{y}={z}")
        return x
    elif addition(y,z) == x:
        print(f"{x}={y}+{z}")
        return x
    elif subtraction(x,y) == z:
        print(f"{x}-{y}={z}")
        return x
    elif subtraction(y,z) == x:
        print(f"{x}={y}-{z}")
        return x
    elif muti(x,y) == z:
        print(f"{x}*{y}={z}")
        return x
    elif muti(y,z) == x:
        print(f"{x}={y}*{z}")
        return x
    elif div(x,y) == z:
        print(f"{x}/{y}={z}")
        return x
    elif div(y,z) == x:
        print(f"{x}={y}/{z}")
        return x
    else:
        print("DNW")

checkIt(x,y,z)
    
    
    
        
    
    
