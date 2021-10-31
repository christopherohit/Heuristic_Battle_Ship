import math

n = int(input())
a = list(map(int , input().split()))
max1 = 0

def sss(i, max1):
    if i <= max1:
        max1 = max1
    else:
        max1 = i
    return max1

for i in range(len(a)):
    try:
        if a[i] < 0 or a[i+1] < 0:
            continue
        else:
            k = str(a[i]) + str(a[i+1])
            max1 = sss(int(k),max1)
    except:
        k = str(a[n-1]) + str(a[0])    
        max1 = sss(int(k), max1)
max1 = str(max1)
for i in max1:
    print(i , end=" ")