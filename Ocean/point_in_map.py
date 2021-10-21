import numpy as np
import math


def Dimension_Matrix(matrix , x1 , y1 , x2 ,y2):
    b = []
    for i in range(len(matrix)):
        if i not in range(y1 - 1 , y2):
            continue
        else:
            b.append([])
            for j in range(len(matrix[i])):
                if j not in range(x1-1,x2):
                    continue
                else:
                    if matrix[i][j] == 'O':
                        b[i].append('O')
                    elif matrix[i][j] == 'X':
                        b[i].append('X')
                    else:
                        b[i].append('_')
    return b

# Fill Small island
'''Completed'''
'''Test Done'''
'''100% Working'''
def Fill_Point_In_Map(x , y ,a):
    try:
        a[x-1][y-1] = 'O'
    except:
        pass
    return a
    

# Fill Main Island
'''Completed'''
'''Test Done'''
'''100% Working'''
def Fill_Island_In_Map(y,x,a):
    a[x-1][y-1] = "X"
    return a

# Print out Matrix
'''Completed'''
'''Test Done'''
'''100% Working'''
def Display_On_Map(matrix):
    print(np.array(matrix))


def Total_Distances(BDF , n , x1 , x , y1 ,y):
    for i in range(n):
        c = math.sqrt(((x1 - x[i])**2) + ((y1 - y[i])**2))
        BDF.append(c)
        # "{:d}{:d}".format(x[i], y[i])

# Draw Beach which non-have island
'''Completed'''
'''Test Done'''
'''100% Working'''
def Create_Beach(a , y, x):
    for i in range(y):
        a.append([])
        for j in range(x):
            a[i].append("_")
    return a

# Check Easy situation when it drop into this situation we can do it easily
'''Completed'''
'''Test Done'''
'''100% Working'''
def Check_Easy_Situation(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 'O':
                count += 1
            else:
                continue
    return count