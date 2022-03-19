def Insertion(arr):
    n = len(arr)
    #print(arr)
    for i in range(1, n):
        value = arr[i]
        hole = i
        while hole > 0 and arr[hole-1] > value:
            #print(i, arr)
            arr[hole] = arr[hole-1]
            hole-=1
        arr[hole] = value
        #print(i,' ------------------> ', arr)
    return arr                            # returning the list
    
    
l = [2, 7, 4, 1, 5, 3]
l1 = Insertion(l)
print(l1)



# https://www.youtube.com/watch?v=i-SKeOcBwko

# O(n)  -->  if list is already sorted   <best case>
# O(n**2) --> for unsorted or in reversed odered  <worst and avg case>

# In unsorted, hole start from 1 till n-1
#       1+2+ ...... + n-1 = (n*(n-1))/2
