import random
from action import Draw_Ship_On_Map

# hang , cot = 2 , 1
# c = cot
# a = [['_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_'],['_','X','X','X','X','X','_','_','_'],['_','_','_','_','_','_','_','_','_']]
# b = []
# def In_Bang_Game(bando):
#     print("  A B C D E F G H I J ")
#     print("  +-+-+-+-+-+-+-+-+-+")
#     sobat = 1
#     for hang in bando:
#         print("%d|%s|" % (sobat, "|".join(hang)))
#         print("+-+-+-+-+-+-+-+-+-+")
#         sobat = sobat + 1
        
# print(In_Bang_Game(a))

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

i = 2
a = [['_','_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_','_'],['_','X','X','X','X','X','_','_','_'],['_','_','_','_','_','_','_','_','_']]
m = random.randrange(0,4)
n = random.randrange(0,5)
if i == 2:
    coun = 0
    for x in a:
        for y in a[m]:
            if y == 'O' and coun < i:
                break
            elif y == 'O' and coun == i:
                continue
            elif y != 'O':
                coun += 1
            break
        
