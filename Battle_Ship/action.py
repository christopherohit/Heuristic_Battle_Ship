

# Trường nhập tọa độ để bắn phá tàu đối phương
def Fight_ship_player(m,n):
    cot = int(input("Please Enter Location To Shoot Ships (from 1 to {:d} in the straight direction):".format(m)))
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




# Nhập Tọa độ để đặt tàu
def Approve_Location_To_Set_Ship(m,n , i):
    out_range = True
    hang = input("Please Enter Location To Set Ship {:d} (from 1 to {:d} in the Vertical directions):".format(i+1,m))
    while int(hang) not in range(n):
        rule = True
        while rule:
            print("You was set ships outside the play area!")
            hang = input("Please Enter Location To Set Ship (from 0 to {:d}):".format(n - 1))
            if int(hang) in range(n):
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