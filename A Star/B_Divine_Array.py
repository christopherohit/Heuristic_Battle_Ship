m , n , k = list(map(int,input().split()))
if m >= n :
    print(int(((m/2)+n - k)/2))
else:
    print(int(((m/2))))