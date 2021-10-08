import numpy as np

n ,m = [int(x) for x in input().split()]
A = [[5,5,4,10,8,6,12,8],[7,5,7,3,9,7,8,5],[10,6,7,8,10,6,5,7]]
C = [0 , 0 , 0]
def Input(n,m , k):
    while k > 0:
        C.append(0)
        k -= 1
    for j in range(m):
        A.append([])
        for i in range(0 , n):
            x = int(input())
            A[j].append(x)
    B = np.array(A)
    return A, B
k = m
def Process():
    for i in range(m):
        for j in range(n):
            w = max(A)
            print(w)
            A.remove(w)
            y = min(C)
            o = y + w
            C.remove(y)
            C.append(o)
            
            
#Input(n,m , k)
Process()
print(round(max(C)))