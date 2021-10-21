from Ocean.point_in_map import Check_Easy_Situation
from point_in_map import Fill_Point_In_Map , Display_On_Map, Fill_Island_In_Map, Create_Beach , Total_Distances, Dimension_Matrix
from Compare import Create_Dictionary
import math


# Function input data to calculate
###
print('Please enter number of island and Distance which cano can move: ', end= "")
n ,m = list(map(int,input().split()))
x = []
y = []
matrix = []
name_island = {'00': 'Non Island'}
for i in range(n):
    a ,b = list(map(int,input().split()))
    x.append(a)
    y.append(b)
###

print("Please Enter Location of A Island:", end=" ")
x1 ,y1 = [int(x) for x in input().split()]
print("Please Enter Location of B Island:", end=" ")
x2 ,y2 = list(map(int,input().split()))

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

'''Dimension Matrix'''
d_matrix = Dimension_Matrix(matrix , x1 , y1 , x2 ,y2)
if Check_Easy_Situation(d_matrix) == 0:
    pass
else:
    matrix = d_matrix


'''Print Location of Island'''
for i in range(n):
    print('Location of Island {:d} is X = {:d} , Y = {:d}'.format(i+1,x[i],y[i]))
    Create_Dictionary(x[i] , y[i] , i , name_island)

Display_On_Map(matrix)

distance = math.sqrt(((x1 - x2)**2) + ((y1-y2)**2))

print("The Distance From A Island to B Island: {:.5f}".format(distance), end=" ")
if distance <= m :
    print("and it's completely go there without stop any island on beach")
else:    
    o = []
    c = []
    # DDF = []
    # Total_Distances(DDF , n , x2 , x , y2 , y)
    # Total_Distances(BDF , n , x1 , x , y1 , y)
    # BDF.sort(reverse= True)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
