x,y,z = list(map(int,input().split()))
a =[]
a.append(x,y,z)
str = input()
str = str.upper()
b = []
c = []
for i in range(len(str)+1):
    b.append(ord(str[i]))