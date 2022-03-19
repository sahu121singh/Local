def counting(arr):
    n = len(arr)
    m = max(arr)
    count = [0]*(m+1)
    res = []*n
    for i in range(n):
        count[arr[i]] += 1
    
    print(count, n, m)
    
    for i in range(m+1):
        for j in range(count[i]):
            res.append(i)
            #print(i, end=" ")
    return res
    

l = [2,0, 0,3,4,5,9,2,1,9]
print(counting(l))
