

oper=""
for k in range(10000):
    for j in range(100):
        inVal="1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,2,10,23,27,1,27,6,31,1,13,31,35,1,13,35,39,1,39,10,43,2,43,13,47,1,47,9,51,2,51,13,55,1,5,55,59,2,59,9,63,1,13,63,67,2,13,67,71,1,71,5,75,2,75,13,79,1,79,6,83,1,83,5,87,2,87,6,91,1,5,91,95,1,95,13,99,2,99,6,103,1,5,103,107,1,107,9,111,2,6,111,115,1,5,115,119,1,119,2,123,1,6,123,0,99,2,14,0,0"
        inVal=list(map(int,inVal.split(",")))
        inVal[1]=k;
        inVal[2]=j;
        for i in range(len(inVal)//4):
            com=inVal[i*4]
            a=inVal[i*4+1]
            b=inVal[i*4+2]
            c=inVal[i*4+3]
            if(c>len(inVal)-1):
                break
            if(com==1):
                inVal[c]=inVal[a]+inVal[b]
                oper+=str(c)+"="+str(a)+"+"+str(b)+","
            if(com==2):
                inVal[c]=inVal[a]*inVal[b]
                oper+=str(c)+"="+str(a)+"*"+str(b)+","
            if(com==99):
                if(inVal[0]==19690720):
                    print(k*100+j)
                break
"""
operations=oper.split(",")[::-1]
for(operation in operations):
    equality=operation.index("=")
    multi=operation.index("*")
    plus=operation.index("+")
    a=operation[:equality]
    b=operation[:
    if(operation.index("*"
    b=operation[operation.index("="):operation.index("*")]

"""


