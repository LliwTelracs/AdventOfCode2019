import copy
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
print(max(asteroidCounts))
        
    
