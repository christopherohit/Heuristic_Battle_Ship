i = list(map(int,input().split()))
a = i[:-1]
s = i[-1]
cout = 0
for j in range(len(a)):
    if a[j] == s:
        print(j + 1,end=" ")
        cout += 1
if cout == 0:
    print(-1)
