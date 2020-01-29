import copy
import math
inVal="""##.#..#..###.####...######
#..#####...###.###..#.###.
..#.#####....####.#.#...##
.##..#.#....##..##.#.#....
#.####...#.###..#.##.#..#.
..#..#.#######.####...#.##
#...####.#...#.#####..#.#.
.#..#.##.#....########..##
......##.####.#.##....####
.##.#....#####.####.#.####
..#.#.#.#....#....##.#....
....#######..#.##.#.##.###
###.#######.#..#########..
###.#.#..#....#..#.##..##.
#####.#..#.#..###.#.##.###
.#####.#####....#..###...#
##.#.......###.##.#.##....
...#.#.#.###.#.#..##..####
#....#####.##.###...####.#
#.##.#.######.##..#####.##
#.###.##..##.##.#.###..###
#.####..######...#...#####
#..#..########.#.#...#..##
.##..#.####....#..#..#....
.###.##..#####...###.#.#.#
.##..######...###..#####.#"""

inVal=inVal.split("\n")

asteroids=[]


for y in range(len(inVal)):
    for x in range(len(inVal[y])):
        if(inVal[y][x]=="#"):
            asteroids.append([x,y])


links=[]
for i in range(len(asteroids)):
    slopes=[]
    for j in range(i+1,len(asteroids)):
        a=asteroids[i]
        b=asteroids[j]
        if(b[0]-a[0]):
            slope=(b[1]-a[1])/(b[0]-a[0])
        else:
            slope=len(inVal)+1
        if(slope not in slopes):
            links.append([i,j])
            slopes.append(slope)

asteroidCounts=list(map(int,[char for char in "0"*len(asteroids)]))
for i in range(len(links)):
    asteroidCounts[links[i][0]]+=1
    asteroidCounts[links[i][1]]+=1
    
station=asteroidCounts.index(max(asteroidCounts))

radials=[]

for i in range(len(asteroids)):
    if(i==station):
        continue
    x=asteroids[i][0]-asteroids[station][0]
    y=asteroids[station][1]-asteroids[i][1]
    angle=(-math.atan2(y,x)+5*math.pi/2)%(math.pi*2)
    distance=(x**2+y**2)**0.5
    index=0
    if(len(radials)>0):
        while(index<len(radials)):
            if(angle>radials[index][0] or (angle==radials[index][0] and distance>radials[index][1])):
                index+=1
            else:
                break
    radials.insert(index,[angle,distance,i])

prevang=-1
index=0
lasered=-1
for i in range(200):
    if(index>len(radials)):
        index=0
    while(radials[index][0]==prevang):
        index+=1
        if(index>len(radials)):
            index=0
    lasered=radials[index][2]
    prevang=radials[index][0]
    print(radials[index],asteroids[lasered])
    del(radials[index])
    

outVal=asteroids[lasered][0]*100+asteroids[lasered][1]
print(outVal)

    
    


    
