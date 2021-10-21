n , m = list(map(int,input().split(" ")))
a = [] # List of Work
w = [] # List of Worker
time = []
def Nhapk():
    k = 0
    # code nay cho 2 cau a va b 
    # neu lam cau a de nguyen code ma chay
    # neu lam cau b thi bo phan comment code va chuyen k < m thanh k <= m
    while k <= m:
        w.append(1)
        k += 1
    for i in range(1 ,n+1):
        print('nhap so trang cho luan van',i,': ',end="")
        bv = int(input())
        a.append(bv)
    print()
    print('Tong so trang cua',n,'luan van: ',sum(a))
def Select():
    k = n
    while k > 0:
        s = max(time)
        time.remove(s)
        y = min(w)
        if y == w[0]:
            s = s * 2
            kda = y + s
            w.insert(0,kda)
            w.remove(y)
            k -= 1
        else:
            kda = y + s
            w.append(kda)
            w.remove(y)
            k -= 1
Nhapk()
for i in a:
    c = float(i/8)
    time.append(c)
Select()
for i in range(0,len(w)):
    # if(i == 0):
    #     print('Thoi gian hoan thanh cua quan li la: ',w[i]-1)
    # else:
        print('Thoi gian hoan thanh cua nhan vien',i+1, 'la: ',w[i] - 1)
print()
print('thoi gian toi da cho viec hoan thanh moi cong viec la:',round(max(w)) - 1)