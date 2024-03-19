x, y, n = input().split()
x = int(x)
y = int(y)
n = int(n)
u = y * x
for i in range(1,n+1):
    if i % y == 0 and i % x == 0:
        print("FizzBuzz")
    elif i % y == 0:
        print("Buzz")
    elif i % x == 0:
        print("Fizz")
    else:
        print(i)
