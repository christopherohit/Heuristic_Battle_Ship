import random
import time

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
    while cot not in "0123456789":
        print("Bạn Bắn ra ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ 0 đến 9):")
    return int(hang), toado(cot)
    

def cung_cap_vi_tri_de_ban5():
    cot = input("Hãy Nhập Vị Trí Để Đặt Tàu 5 (từ A đến J theo hướng thẳng):")
    while cot not in "ABCDEFGHIJ":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ A đến J):")
    hang = input(" Hãy nhập vị trí đặt tàu (Từ 0 - 9 theo hướng nằm ngang):")
    while cot not in "0123456789":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ 0 đến 9):")
    return int(hang) - 5 , toado(cot)

def cung_cap_vi_tri_de_ban4():
    cot = input("Hãy Nhập Vị Trí Để Đặt Tàu 4 (từ A đến J theo hướng thẳng):")
    while cot not in "ABCDEFGHIJ":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ A đến J):")
    hang = input(" Hãy nhập vị trí đặt tàu (Từ 0 - 9 theo hướng nằm ngang):")
    while cot not in "0123456789":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ 0 đến 9):")
    return int(hang) - 4 , toado(cot)

def cung_cap_vi_tri_de_ban3(i = 1):
    
    cot = input("Hãy Nhập Vị Trí Để Đặt Tàu 5 (từ A đến J theo hướng thẳng):")
    while cot not in "ABCDEFGHIJ":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ A đến J):")
    hang = input(" Hãy nhập vị trí đặt tàu (Từ 0 - 9 theo hướng nằm ngang):")
    while cot not in "0123456789":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ 0 đến 9):")
    if (i <= 2 ):
        return int(hang) - 3 , toado(cot)
    else:
        return cung_cap_vi_tri_de_ban3(i + 1)

def cung_cap_vi_tri_de_ban2():
    cot = input("Hãy Nhập Vị Trí Để Đặt Tàu 5 (từ A đến J theo hướng thẳng):")
    while cot not in "ABCDEFGHIJ":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ A đến J):")
    hang = input(" Hãy nhập vị trí đặt tàu (Từ 0 - 9 theo hướng nằm ngang):")
    while cot not in "0123456789":
        print("Bạn đặt tàu ngoài phạm vi khu vực chơi!")
        cot = input("Hãy Nhập Vị Trí Để Đặt Tàu(từ 0 đến 9):")
    return int(hang) - 2 , toado(cot)

def In_Bang_Game(bando):
    print("A B C D E F G H I J ")
    print("+-+-+-+-+-+-+-+-+-+")
    sobat = 1
    for hang in bando:
        print("%d|%s|" % (sobat, "|".join(hang)))
        print("+-+-+-+-+-+-+-+-+-+")
        sobat = sobat + 1

for n in range(5):
    print("Trò chơi bắn tàu chiến giữa biển khơi mênh mông đối diện chúng ta là một kẻ thù khá là mạnh")
    time.sleep(3)
    print("Hãy vận dụng khả năng tiên đoán của Edogawa Conan bên trong bạn để tiêu diệt toàn bộ tàu chiến")
    time.sleep(3)
    print("của đối phương đem lại hòa bình cho nước nhà nhưng thật kì lạ bộ tổng tư lệnh chỉ cho bạn được")
    time.sleep(3)
    print("sử dụng đúng 5 tàu chiến gồm 1 tàu che chắn to 5 đơn vị , 1 tàu hậu phương to 4 đơn vị , 2 tàu")
    time.sleep(3)
    print("Ngư lôi to 3 đơn vị và 1 tàu đại bác to 2 đơn vị. Bạn chỉ có 5 lượt bắn tướng ứng với số tàu bạn")
    time.sleep(3)
    print("sỡ hữu bạn có thể thấy rằng tàu 3 và tàu 2 khá quan trọng vì nó là có thể tấn công được vậy nên khi mất")
    time.sleep(3)
    print("nó đối phương sẽ được một số điểm khá lớn đấy vậy nên hãy vận dụng sự thông thái và khôn ngoan trong")
    time.sleep(3)
    print("việc sắp xếp các tàu và sự Pro của Cô Văn Nan trong việc đoán ra vị trị tàu của đoán phương nhé")
    time.sleep(3)
    print("Chúc các bạn chơi vui vẻ !!!")
    time.sleep(2)
    print("Bạn muốn đặt tàu " , n+1 , " ở vị trí nào ?" )
    if (n + 1 == 5):
        hang , cot = cung_cap_vi_tri_de_ban5()
        bando[hang][cot] = 'X' , 'X' , 'X' , 'X' , 'X'
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
        In_Bang_Game(bando)
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

