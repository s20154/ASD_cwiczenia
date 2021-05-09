def quickSort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)
    
def partition(A,p,r):
    pivot = A[r]
    smaller = p 
    for j in range(p,r):
        if A[j] <= pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller = smaller + 1          
    A[smaller], A[r] = A[r], A[smaller]
    return smaller
    
A = [0,3,5,1,8,9,4,7,10,0,10,9,3,3,6]
quickSort(A, 0, len(A)-1)
print(A)