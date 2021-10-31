n = int(input())
s = []

def nhap(n):
    i = list(map(int,input().split()))
    cout(i , n )

def cout(a , n):
    cout = 0
    for i in range(len(a)):
        try:
            if(a[i] + a[i+1] == n):
                cout += 1
        except:
            continue
    return cout
for i in range(n):
    sl , x = list(map(int,input().split()))
    nhap(x)
