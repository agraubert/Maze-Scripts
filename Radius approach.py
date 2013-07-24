import os
import sys
from math import copysign
def toarray(string):
    return [a for a in string]

def seeker(file, character):
    #print("finding")
    for a in range(len(file)):
        for b in range(len(file[a])):
            if file[a][b]==character:
                x=b
                y=a
    return y,x
counter=0

def cost(prv_age, cur_y, cur_x):
    global endcoordinates
    #+abs(cur_y-endcoordinates[0])+abs(cur_x-endcoordinates[1]))
    return (prv_age+abs(cur_y-endcoordinates[0])+abs(cur_x-endcoordinates[1])))
    
def generateset(current, frontfile):
    newlist=[]
    global counter
    age=current[3]
    counter+=1
    if(frontfile[current[0]-1][current[1]]==" " or frontfile[current[0]-1][current[1]]=="X"): #up
        frontfile[current[0]-1][current[1]]="V"
        newlist.append([current[0]-1, current[1], cost(age, current[0]-1, current[1]), age+1])
    if(frontfile[current[0]][current[1]+1]==" " or frontfile[current[0]][current[1]+1]=="X"): #right
        frontfile[current[0]][current[1]+1]="<"
        newlist.append([current[0], current[1]+1, cost(age, current[0], current[1]+1), age+1])
    if(frontfile[current[0]+1][current[1]]==" " or frontfile[current[0]+1][current[1]]=="X"): #down
        frontfile[current[0]+1][current[1]]="^"
        newlist.append([current[0]+1, current[1], cost(age, current[0]+1, current[1]), age+1])
    if(frontfile[current[0]][current[1]-1]==" " or frontfile[current[0]][current[1]-1]=="X"): #left
        frontfile[current[0]][current[1]-1]=">"
        newlist.append([current[0], current[1]-1, cost(age, current[0], current[1]-1), age+1])
    #locations=[thing[:] for thing in newlist]
    return newlist
            
maze_file = open(sys.argv[1], "r")
mazebase = maze_file.readlines()
mazebase=[toarray(line[:-1]) for line in mazebase]
#invisible=[thing[:] for thing in mazebase]
finalmap=[thing[:] for thing in mazebase]
startcoordinates = seeker(mazebase, "O")
endcoordinates = seeker(mazebase, "X")
location=[startcoordinates[0], startcoordinates[1]]
radius=0
found=False
br=False
#invisible[location[0]][location[1]]=str(0)
print("Checking Path")
maximum=(len(mazebase))
maximum*=len(mazebase[0])
agelist=[]
agelist.append([location[0], location[1], 0, 0])
while((not found) and len(agelist)>0):
    maxes=[]
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
finalmap[endcoordinates[0]][endcoordinates[1]]="O"
finalmap[startcoordinates[0]][startcoordinates[1]]="!"
for a in range(len(finalmap)):
    print("".join(finalmap[a]))
radius+=2
print("Length: ",radius)
print(counter)
input("")
