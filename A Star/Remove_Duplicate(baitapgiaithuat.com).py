n = int(input())
i = list(map(int,input().split()))

a = list(dict.fromkeys(i))
a.sort()

for k in a:
    print(k , end=" ")