n = int(input())
k = []

def tong(a,b):
    return str(a+b)
def ao(c , d):
    return str(c+d) + "i"

for i in range(n):
    a , b = list(map(int,input().split()))
    c , d = list(map(int,input().split()))
    m = tong(a,c)
    n = ao(b,d)
    p = m + " + " + n
    k.append(p)

for i in k:
    print(i)