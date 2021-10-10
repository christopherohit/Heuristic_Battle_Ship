from _action import *


print("Hãy nhập lần lượt chiều dài và rộng của biển(Phân cách nhau bằng dấu cách):", end= " ")
m, n = list(map(int,input().split()))
a = []
def Creat_Background():
    for i in range(m):
        a.append([])
        for j in range(n):
            a[i].append("__")
    return;

def Play_again():
    ans:bool = True
    while ans:
        print("Do you wanna to play it again ?", end= " ")
        ques = input("")
        if ques not in "yYnN":
            continue
        elif ques in "yY":
            return True
        elif ques in "nN":
            ans = False
            print("Thanks for play it")
            return False

def Choose_mode( params: bool = True):
    while params:
        print('[1] Play with Com')
        print('[2] Play with Human')
        print('[3] Com vs Com\n')
        select = input("What is your mode: ")
        if select not in "123" :
            print("This choice is invalid")
            continue
        elif select == "1":
            
            Play_again()
            if Play_again is False: continue 
            else:
                params = False
                continue
        elif select == "2":
            
            Play_again()
            if Play_again: continue 
            else:
                params = False
                continue
        elif select == "3":
            
            Play_again()
            if Play_again: continue 
            else:
                params = False
                continue

# This definite use to Draw 
def Draw_Ship_On_Map(cot , hang , n):
    c = cot
    while cot < c + (n +1):
        a[hang][cot] = 'X'
        cot += 1

def Position_Ship():
    for n in range(2,6):
        print("Bạn muốn đặt tàu " , n+1 , " ở vị trí nào ?" )
        if (n + 1 == 5):
            hang , cot = cung_cap_vi_tri_de_ban()
            Draw_Ship_On_Map(cot , hang , n)


        elif (n + 1 == 4):
            cot , hang = cung_cap_vi_tri_de_ban()
            Draw_Ship_On_Map(cot , hang , n)
            

        elif (n + 1 == 3):
            cot , hang = cung_cap_vi_tri_de_ban()
            Draw_Ship_On_Map(cot , hang , n)

        elif (n + 1 == 2):
            cot , hang = cung_cap_vi_tri_de_ban()
            Draw_Ship_On_Map(cot , hang , n)

        elif a[hang][cot] == 'X':
            print("Vị trí này đã được đặt một tàu khác")

Choose_mode()
