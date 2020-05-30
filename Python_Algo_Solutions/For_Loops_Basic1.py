# Basic 
def int():
    for i in range(151):
        print(i)
int()

# multiples of 5 
def mult():
    for i in range(5, 1001, 5):
        print(i)
mult()

# Counting, the Dojo Way
def Dojo():
    for i in range(1,101):
        if(i % 10 == 0):
            print("Coding Dojo")
        elif(i % 5 == 0):
            print("Coding")
        else:
            print(i)
Dojo()
# Whoa! Thats Suckers Huge!
def bigNum(num):
    sum = 0
    for i in range(num):
        if (i % 2 != 0):
            sum += i
    print(sum)
bigNum(500000)
# Countdown by fours
def minusFour(num):
    for i in range(num ,0, -4):
        print(i)
minusFour(2018)
# Flexible Counter
def flex(x,y,z):
    for i in range(x , y+1 ):
        if(i % z == 0):
            print(i)
flex(0,75,5)
