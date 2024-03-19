#This program creates shows how to solve a lattice mutiplication problem

#This program was made to solve the problem at this webpage
#https://open.kattis.com/problems/multiplication

global listTotal
global active

def numberSplit(num):
    #this splits the numbers into a list 10 becomes [1,0]
    num = str(num)
    list = []
    for i in num:
        i = int(i)
        list.append(i)
    return list



def stringSize(string):
    #this figures out how big a string is 
    count = 0
    for i in string:
        count +=1
    return count
def divider(list, num):
    # this takes numbers in a list and mutiplies them by a number
    # if the value is greater than 10 the number gets split up with numberSplot
    newList = []
    for i in list:
        listIfLessThan10 = []
        newItem = num*i
        if newItem < 10:
            listIfLessThan10.append(0)
            listIfLessThan10.append(newItem)
            newList.append(listIfLessThan10)
        else:
            newList.append(numberSplit(newItem))
    return newList

def veryTop(string):
    # this dicideds what the top of the lattice will look like
    veryTop = "+"
    for i in range(2,stringSize(string)):
        veryTop += "-"
    veryTop += "+"
    return veryTop

 

def veryTop2(string):
    # this decides what the top of the inner section of the lattice looks like 
    #veryTop = "|"
    veryTop = ""
    for i in string:
        if i == "|":
            veryTop += "+"
        else:
            veryTop += "-"
    #veryTop += "|"
    veryTop = veryTop[2:-2]
    veryTop = "| "+veryTop+" |"
    return veryTop



def recomplier(list, value):
    
    
    topString = ""
    middleString = ""
    bottomString = ""
    t = 0
    global active # this is used to determine if the value has been used before
    active2 = "n" # this is used to figure if an additoanl space is needed later on
    for i in list:
        global listTotal
        firstNumber = listTotal[0] #the first number is used to put the awnser on the lattice
                                #this takes a list and a value to make the middle section of the lattice 
        a = i[0]
        b = i[1]
            #a = str(a)
            #b = str(b)
        if t == 0 and a == firstNumber and active == "n":
            #this adds the first number to the front to the lattice
            bottomString += f"{firstNumber}|/ {b}"
            active = "y"
            active2 = "y"
            listTotal = listTotal[1:] 
        elif t == 0 and active != "n":
            # this puts the next number where it should go
            bottomString += f"{firstNumber}|/ {b}"
            active = "y"
            active2 = "y"
            listTotal = listTotal[1:]
        else:
            bottomString += f"|/ {b}"
        topString += f"|{a} /"
        middleString += "| / "
        t += 1
        

#f"""
#|{a} /|
#| / |
#|/{b} |
#"""
    
    topString = "| "+topString+"| |" 
    middleString = "| "+middleString+f"|{str(value)}|"
    if active2 == "n":
        bottomString = "| "+bottomString+"| |"
    else:
        bottomString = "|"+bottomString+"| |"
    active2 = "n"
    global usefulLine
    usefulLine = veryTop2(topString)
    print(veryTop2(topString))
    print(topString)
    print(middleString)
    print(bottomString)
    


    #this packs everything into a list so that the function can input a list into the calculator function
    returnList = []
    retrunList = [veryTop2(topString),topString,bottomString]
    active = "wont happen"
    
def lastLine(list,):
    #this makes the last line of the lattice
    string = "|"
    for i in list:
        string +="/ "
        string += str(i)
        string +=" "
    string+="   |"
    print(usefulLine)
    print(string)
    print(veryTop(string))

def calculator(listIn,num1,num2):
    # this takes the output from the recompiler function and adds the calulations.
    print("WIP")
    total = num1 * num2
    list = []
    list = numberSplit(total)
    
    
    
    
    
    
    
def latticeFunction(num1, num2):
    # this combines everything and forms a lattice with two numbers 
    topRow = []
    sideRow = []
    #this uses the numbersplit function to lists that will be used to make the top and side row
    topRow = numberSplit(A)
    sideRow = numberSplit(B)
    ### This code makes the top two rows
    topDisplay = "|   "
    for i in topRow:
        i = str(i)
        topDisplay = topDisplay + i + "   "
    topDisplay = topDisplay.rstrip()
    topDisplay += "   |"
    print(veryTop(topDisplay))
    print(topDisplay)
    # This code makes the rest of the lines
    for i in sideRow:
        recomplier(divider(topRow,i),i)
    lastLine(listTotal)
        
        


        
def generalFunction(A,B):
    if A == "" and B == "":
        return ""
    A = int(A)
    B = int(B)
    
    global active
    active = "n"
    global listTotal

    #this calulates the awnser
    total = A * B
    listTotal = []
    listTotal = numberSplit(total) # this seperates the number allowing the list total to be used like a queue
                                    # where numbers are removed as the awnnser gets filled out
    latticeFunction(A,B)  

        


    
while True:
    try:
        A, B = input().split()
    except:
        break

    try:
        A1, B1 = input().split()
    except:
        break
    

    try:
        A2, B2 = input().split()
    except:
        break
    

    try:
        A3, B3 = input().split()
    except:
        break
    

    try:
        A4, B4 = input().split()
    except:
        break
    

    try:
        A5, B5 = input().split()
    except:
        break
    

    try:
        A6, B6 = input().split()
    except:
        break
    

    try:
        A7, B7 = input().split()
    except:
        break
    

    try:
        A8, B8 = input().split()
    except:
        break
    

    try:
        A9, B9 = input().split()
    except:
        break
    

    try:
        A10, B10 = input().split()
    except:
        break
    

    try:
        A11, B11 = input().split()
    except:
        break
    

    try:
        A12, B12 = input().split()
    except:
        break
    

    try:
        A13, B13 = input().split()
    except:
        break
    

    try:
        A14, B14 = input().split()
    except:
        break
    

    try:
        A15, B15 = input().split()
    except:
        break
    

    try:
        A16, B16 = input().split()
    except:
        break
    

    try:
        A17, B17 = input().split()
    except:
        break
    

    try:
        A18, B18 = input().split()
    except:
        break
    

    try:
        A19, B19 = input().split()
    except:
        break
    

    try:
        A20, B20 = input().split()
    except:
        break

while True:
    try:
        generalFunction(A1,B1)
    except:
        break

    try:
        generalFunction(A2,B2)
    except:
        break

    try:
        generalFunction(A3,B3)
    except:
        break

    try:
        generalFunction(A4,B4)
    except:
        break

    try:
        generalFunction(A5,B5)
    except:
        break

    try:
        generalFunction(A6,B6)
    except:
        break

    try:
        generalFunction(A7,B7)
    except:
        break

    try:
        generalFunction(A8,B8)
    except:
        break

    try:
        generalFunction(A9,B9)
    except:
        break

    try:
        generalFunction(A10,B10)
    except:
        break

    try:
        generalFunction(A11,B11)
    except:
        break

    try:
        generalFunction(A12,B12)
    except:
        break

    try:
        generalFunction(A13,B13)
    except:
        break

    try:
        generalFunction(A14,B14)
    except:
        break

    try:
        generalFunction(A15,B15)
    except:
        break

    try:
        generalFunction(A16,B16)
    except:
        break

    try:
        generalFunction(A17,B17)
    except:
        break

    try:
        generalFunction(A18,B18)
    except:
        break

    try:
        generalFunction(A19,B19)
    except:
        break

    try:
        generalFunction(A20,B20)
    except:
        break

