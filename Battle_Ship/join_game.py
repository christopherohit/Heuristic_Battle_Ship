from action import Fight_ship_player , Approve_Location_To_Set_Ship , In_Bang_Game
import random
# Create new war
'''Complete'''
'''Test Done'''
'''100% Working'''
def war_area_background(m , n):
    war_area = []
    for i in range(m):
        war_area.append([])
        for j in range(n):
            war_area[i].append("___")
    return war_area

#Fight To The Ship
'''Complete'''
'''Untest'''
'''Calculating'''
def battling_on_ocean(a , m ,n,i):
    temp_shoot = 0
    Emotion_Winner = ["Yess", "Wao" , "Great" , "So Good" , "OMG" , "Good Hit" , "Amazing" , "Good Job"]
    Emotion_Loser = ["OOPS" , "Too Bad" , "Nood" , "Chicken" , "Unlucky"]
    score = 0
    while temp_shoot < 5:     
        print("Chọn vị trí để bắn: ")
        hang , cot = Fight_ship_player()

        if  war_area_background[hang][cot] != ' ':
            print("Bạn đã từng bắn vào vị trí này ")
            temp_shoot = temp_shoot + 1
            continue

        if a[hang][cot] == 'X':
            print(random.choice(Emotion_Winner))
            if (Fight_ship_player() == Approve_Location_To_Set_Ship(m ,n , i)):
                war_area_background[hang][cot] = 'O' , 'O' , 'O' , 'O' , 'O'
                score = score + 1
                temp_shoot = temp_shoot + 1
            elif (Fight_ship_player() == Approve_Location_To_Set_Ship(m , n ,i)):
                war_area_background[hang][cot] = 'X' , 'X', 'X' , 'X'
                score = score + 2
                temp_shoot = temp_shoot + 1
            elif (Fight_ship_player() == Approve_Location_To_Set_Ship(m ,n ,i)):
                war_area_background[hang][cot] = 'X' , 'X' , 'X'
                score = score + 3
                temp_shoot = temp_shoot + 1
            elif (Fight_ship_player() == Approve_Location_To_Set_Ship(m ,n ,i)):
                war_area_background[hang][cot] = 'X', 'X'
                score = score + 5
                temp_shoot = temp_shoot + 1
            else:
                war_area_background[hang][cot] = '.'
                print(random.choice(Emotion_Loser))
                temp_shoot = temp_shoot + 1
            In_Bang_Game(a , m , n)
    print("Trò chơi kết thúc")
