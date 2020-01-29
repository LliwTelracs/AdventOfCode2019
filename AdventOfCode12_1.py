pos=[[-1,-4,0],[4,7,-1],[-14,-10,9],[1,2,17]]
vel=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]


for step in range(1000):
    velMod=[0,0,0,0]
    for i in range(4):
        xvelmod=0
        yvelmod=0
        zvelmod=0
        for j in range(4):
            if(i==j):
                continue
            xvelmod+=(pos[i][0]<pos[j][0])-(pos[i][0]>pos[j][0])
            yvelmod+=(pos[i][1]<pos[j][1])-(pos[i][1]>pos[j][1])
            zvelmod+=(pos[i][2]<pos[j][2])-(pos[i][2]>pos[j][2])
        velMod[i]=[xvelmod,yvelmod,zvelmod]
    for i in range(4):
        for j in range(3):
            vel[i][j]+=velMod[i][j]
            pos[i][j]+=vel[i][j]
            
    
outVal=0
for i in range(4):
    kin=0
    pot=0
    for j in range(3):
        pot+=abs(pos[i][j])
        kin+=abs(vel[i][j])
    outVal+=kin*pot
print(outVal)
    
