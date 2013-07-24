import os
import sys
from math import copysign

def toarray(string):
    return [a for a in string]

def seeker(file, character):
    for a in range(len(file)):
        for b in range(len(file[a])):
            if file[a][b]==character:
                x=b
                y=a
    return y,x

def cost(prv_age, cur_y, cur_x):
    global endcoordinates
    ydist=abs(cur_y-endcoordinates[0])
    xdist=abs(cur_x-endcoordinates[1])
    return (prv_age+ydist+xdist)
    
def generateset(current, frontfile):
    newlist=[]
    coordx=current[1]
    coordy=current[0]
    global counter
    global diagonal
    age=current[3]
    counter+=1
    if(diagonal):
        if(frontfile[coordy-1][coordx+1]==" " or frontfile[coordy-1][coordx+1]=="X"): #up/right
            frontfile[coordy-1][coordx+1]="1" #xy plane quadrant 1
            newlist.append([coordy-1, coordx+1, cost(age, coordy-1, coordx+1), age+1])
        if(frontfile[coordy-1][coordx-1]==" " or frontfile[coordy-1][coordx-1]=="X"): #up/left
            frontfile[coordy-1][coordx-1]="2" #xy plane quadrant 2
            newlist.append([coordy-1, coordx-1, cost(age, coordy-1, coordx-1), age+1])
        if(frontfile[coordy+1][coordx+1]==" " or frontfile[coordy+1][coordx+1]=="X"): #down/right
            frontfile[coordy+1][coordx+1]="4" #xy plane quadrant 4
            newlist.append([coordy+1, coordx+1, cost(age, coordy+1, coordx+1), age+1])
        if(frontfile[coordy+1][coordx-1]==" " or frontfile[coordy+1][coordx-1]=="X"): #down/left
            frontfile[coordy+1][coordx-1]="3" #xy plane quadrant 3
            newlist.append([coordy+1, coordx-1, cost(age, coordy+1, coordx-1), age+1])
    if(frontfile[coordy-1][coordx]==" " or frontfile[coordy-1][coordx]=="X"): #up
        frontfile[coordy-1][coordx]="V"
        newlist.append([coordy-1, coordx, cost(age, coordy-1, coordx), age+1])
    if(frontfile[coordy][coordx+1]==" " or frontfile[coordy][coordx+1]=="X"): #right
        frontfile[coordy][coordx+1]="<"
        newlist.append([coordy, coordx+1, cost(age, coordy, coordx+1), age+1])
    if(frontfile[coordy+1][coordx]==" " or frontfile[coordy+1][coordx]=="X"): #down
        frontfile[coordy+1][coordx]="^"
        newlist.append([coordy+1, coordx, cost(age, coordy+1, coordx), age+1])
    if(frontfile[coordy][coordx-1]==" " or frontfile[coordy][coordx-1]=="X"): #left
        frontfile[coordy][coordx-1]=">"
        newlist.append([coordy, coordx-1, cost(age, coordy, coordx-1), age+1])
    return newlist

counter=0            
maze_file = open(sys.argv[1], "r")
mazebase = maze_file.readlines()
mazebase=[toarray(line[:-1]) for line in mazebase]
finalmap=[thing[:] for thing in mazebase]
startcoordinates = seeker(mazebase, "O")
endcoordinates = seeker(mazebase, "X")
found=False
diagonal=True
print("Checking Path")
agelist=[]
agelist.append([startcoordinates[0], startcoordinates[1], 0, 0])
while((not found) and len(agelist)>0):
    _current=agelist.pop(0)
    agelist+=generateset(_current, mazebase)
    agelist.sort(key=lambda x : x[2])
    if(mazebase[endcoordinates[0]][endcoordinates[1]]!="X"):
        found=True
        radius=_current[3]
print("Solution found!")
location=[endcoordinates[0], endcoordinates[1]]
while(location[0]!=startcoordinates[0] or location[1]!= startcoordinates[1]):
    direction=mazebase[location[0]][location[1]]
    finalmap[location[0]][location[1]]="!"
    if(direction=="<"):
        location[1]-=1
    elif(direction=="^"):
        location[0]-=1
    elif(direction==">"):
        location[1]+=1
    elif(direction=="V"):
        location[0]+=1
    elif(direction=="1"):
        location[0]+=1
        location[1]-=1
    elif(direction=="2"):
        location[0]+=1
        location[1]+=1
    elif(direction=="3"):
        location[0]-=1
        location[1]+=1
    elif(direction=="4"):
        location[0]-=1
        location[1]-=1
finalmap[endcoordinates[0]][endcoordinates[1]]="O"
finalmap[startcoordinates[0]][startcoordinates[1]]="!"
for a in range(len(finalmap)):
    print("".join(finalmap[a]))
radius+=1
print("Length: ",radius)
print("Movement Sets Created: ", counter)
input("")
