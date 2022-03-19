def quicksort(A, p, q):
    if p<q:
        index = partition(A, p, q)
        quicksort(A, p, index-1)
        quicksort(A, index+1, q)

def partition(A, p, q):
    pivot = A[q]
    pindex = p
    for i in range(p,q):
        if A[i] <= pivot:
            A[i], A[pindex] = A[pindex], A[i]
            pindex+=1
    A[pindex], A[q] = A[q], A[pindex]
    return pindex
    
A = [3, 4, 2, 6, 4, 8, 1, 9, 2]
n = len(A)
quicksort(A, 0, n-1)
print(A)
