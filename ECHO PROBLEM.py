N = int(input())
list = []
for i in range(0,N):
    word = input()
    list.append(word)
print("----------")
for i in list:
    #print(list.index(i))
    #if not list.index(i) // 2 == 0:
     #   print(i)
    if list.index(i) % 2 == 0:
        print(i)
