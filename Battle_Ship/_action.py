

# Trường nhập tọa độ để bắn phá tàu đối phương
def Fight_ship_player(m,n):
    cot = int(input("Hãy Nhập Vị Trí Để Bắn Tàu (từ 0 đến {:d} theo hướng thẳng):".format(m-1)))
    while cot not in range(m):
        rule = True
        while rule:
            print("Bạn bắn tàu ngoài phạm vi khu vực chơi!")
            cot = input("Hãy Nhập Vị Trí Để Bắn Tàu(từ 0 đến {:d}):".format(m -1))
            if cot in range(n):
                rule = False
                break    
    hang = int(input("Hãy nhập vị trí để bắn tàu (Từ 0 - {:d} theo hướng nằm ngang):".format(n-1)))
    while hang not in range(n):
        rule = True
        while rule:
            print("Bạn Bắn ra ngoài phạm vi khu vực chơi!")
            hang = input("Hãy Nhập Vị Trí Để bắn Tàu(từ 0 đến {:d}):".format(n - 1))
            if hang in range(n):
                rule = False
                break
    return int(hang), int(cot)




# Nhập Tọa độ để đặt tàu
def cung_cap_vi_tri_de_ban(m,n , i):
    cot = input("Hãy Nhập Vị Trí Để Đặt Tàu {:d} (từ 0 đến {:d} theo hướng thẳng):".format(i,m-1))
    while cot not in range(m):
        rule = True
        while rule:
            print("Bạn bắn tàu ngoài phạm vi khu vực chơi!")
            cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ 0 đến {:d}):".format(m-1))
            if cot in range(n):
                rule = False
                break 
    hang = input(" Hãy nhập vị trí đặt tàu {:d} (Từ 0 - {:d} theo hướng nằm ngang):".format(i, n - 1))
    while hang not in range(n):
        rule = True
        while rule:
            print("Bạn Đặt ra ngoài phạm vi khu vực chơi!")
            hang = input("Hãy Nhập Vị Trí Để đặt Tàu(từ 0 đến {:d}):".format(n - 1))
            if hang in range(n):
                rule = False
                break
    return int(hang) , int(cot)




Fight_ship_player(9 , 9)