def merge(A, l, mid, r):
    m = mid - l + 1
    n = r - mid
    count = 0
    c1 = l
    L = [0 for i in range(m)]
    R = [0 for i in range(n)]
    for i in range(m):
        L[i] = A[i+l]
    for j in range(n):
        R[j] = A[mid+j+1]
        
    i, j, k = 0, 0, l
    while(i < m and j < n):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
            c1+=1
        else:
            count += (mid -c1 +1)
            A[k] = R[j]
            j += 1 
        k+=1
    
    while(i<m):
        A[k] = L[i]
        i+=1 
        k+=1 
    while(j<n):
        A[k] = R[j]
        k+=1 
        j+=1
    return count
    
def mergesort(A, p, q):
    count = 0
    if p<q:
        m = (p+q)//2
        count += mergesort(A, p, m)
        count += mergesort(A, m+1, q)
        count += merge(A, p, m, q)
    return count

#arr = [12, 11, 0,1,0,5, 23, 45, 2 , 2, 45 , 67,2,  78, 13, 5,5, 6, 7, 9]
#arr = [2, 1, 3, 1 ,2]
#arr = [12, 15, 1, 5, 6, 14, 11]
arr = [3, 5, 7, 11, 9]
n = len(arr)
k = mergesort(arr, 0, n-1)
print(k)

'''
def merge(A, l, mid, r):
    m = mid - l + 1
    n = r - mid
    
    L = [0 for i in range(m)]
    R = [0 for j in range(n)]
    for i in range(m):
        L[i] = A[i+l]
    for j in range(n):
        R[j] = A[mid+j+1]
        
    i, j, k = 0, 0, l
    while(i < m and j < n):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1 
        else:
            A[k] = R[j]
            j += 1 
        k+=1
    
    while(i<m):
        A[k] = L[i]
        i+=1 
        k+=1 
    while(j<n):
        A[k] = R[j]
        k+=1 
        j+=1
'''
