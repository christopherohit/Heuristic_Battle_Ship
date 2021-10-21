from math import sqrt
import numpy as np

def Create_Dictionary(x ,y, i , name_island):
    name_island['{:d}{:d}'.format(x, y)] = 'Island {:d}'.format(i+1)

def Choose_Island(n , x ,y ,m):
    pass

def No_Solution(x1 , y1 , x , y ,m):
    if sqrt((x1 - x)**2 + (y1 - y)**2) > m :
        return True
    else:
        return False

def Calculated_On_D_Matrix(x1 ,y1 ,x2,y2 ,a ,m):
    Total_Approve_petro = 0
    All_Distance = 0
    for i in a:
        