data = [17,12,77,0,8,44]
def selSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
print(selSort(data))