import os
import sys
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

def generateset(age, locations, frontfile):
    newlist=[]
    global counter
    counter+=1
    if(frontfile[locations[0][0]-1][locations[0][1]]==" " or frontfile[locations[0][0]-1][locations[0][1]]=="X"): #up
        frontfile[locations[0][0]-1][locations[0][1]]="V"
        newlist.append([locations[0][0]-1, locations[0][1]])
    if(frontfile[locations[0][0]][locations[0][1]+1]==" " or frontfile[locations[0][0]][locations[0][1]+1]=="X"): #right
        frontfile[locations[0][0]][locations[0][1]+1]="<"
        newlist.append([locations[0][0], locations[0][1]+1])
    if(frontfile[locations[0][0]+1][locations[0][1]]==" " or frontfile[locations[0][0]+1][locations[0][1]]=="X"): #down
        frontfile[locations[0][0]+1][locations[0][1]]="^"
        newlist.append([locations[0][0]+1, locations[0][1]])
    if(frontfile[locations[0][0]][locations[0][1]-1]==" " or frontfile[locations[0][0]][locations[0][1]-1]=="X"): #left
        frontfile[locations[0][0]][locations[0][1]-1]=">"
        newlist.append([locations[0][0], locations[0][1]-1])
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
agelist.append([location[0], location[1]])
while((not found) and len(agelist)>0):
    maxes=[]
    agelist+=generateset(radius, agelist, mazebase)
    agelist.pop(0)
    if(mazebase[endcoordinates[0]][endcoordinates[1]]!="X"):
        found=True
    radius+=1
    
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
print("Length: ",radius)
print(counter)
input("")
