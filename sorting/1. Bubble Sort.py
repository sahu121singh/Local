def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr                           # returning the list
    
def bubble_alt(arr):
    n = len(arr)
    done = False
    while(not done):
        done = True
        i = 0
        while(i < n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                done = False
            i+=1
    return arr

l = [2, 7, 4, 1, 5, 3]
print(bubble(l))
print(bubble_alt(l))
