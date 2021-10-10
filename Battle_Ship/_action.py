

# Trường nhập tọa độ để bắn phá tàu đối phương
def Fight_ship_player(m,n):
    cot = int(input("Please Enter Location To Shoot Ships (from 0 to {:d} in the straight direction):".format(m-1)))
    while cot not in range(m):
        rule = True
        while rule:
            print("You shoot ships outside the play area!")
            cot = input("Please Enter Location To Shoot Ships (from 0 to {:d}):".format(m -1))
            if cot in range(n):
                rule = False
                break    
    hang = int(input("Please Enter Location To Shoot Ships (from 0 to {:d} in the vertical direction):".format(n-1)))
    while hang not in range(n):
        rule = True
        while rule:
            print("You shoot ships outside the play area!")
            hang = input("Please Enter Location To Shoot Ships (from 0 to {:d}):".format(n - 1))
            if hang in range(n):
                rule = False
                break
    return int(hang), int(cot)




# Nhập Tọa độ để đặt tàu
def Approve_Location_To_Set_Ship(m,n , i):
    cot = input("Please Enter Location To Set Ship {:d} (from 0 to {:d} in the horizontal directions):".format(i,m-1))
    while cot not in range(m):
        rule = True
        while rule:
            print("You was set ships outside the play area!")
            cot = input("Please Enter Location To Set Ship (from 0 to {:d}):".format(m-1))
            if cot in range(n):
                rule = False
                break 
    hang = input("Please Enter Location To Set Ship {:d} (from 0 to {:d} in the vertical directions):".format(i, n - 1))
    while hang not in range(n):
        rule = True
        while rule:
            print("You was set ships outside the play area!")
            hang = input("Please Enter Location To Set Ship (from 0 to {:d}):".format(n - 1))
            if hang in range(n):
                rule = False
                break
    return int(hang) , int(cot)




