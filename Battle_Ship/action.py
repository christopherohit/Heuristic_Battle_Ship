import random

# Complete To Print't Out the ship on the map
'''Complete'''
'''Hardly Working I don't ensure that it had never have Error in Future but at this time i working very very good'''
'''95% Working'''
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

# Coordinate input function to bombard enemy ships
'''Complete'''
'''Testing Undone'''
'''Calculating'''
def Fight_ship_player(m,n):
    cot = int(input("Please Enter Location To Shoot Ships (from {:d} to {:d} in the straight direction):".format(m//2,m + 1)))
    while cot not in range(m):
        rule = True
        while rule:
            print("You shoot ships outside the play area!")
            cot = input("Please Enter Location To Shoot Ships (from 1 to {:d}):".format(m))
            if cot in range(n):
                rule = False
                break    
    hang = int(input("Please Enter Location To Shoot Ships (from 1 to {:d} in the vertical direction):".format(n)))
    while hang not in range(n):
        rule = True
        while rule:
            print("You shoot ships outside the play area!")
            hang = input("Please Enter Location To Shoot Ships (from 1 to {:d}):".format(n))
            if hang in range(n):
                rule = False
                break
    return int(hang), int(cot)

# Function Input Coordinates to place train
'''Complete'''
'''Test Done'''
'''85% Working'''
def Approve_Location_To_Set_Ship(m,n , i):
    out_range = True
    hang = input("Please Enter Location To Set Ship {:d} (from 1 to {:d} in the Vertical directions):".format(i+1,m))
    while int(hang) not in range(m+1):
        rule = True
        while rule:
            print("You was set ships outside the play area!")
            hang = input("Please Enter Location To Set Ship (from 0 to {:d}):".format(m))
            if int(hang) in range(m+1):
                rule = False
                break
    while out_range:
        # catch the case of placing the train out for each type of ship
        cot = input("Please Enter Location To Set Ship {:d} (from 0 to {:d} in the Horizontal directions):".format(i+1, n //2 -i))
        if (i + 1 == 2):
            #For example, if the ship is two in size, then the maximum distance to place the ship within the allowed range is (m//2 ) - 1
            #And the following cases are progressive
            if int(cot) > (n//2 -1):
                print("You are try to access illegal of competitor and it'sn't allowed to happen so let try again do it at another place")
                continue
            else:
                break
        elif i + 1 == 3:
            if int(cot) > (n//2 -2):
                print("You are try to access illegal of competitor and it'sn't allowed to happen so let try again do it at another place")
                continue
            else:
                break
        elif i + 1 == 4:
            if int(cot) > (n//2 -3):
                print("You are try to access illegal of competitor and it'sn't allowed to happen so let try again do it at another place")
                continue
            else:
                break
        elif i + 1 == 5:
            if int(cot) > (n//2 -4):
                print("You are try to access illegal of competitor and it'sn't allowed to happen so let try again do it at another place")
                continue
            else:
                break
    return int(hang) , int(cot)

# Function create Random Ship


def Random_Ship(m,n , i , a):
    count3 = 0
    for j in range(1,5):
        i += 1
        if i == 2 :
            Draw_Ship_On_Map(n , m, i ,a)
        elif i == 3:
            Draw_Ship_On_Map(n ,m ,i ,a)
            if count3 == 0:
                count3 += 1
                i -= 1
            else:
                continue
        elif i == 4:
            Draw_Ship_On_Map(n, m, i ,a)
        elif i == 5 :
            Draw_Ship_On_Map(n , m , i ,a)


# This definite use to Draw ship on map
'''Complete'''
'''Test Done'''
'''100% Working'''
def Draw_Ship_On_Map(cot , hang , i , a):
    c = cot
    while cot < c + (i +1):
        a[hang-1][cot - 1] = '_X_'
        cot += 1


a = [['_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_'],['_','X','X','X','X','X','_','_','_'],['_','_','_','_','_','_','_','_','_']]
