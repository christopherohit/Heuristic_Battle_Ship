import random
from intro import Intro


#Create map for game Battle Ship (Water)
bando = [
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
]

#tham chiếu đến các cột theo chữ cái, nhưng Python truy cập danh sách theo số. Vì vậy, 
#xác định một từ điển để dịch các chữ cái sang số tương ứng. Lưu ý rằng danh sách Python bắt đầu bằng 0,
#không phải bằng một!

toado = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'I' : 8,
    'J' : 9,
}
def Nguoi_choi_Ban_Tau():
    cot = input("Hãy Nhập Vị Trí Để Bắn Tàu (từ A đến J theo hướng thẳng):")
    while cot not in "ABCDEFGHIJ":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Bắn Tàu(từ A đến J):")
    hang = input(" Hãy nhập vị trí để bắn tàu (Từ 0 - 9 theo hướng nằm ngang):")
    while hang not in "0123456789":
        print("Bạn Bắn ra ngoài phạm vi khu vực chơi!")
        hang = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ 0 đến 9):")
    return int(hang), toado[cot]
    

def cung_cap_vi_tri_de_ban5():
    cot = input("Hãy Nhập Vị Trí Để Đặt Tàu 5 (từ A đến J theo hướng thẳng):")
    while cot not in "ABCDEFGHIJ":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ A đến J):")
    hang = input(" Hãy nhập vị trí đặt tàu (Từ 0 - 9 theo hướng nằm ngang):")
    while hang not in "0123456789":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        hang = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ 0 đến 9):")
    return int(hang) , toado[cot]

def cung_cap_vi_tri_de_ban4():
    cot = input("Hãy Nhập Vị Trí Để Đặt Tàu 4 (từ A đến J theo hướng thẳng):")
    while cot not in "ABCDEFGHIJ":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ A đến J):")
    hang = input(" Hãy nhập vị trí đặt tàu (Từ 0 - 9 theo hướng nằm ngang):")
    while hang not in "0123456789":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        hang = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ 0 đến 9):")
    return int(hang) , toado[cot]

def cung_cap_vi_tri_de_ban3():
    
    cot = input("Hãy Nhập Vị Trí Để Đặt Tàu 3 (từ A đến J theo hướng thẳng):")
    while cot not in "ABCDEFGHIJ":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ A đến J):")
    hang = input(" Hãy nhập vị trí đặt tàu (Từ 0 - 9 theo hướng nằm ngang):")
    while hang not in "0123456789":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        hang = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ 0 đến 9):")
    return int(hang) , toado[cot]


def cung_cap_vi_tri_de_ban2():
    cot = input("Hãy Nhập Vị Trí Để Đặt Tàu 2 (từ A đến J theo hướng thẳng):")
    while cot not in "ABCDEFGHIJ":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ A đến J):")
    hang = input(" Hãy nhập vị trí đặt tàu (Từ 0 - 9 theo hướng nằm ngang):")
    while hang not in "0123456789":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        hang = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ 0 đến 9):")
    return int(hang) , toado[cot]

def In_Bang_Game(cot ,hang , bando):
    print("  A B C D E F G H I J ")
    print("  +-+-+-+-+-+-+-+-+-+")
    sobat = 1
    for hang in bando:
        print("%d|%s|" % (hang, "|".join(cot)))
        print("+-+-+-+-+-+-+-+-+-+")
        sobat = sobat + 1

Intro()
for n in range(1,6):
    print("Bạn muốn đặt tàu " , n+1 , " ở vị trí nào ?" )
    if (n + 1 == 5):
        hang , cot = cung_cap_vi_tri_de_ban5()
        c = cot
        while cot < c + 5:
            bando[hang][cot] = 'X'
            cot += 1
        In_Bang_Game(bando)
    elif (n + 1 == 4):
        cot , hang = cung_cap_vi_tri_de_ban4()
        bando[hang][cot] = 'X' , 'X' , 'X' , 'X'
        In_Bang_Game(bando)
    elif (n + 1 == 3):
        cot , hang = cung_cap_vi_tri_de_ban3()
        bando[hang][cot] = 'X' , 'X' , 'X'
        In_Bang_Game(bando)
    elif (n + 1 == 2):
        cot , hang = cung_cap_vi_tri_de_ban2 ()
        bando[hang][cot] = 'X' , 'X'
        In_Bang_Game(cot , hang , bando)
    elif bando[hang][cot] == 'X':
        print("Vị trí này đã được đặt một tàu khác")
    
    



#làm sạch terminal cho người chơi bắt đầu chơi
print("\n"*50)

bang_doan_tau = [
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
    [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '],
]

# Cho người chơi 5 lượt đoán
ban_tau = 0
mang = ["Yess", "Wao" , "Great" , "So Good" , "OMG" , "Good Hit" , "Amazing" , "Good Job"]
mangfail = ["OOPS" , "Too Bad" , "Nood" , "Chicken" , "Unlucky"]
random.choice(mang)
score = 0
while ban_tau < 5:     
    print("Chọn vị trí để bắn: ")
    hang , cot = Nguoi_choi_Ban_Tau()

    if bang_doan_tau[hang][cot] != ' ':
        print("Bạn đã từng bắn vào vị trí này ")
        ban_tau = ban_tau + 1
        continue

    if bando[hang][cot] == 'X':
        print(random.choice(mang))
        if (Nguoi_choi_Ban_Tau() == cung_cap_vi_tri_de_ban5()):
            bang_doan_tau[hang][cot] = 'X' , 'X' , 'X' , 'X' , 'X'
            score = score + 1
            ban_tau = ban_tau + 1
        elif (Nguoi_choi_Ban_Tau() == cung_cap_vi_tri_de_ban4()):
            bang_doan_tau[hang][cot] = 'X' , 'X', 'X' , 'X'
            score = score + 2
            ban_tau = ban_tau + 1
        elif (Nguoi_choi_Ban_Tau() == cung_cap_vi_tri_de_ban3()):
            bang_doan_tau[hang][cot] = 'X' , 'X' , 'X'
            score = score + 3
            ban_tau = ban_tau + 1
        elif (Nguoi_choi_Ban_Tau() == cung_cap_vi_tri_de_ban2()):
            bang_doan_tau[hang][cot] = 'X', 'X'
            score = score + 5
            ban_tau = ban_tau + 1
        else:
            bang_doan_tau[hang][cot] = '.'
            print(random.choice(mangfail))
            ban_tau = ban_tau + 1


        In_Bang_Game(bang_doan_tau)
    print("Trò chơi kết thúc")
