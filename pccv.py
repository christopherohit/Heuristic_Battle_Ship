n , m = list(map(int,input().split(" ")))
a = [] # List of work
k = 0
w = [] # List of worker
while k < m:
   w.append(0)
   k += 1
for i in range(1 ,n+1):
  print('nhap thoi gian cho cong viec',i,': ',end="")
  bv = int(input())
  a.append(bv)
print()
print('Tong thoi gian cua',n,'cong viec: ',sum(a))

k = n

while k > 0:
    s = max(a)
    a.remove(s)
    y = min(w)
    kda = y + s
    w.append(kda)
    w.remove(y)
    k -= 1

print('Thoi gian hoan thanh cua may thu 1 la: ',w[0])
print('Thoi gian hoan thanh cua may thu 2 la: ',w[1])
print('Thoi gian hoan thanh cua may thu 3 la: ',w[2])
print('\n')
print('thoi gian toi da cho viec hoan thanh moi cong viec la:',max(w))