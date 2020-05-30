# countdown
def countd(num):
    count = []
    for i in range(num , -1 ,-1):
        count.append(i)
    return count
print(countd(10))

# print & return
def pnr(x,y):
    print(x)
    return y
print(pnr(1,2))

#first plus length
def fpl(arr):
    y = 0
    for i in range (len(arr)):
        y = arr[i] + len(arr)
        return y
print(fpl([5,6,7,8]))

# values greater than second
def vg(arr):
    newarr = []
    for i in range(len(arr)):
        if(arr[i] > arr[1]):
            newarr.append(arr[i])
    print(newarr)
vg([10,20,30,40,50])

# lv
def lv(x,y):
    arr = []
    for i in range(0 , y , 1):
        arr.append(x)
    return arr
print(lv(4,5))