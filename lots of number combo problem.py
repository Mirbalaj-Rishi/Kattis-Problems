


# maybe the pop isn't working as I expected 

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
list = []

addAB = a + b
addBC = c + b
def subrule(a,b):
    if a - b >= 0:
        subAB = a - b
    else:
        subAB = 10000000000000000
    return subAB
def divrule(a,b):
    if b != 0:
        if a%b == 0: 
            divAB = a/b
            divAB = int(divAB)
        else:
            divAB = 10000000
    else:
        divAB = 100000000000
    return divAB

def addrule(a,b):
    c = a + b
    return c
def mutiprule(a,b):
    c = a * b
    return c

A = subrule(subrule(a,b),c)
B = subrule(a,subrule(b,c))
C = subrule(addAB,c)
D = subrule(a,addBC)
E = subrule(a,divrule(b,c))
F = subrule(divrule(a,b),c)
AA = subrule(mutiprule(a,b),c)
AB = subrule(a,mutiprule(b,c))



G = divrule(subrule(a,b),c)
H = divrule(a,subrule(b,c))
I = divrule(addAB,c)
J = divrule(a,addBC)
K = divrule(a,divrule(b,c))
L = divrule(divrule(a,b),c)
BA = divrule(mutiprule(a,b),c)
BB = divrule(a,mutiprule(b,c))

# NEED TO ADD ADDITION AND MUTIPLICATION

M = addrule(subrule(a,b),c)
N = addrule(a,subrule(b,c))
O = addrule(addAB,c)
P = addrule(a,addBC)
Q = addrule(a,divrule(b,c))
R = addrule(a,b)
CA = addrule(mutiprule(a,b),c)
CB = addrule(a,mutiprule(b,c))

S = mutiprule(subrule(a,b),c)
T = mutiprule(a,subrule(b,c))
U = mutiprule(addAB,c)
V = mutiprule(a,addBC)
W = mutiprule(a,divrule(b,c))
X = mutiprule(divrule(a,b),c)
DA = mutiprule(mutiprule(a,b),c)
DB = mutiprule(a,mutiprule(b,c))



list.append(A)
list.append(B)
list.append(C)
list.append(D)
list.append(E)
list.append(F)
list.append(G)
list.append(H)
list.append(I)
list.append(J)
list.append(K)
list.append(L)
list.append(M)
list.append(O)
list.append(P)
list.append(Q)
list.append(R)
list.append(S)
list.append(T)
list.append(U)
list.append(V)
list.append(W)
list.append(X)
list.append(AB)
list.append(AA)
list.append(BB)
list.append(BA)
list.append(CB)
list.append(CA)
list.append(DB)
list.append(DA)


min = 1000000000000
for i in list:
    if i < 0:
        list.pop(i)
    elif i < min:
        min = i

print(min)
    
"""
# supposedly better 
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
list = []

addAB = a + b
addBC = c + b
def subrule(a,b):
    if a - b >= 0:
        subAB = a - b
    else:
        subAB = 10000000000000000
    return subAB
def divrule(a,b):
    if b != 0:
        if a%b == 0: 
            divAB = a/b
            divAB = int(divAB)
        else:
            divAB = 10000000
    else:
        divAB = 100000000000
    return divAB
A = subrule(subrule(a,b),c)
B = subrule(a,subrule(b,c))
C = subrule(addAB,c)
D = subrule(a,addBC)
E = subrule(a,divrule(b,c))
F = subrule(divrule(a,b),c)


G = divrule(subrule(a,b),c)
H = divrule(a,subrule(b,c))
I = divrule(addAB,c)
J = divrule(a,addBC)
K = divrule(a,divrule(b,c))
L = divrule(divrule(a,b),c)


list.append(A)
list.append(B)
list.append(C)
list.append(D)
list.append(E)
list.append(F)
list.append(G)
list.append(H)
list.append(I)
list.append(J)
list.append(K)
list.append(L)

min = 1000000000000
for i in list:
    for i in list:
        if i < 0:
            list.pop(i)
    if i < min:
        min = i

print(min)
    

"""
