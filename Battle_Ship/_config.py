from action import Fight_ship_player, Approve_Location_To_Set_Ship
from intro import Intro
import _1_To_Com

Intro()
# m is Row
# n is Columns
tau3 = 0

#Create Background
'''Complete'''
'''Test Done'''
def Creat_Background(m ,n):
    for i in range(m):
        a.append([])
        for j in range(n):
            a[i].append("___")

#Input Parameter
'''Complete'''
'''Test Done'''
while True:
    print("Please enter the length and width of the sea respectively (separated by space):", end= " ")
    m, n = list(map(int,input().split()))
    a = []
    if (m < 20 or n < 20):
        print("This area of war too short so you can't add full ship")
        continue
    else:
        Creat_Background(m ,n)
        break

#This function display menu play again when this game had gone to over
'''Complete'''
'''Test Done'''
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

#This Function Display Menu mode choose the game
'''Working'''
'''No Bug or Error untils this time'''
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
            b = []
            Position_Ship()
            # Config Player
            print('\n' * 50)
            Play_again()
            if Play_again is True: continue 
            else:
                params = False
                continue
        elif select == "2":
            Play_again()
            if Play_again is True: continue 
            else:
                params = False
                continue
        elif select == "3":
            Play_again()
            if Play_again is True: continue 
            else:
                params = False
                continue


# This definite use to Draw ship on map
'''Complete'''
'''Test Done'''
def Draw_Ship_On_Map(cot , hang , i):
    c = cot
    while cot < c + (i +1):
        a[hang-1][cot - 1] = '_X_'
        cot += 1


# Complete To Print't Out the ship on the map
'''Complete'''
'''Hardly Working I don't ensure that it had never have Error in Future but at this time i working very very good'''
def In_Bang_Game(bando , n , m):
    for i in range(n+1):
        if i ==1:
            print(" ", i , " ", end=" ")
        elif i in range(2,10):
            print(i," ", end= " ")
        elif i in range(10, 99):
            print(i , end= "  ")
    print()
    sobat = 1
    for hang in bando:
        print("%d|%s|" % (sobat, "|".join(hang)))
        print("+-" * (m+18))
        sobat = sobat + 1
 

# This function to definite position where ship located

def Position_Ship():
    '''
    In this situation , We have 5 ship: 1 area 2, 2 area 3 , 1 area 4 and 1 area 5
    '''
    cout3 = 0
    for i in range(1,6):
        print("You want to set a ship" , i + 1 , " at which location?" )
        if (i + 1 == 5):
            hang , cot = Approve_Location_To_Set_Ship(m ,n ,i)
            Draw_Ship_On_Map(cot , hang , i)
            In_Bang_Game(a , n , m)
        elif (i + 1 == 4):
            hang , cot = Approve_Location_To_Set_Ship(m ,n ,i)
            Draw_Ship_On_Map(cot , hang , i)
            In_Bang_Game(a ,n ,m)
        elif (i + 1 == 3):
            if cout3 == 0:
                hang , cot = Approve_Location_To_Set_Ship(m ,n ,i)
                Draw_Ship_On_Map(cot , hang , i)
                In_Bang_Game(a , n ,m)
                cout3 += 1
                i -= 1
            else:
                hang , cot = Approve_Location_To_Set_Ship(m,n,i)
                Draw_Ship_On_Map(cot , hang , i)
                In_Bang_Game(a ,n ,m)
        elif (i + 1 == 2):
            hang , cot = Approve_Location_To_Set_Ship(m,n,i)
            Draw_Ship_On_Map(cot , hang , i)
            In_Bang_Game(a , n ,m )
        elif a[hang][cot] == 'X':
            print("This location has been locked by another ship")

Choose_mode()