import os
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

def generateset(age, backfile, frontfile):
    for a in range(len(backfile)):
        for b in range(len(backfile[a])):
            if(backfile[a][b]==str(age)):
                if(frontfile[a-1][b]==" " or frontfile[a-1][b]=="X"): #up
                    frontfile[a-1][b]="V"
                    backfile[a-1][b]=str(age+1)
                if(frontfile[a][b+1]==" " or frontfile[a][b+1]=="X"): #right
                    frontfile[a][b+1]="<"
                    backfile[a][b+1]=str(age+1)
                if(frontfile[a+1][b]==" " or frontfile[a+1][b]=="X"): #down
                    frontfile[a+1][b]="^"
                    backfile[a+1][b]=str(age+1)
                if(frontfile[a][b-1]==" " or frontfile[a][b-1]=="X"): #left
                    frontfile[a][b-1]=">"
                    backfile[a][b-1]=str(age+1)

maze_file = open("maze5.txt", "r")
mazebase = maze_file.readlines()
mazebase=[toarray(line[:-1]) for line in mazebase]
invisible=[thing[:] for thing in mazebase]
finalmap=[thing[:] for thing in mazebase]
startcoordinates = seeker(mazebase, "O")
endcoordinates = seeker(mazebase, "X")
location=[startcoordinates[0], startcoordinates[1]]
radius=0
found=False
br=False
invisible[location[0]][location[1]]=str(0)
print("Checking Path")
maximum=(len(mazebase))
maximum*=len(mazebase[0])
while(not found):
    maxes=[]
    generateset(radius, invisible, mazebase)
    if(mazebase[endcoordinates[0]][endcoordinates[1]]!="X"):
        found=True
    radius+=1
    if(radius>=3+maximum):
        print("BROKEN")
        br=True
        break
if(not br):
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
input("")
