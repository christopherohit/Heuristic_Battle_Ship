from _action import *



while True:
    print("Please enter the length and width of the sea respectively (separated by space):", end= " ")
    m, n = list(map(int,input().split()))
    a = []
    if (m , n <= 10):
        print("This area of war too short so you can't add full ship")
        continue
    else:
        break

def Creat_Background():
    for i in range(m):
        a.append([])
        for j in range(n):
            a[i].append("__")
    return;

# This function display menu play again when this game had gone to over
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

# This definite use to Draw ship on map
def Draw_Ship_On_Map(cot , hang , n):
    c = cot
    while cot < c + (n +1):
        a[hang][cot] = 'X'
        cot += 1

def In_Bang_Game(bando):
    print("  A B C D E F G H I J ")
    print("  +-+-+-+-+-+-+-+-+-+")
    sobat = 1
    for hang in bando:
        print("%d|%s|" % (sobat, "|".join(hang)))
        print("+-+-+-+-+-+-+-+-+-+")
        sobat = sobat + 1

tau3 = 0    
# This function to definite position where ship located
def Position_Ship():
    '''
    In this situation , We have 5 ship: 2 area 2, 
    '''
    for i in range(2,6):
        print("You want to set a train" , i+1 , " at which location?" )
        if (i + 1 == 5):
            hang , cot = Approve_Location_To_Set_Ship()
            Draw_Ship_On_Map(cot , hang , i)
            In_Bang_Game(a)

        elif (i + 1 == 4):
            cot , hang = Approve_Location_To_Set_Ship()
            Draw_Ship_On_Map(cot , hang , i)
            

        elif (i + 1 == 3):
            cot , hang = Approve_Location_To_Set_Ship()
            Draw_Ship_On_Map(cot , hang , i)

        elif (i + 1 == 2):
            cot , hang = Approve_Location_To_Set_Ship()
            Draw_Ship_On_Map(cot , hang , i)

        elif a[hang][cot] == 'X':
            print("This location has been locked by another ship")

Position_Ship()