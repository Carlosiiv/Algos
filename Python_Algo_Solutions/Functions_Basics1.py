#1 prints out 5
def a():
    return 5
print(a()) #5

#2 5+5=10  Prints 10
def a():
    return 5
print(a()+a()) #10

#3 Returns 5 function ends
def a():
    return 5
    return 10
print(a()) #5

#4 returns 5 funtion ends
def a():
    return 5
    print(10)
print(a()) #5

#5 Prints 5 but doesnt return anything so x = null
def a():
    print(5)
x = a()
print(x) #5

#6 Prints 3 & 5 but since nothing is returned you cant add the two elements together
def a(b,c): 
    print(b+c)
# print(a(1,2) + a(2,3)) 

#7 string plus string  returns 25
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) #25

#8 prints 100 returns 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a()) #100 10

#9 Prints 7 Prints 14 Prints 7 & 14 then adds the two elements that were returned
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) #7
print(a(5,3)) #14
print(a(2,3) + a(5,3)) #7+14= 21

#10 ads 3+5 retunrs 8 and prints
def a(b,c):
    return b+c
    return 10
print(a(3,5)) #8

#11 #500,500,300,500
b = 500
print(b) #500
def a():
    b = 300
    print(b) #300
print(b)#500
a()
print(b) #300

#12 500 500 300 300
b = 500
print(b) #500
def a():
    b = 300
    print(b) #300
    return b
print(b) #500
a()
print(b) #300

b = 500
print(b) #500
def a():
    b = 300
    print(b) #300
    return b
print(b) #500
b=a()
print(b) #300

#14 1 , 3 , 2
def a():
    print(1)#1
    b()#3
    print(2)#2
def b():
    print(3)
a()# <---- call

#15 1 , 3 , 5 , 10
def a():
    print(1)#1
    x = b()#3
    print(x) #5
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)#10