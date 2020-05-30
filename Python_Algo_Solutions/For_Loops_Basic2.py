# Biggie Size
def sz(arr):
    for i in range(len(arr)):
        if(arr[i] > 0):
            arr[i] = 'Big'
    return arr
print(sz([-10,30,50,-15]))

# Count Positives
def positives(arr):
    count = 0
    for i in range(len(arr)):
        if ( arr[i] > 0):
            count += 1
    arr[i] = count
    return arr
print(positives([-10,15,20,-5]))

# Sum total 
def add(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
print(add([500,10,20,20,50]))

# Avg 
def avg(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    avg = sum / len(arr)
    return avg
print(avg([10,20,30]))

#   length
def length(arr):
    count = 0
    for i in range(len(arr) + 1):
        count = i
    return count
print(length([5,10,15]))

# min
def min(arr):
    if(arr == []):
        return False
    else:
        sm = arr[0]
        for i in range(1,len(arr)):
            if( arr[i] < sm):
                sm = arr[i]
        return sm
print(min([10,20,15,-12,9]))

# max
def max(arr):
    if(arr == []):
        return False
    else:
        lg = arr[0]
        for i in range (1, len(arr)):
            if( arr[i] > lg):
                lg = arr[i]
        return lg
print(max([10,20,15,-12,9]))

#ultimate analysis
def ult(arr):
    sum = 0
    min = arr[0]
    max = arr[0]
    for i in range(len(arr)):
        sum += arr[i]
        if ( arr[i] < min):
            min = arr[i]
        if ( arr[i] > max):
            max = arr[i]
    avg = sum / len(arr)
    ultimate_dictionary = {
        'sumTotal': sum,
        'average': avg,
        'minimum': min,
        'maximum': max,
        'length': len(arr)
    }
    return ultimate_dictionary
print(ult([37,2,1,-9]))

#reverse list
def rev(arr):
    for i in range( 0 , int(len(arr)/2), 1):
        temp = arr[i]
        arr[i] = arr[len(arr)-i-1]
        arr[len(arr)-i-1] = temp
    return arr
print(rev([5,4,3,2,1,]))