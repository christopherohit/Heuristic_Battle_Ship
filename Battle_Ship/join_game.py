from action import Fight_ship_player , Approve_Location_To_Set_Ship , In_Bang_Game
import random

def war_area_background(m , n):
    war_area = []
    for i in range(m):
        war_area.append([])
        for j in range(n):
            war_area[i].append("___")
    return war_area

def battling_on_ocean(a , m ,n,i):
    ban_tau = 0
    mang = ["Yess", "Wao" , "Great" , "So Good" , "OMG" , "Good Hit" , "Amazing" , "Good Job"]
    mangfail = ["OOPS" , "Too Bad" , "Nood" , "Chicken" , "Unlucky"]
    random.choice(mang)
    score = 0
    while ban_tau < 5:     
        print("Chọn vị trí để bắn: ")
        hang , cot = Fight_ship_player()

        if  war_area_background[hang][cot] != ' ':
            print("Bạn đã từng bắn vào vị trí này ")
            ban_tau = ban_tau + 1
            continue

        if a[hang][cot] == 'X':
            print(random.choice(mang))
            if (Fight_ship_player() == Approve_Location_To_Set_Ship(m ,n , i)):
                war_area_background[hang][cot] = 'O' , 'O' , 'O' , 'O' , 'O'
                score = score + 1
                ban_tau = ban_tau + 1
            elif (Fight_ship_player() == Approve_Location_To_Set_Ship(m , n ,i)):
                war_area_background[hang][cot] = 'X' , 'X', 'X' , 'X'
                score = score + 2
                ban_tau = ban_tau + 1
            elif (Fight_ship_player() == Approve_Location_To_Set_Ship(m ,n ,i)):
                war_area_background[hang][cot] = 'X' , 'X' , 'X'
                score = score + 3
                ban_tau = ban_tau + 1
            elif (Fight_ship_player() == Approve_Location_To_Set_Ship(m ,n ,i)):
                war_area_background[hang][cot] = 'X', 'X'
                score = score + 5
                ban_tau = ban_tau + 1
            else:
                war_area_background[hang][cot] = '.'
                print(random.choice(mangfail))
                ban_tau = ban_tau + 1
            In_Bang_Game(a , m , n)
    print("Trò chơi kết thúc")
