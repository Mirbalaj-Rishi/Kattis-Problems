likes = int(input())
days = input()
list = []
for i in days.split():
    list.append(int(i))
print(list)
list = sorted(list)
print(list)

output = 0


for i in range(len(list)):
    print(list[i])
    list1 = 1 + list[i]
    list11 = list[i + 1]
    # need a way to get passed this error - 
    list2 = 2 + list[i]
    list21 = list[i + 2]

    A = list1 == list11
    B = list2 == list21

    
    if list1 == list11:
        print("y")
        output = output + 1
    elif list2 == list21:
        print("y as well")
        output = output + 2
    else:
        print("n")
    print("that is the end of the thingy")
print(output)


#a = x[0]
#b = x[1]
