def selection(arr):
    n = len(arr)
    for i in range(n):
        iMin = i
        for j in range(i+1,n):
            if arr[j]<=arr[iMin]:
                iMin = j
        arr[iMin], arr[i] = arr[i], arr[iMin]
    return arr

a = [3,5,2,6,7,9,8,0,1,2]
print(selection(a))
