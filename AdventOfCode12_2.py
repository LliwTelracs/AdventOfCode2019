import copy

initpos=[[-1,-4,0],[4,7,-1],[-14,-10,9],[1,2,17]]
vel=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
pos=copy.copy(initpos)

xInt=0
yInt=0
zInt=0

xInit=[-1,4,-14,1]
yInit=[-4,7,-10,2]
zInit=[0,-1,9,17]

xPos=copy.copy(xInit)
vel=[0,0,0,0]
while(xInt==0 or xInit[0]!=xPos[0] or xInit[1]!=xPos[1] or xInit[2]!=xPos[2] or xInit[3]!=xPos[3] or vel[0]!=0 or vel[1]!=0 or vel[2]!=0 or vel[3]!=0):
    for i in range(4):
        for j in range(4):
            vel[i]+=(xPos[i]<xPos[j])-(xPos[i]>xPos[j])
    for i in range(4):
        xPos[i]+=vel[i]
    xInt+=1

yPos=copy.copy(yInit)
vel=[0,0,0,0]
while(yInt==0 or yInit[0]!=yPos[0] or yInit[1]!=yPos[1] or yInit[2]!=yPos[2] or yInit[3]!=yPos[3] or vel[0]!=0 or vel[1]!=0 or vel[2]!=0 or vel[3]!=0):
    for i in range(4):
        for j in range(4):
            vel[i]+=(yPos[i]<yPos[j])-(yPos[i]>yPos[j])
    for i in range(4):
        yPos[i]+=vel[i]
    yInt+=1


zPos=copy.copy(zInit)
vel=[0,0,0,0]
while(zInt==0 or zInit[0]!=zPos[0] or zInit[1]!=zPos[1] or zInit[2]!=zPos[2] or zInit[3]!=zPos[3] or vel[0]!=0 or vel[1]!=0 or vel[2]!=0 or vel[3]!=0):
    for i in range(4):
        for j in range(4):
            vel[i]+=(zPos[i]<zPos[j])-(zPos[i]>zPos[j])
    for i in range(4):
        zPos[i]+=vel[i]
    zInt+=1

def gcf(a,b):
    while(a>0 and b>0):
        if(a>b):
            a=a%b
        else:
            b=b%a
    return a if a>b else b

def lcm(a,b):
    return a*b//gcf(a,b)

print(lcm(lcm(zInt,xInt),yInt))

