from point_in_map import Check_Easy_Situation , All_Island_In_Dimension_Matrix
from point_in_map import Fill_Point_In_Map , Display_On_Map, Fill_Island_In_Map, Create_Beach , Total_Distances, Dimension_Matrix
from Compare import Create_Dictionary
import math


# Function input data to calculate
###
'''Completed'''
'''Test Done'''
'''100% Working'''
print('Please enter number of island and Distance which cano can move: ', end= "")
n ,m = list(map(int,input().split()))
x = []
y = []
matrix = []
name_island = {'00': 'Non Island'}
for i in range(n):
    #print('Please enter data for island {:d}'.format(i+1), end=' ')
    a ,b = list(map(int,input().split()))
    x.append(a)
    y.append(b)
###


### Input Location for Main island
'''Completed'''
'''Test Done'''
'''100% Working'''
###
print("Please Enter Location of A Island:", end=" ")
x1 ,y1 = [int(x) for x in input().split()]
island_a = [x1,y1]
print("Please Enter Location of B Island:", end=" ")
x2 ,y2 = list(map(int,input().split()))
island_b = [x2 , y2]
name_island['{}{}'.format(island_a[:1],island_a[:1])] = 'Main Island A'
name_island['{}{}'.format(island_b[:1],island_b[:1])] = 'Main Island B'
###


# Find a maxpoint in map to create Beach
###
max_x = max(x)
max_y = max(y)
if x2 < max_x:
    max_x = x2
if y2 < max_y:
    max_y = y2
###


'''-> Address to Function'''
Create_Beach(matrix, max_y, max_x)
Fill_Island_In_Map(x1 , y1 , matrix)
Fill_Island_In_Map(x2, y2 , matrix)


'''Loop To Fill Small Island'''
for i in range(n):
    Fill_Point_In_Map(x[i],y[i],matrix)


'''Print Location of Island'''
# Output information of all Island
'''Completed'''
'''Test Done'''
'''100% Working'''
for i in range(n):
    print('Location of Island {:d} is X = {:d} , Y = {:d}'.format(i+1,x[i],y[i]))
    Create_Dictionary(x[i] , y[i] , i , name_island)


'''Dimension Matrix'''
# Check Status of All island to Dimension Matrix
'''Completed'''
'''Test Done'''
'''100$ Working'''
d_matrix = Dimension_Matrix(matrix , x1 , y1 , x2 ,y2)
if Check_Easy_Situation(d_matrix) == 0:
    print("Error: This matrix can't resize !!!")
    pass
else:
    matrix = d_matrix
    n = All_Island_In_Dimension_Matrix(matrix)
    for i in y:
        cout = 0
        if i not in range(y1 - 1 , y2):
            x.remove(x[cout])
            y.remove(y[cout])
        else:
            for j in x:
                if i not in range(x1 - 1 , x2):
                    x.remove(x[cout])
                    y.remove(y[cout])
                else:
                    cout += 1


# Check Distance From Island A to Island B if cano have enough petro, will extract result that go straight to that island
Display_On_Map(matrix)
distance = math.sqrt(((x1 - x2)**2) + ((y1-y2)**2))
print("The Distance From A Island to B Island: {:.5f}".format(distance), end=" ")
if distance <= m:
    print("and it's completely go there without stop any island on beach")
    print('The route of cano is From', name_island['{}{}'.format(island_a[:1],island_a[:1])],'to',name_island['{}{}'.format(island_b[:1], island_b[:1])])
    print('And it take {:0.8f} gas, it have residual {:0.8f} gas'.format(distance, m - distance))
else:    
    o = []
    c = []
    # DDF = []
    # Total_Distances(DDF , n , x2 , x , y2 , y)
    r = Total_Distances(n , x1 , x , y1 , y)
    r.sort(reverse= True)
    