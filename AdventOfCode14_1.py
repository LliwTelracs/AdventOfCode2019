import math

inVal="""4 BFNQL => 9 LMCRF
2 XGWNS, 7 TCRNC => 5 TPZCH
4 RKHMQ, 1 QHRG, 5 JDSNJ => 4 XGWNS
6 HWTBC, 4 XGWNS => 6 CWCD
1 BKPZH, 2 FLZX => 9 HWFQG
1 GDVD, 2 HTSW => 8 CNQW
2 RMDG => 9 RKHMQ
3 RTLHZ => 3 MSKWT
1 QLNHG, 1 RJHCP => 3 GRDJ
10 DLSD, 2 SWKHJ, 15 HTSW => 1 TCRNC
4 SWKHJ, 24 ZHDSD, 2 DLSD => 3 CPGJ
1 SWKHJ => 1 THJHK
129 ORE => 8 KLSMQ
3 SLNKW, 4 RTLHZ => 4 LPVGC
1 SLNKW => 5 RLGFX
2 QHRG, 1 SGMK => 8 RJHCP
9 RGKCF, 7 QHRG => 6 ZHDSD
8 XGWNS, 1 CPGJ => 2 QLNHG
2 MQFJF, 7 TBVH, 7 FZXS => 2 WZMRW
13 ZHDSD, 11 SLNKW, 18 RJHCP => 2 CZJR
1 CNQW, 5 GRDJ, 3 GDVD => 4 FLZX
129 ORE => 4 RHSHR
2 HWTBC, 2 JDSNJ => 8 QPBHG
1 BKPZH, 8 SWKHJ => 6 WSWBV
8 RJHCP, 7 FRGJK => 1 GSDT
6 QPBHG => 4 BKPZH
17 PCRQV, 6 BFNQL, 9 GSDT, 10 MQDHX, 1 ZHDSD, 1 GRDJ, 14 BRGXB, 3 RTLHZ => 8 CFGK
8 RMDG => 6 SGMK
3 CZJR => 8 RTLHZ
3 BFRTV => 7 RGKCF
6 FRGJK, 8 CZJR, 4 GRDJ => 4 BRGXB
4 VRVGB => 7 PCRQV
4 TCRNC, 1 TBVH, 2 FZXS, 1 BQGM, 1 THJHK, 19 RLGFX => 2 CRJTJ
5 RDNJK => 6 SWKHJ
2 FLVC, 2 SLNKW, 30 HWTBC => 8 DLSD
6 TBVH, 3 ZHDSD => 5 BQGM
17 RLGFX => 4 SCZQN
8 SWKHJ => 6 FZXS
9 LZHZ => 3 QDCL
2 ZHDSD => 1 RDNJK
15 FZXS, 3 TPZCH => 6 MQFJF
12 RLGFX, 9 QPBHG, 6 HTSW => 1 BFNQL
150 ORE => 9 BFRTV
2 BFRTV, 2 KLSMQ => 2 RMDG
4 VFLNM, 30 RKHMQ, 4 CRJTJ, 24 CFGK, 21 SCZQN, 4 BMGBG, 9 HWFQG, 34 CWCD, 7 LPVGC, 10 QDCL, 2 WSWBV, 2 WTZX => 1 FUEL
6 RHSHR, 3 RGKCF, 1 QHRG => 6 JDSNJ
3 MQDHX, 2 XGWNS, 12 GRDJ => 9 LZHZ
128 ORE => 6 ZBWLC
9 JDSNJ, 7 RMDG => 8 FLVC
4 DLSD, 12 CZJR, 3 MSKWT => 4 MQDHX
2 BXNX, 4 ZBWLC => 3 QHRG
19 LMCRF, 3 JDSNJ => 2 BMGBG
1 RJHCP, 26 SGMK => 9 HTSW
2 QPBHG => 8 VFLNM
2 RGKCF => 9 SLNKW
3 LZHZ, 2 GRDJ => 2 TBVH
100 ORE => 2 BXNX
4 DLSD, 21 JDSNJ => 8 GDVD
2 QHRG => 2 HWTBC
1 LPVGC, 8 XGWNS => 8 FRGJK
9 FZXS => 7 VRVGB
7 WZMRW, 1 TBVH, 1 VFLNM, 8 CNQW, 15 LZHZ, 25 PCRQV, 2 BRGXB => 4 WTZX"""


inVal=inVal.split("\n")

reactions=[]
for i in range(len(inVal)):
    tmp=inVal[i].split(" => ")
    inputs=tmp[0].split(", ")
    for j in range(len(inputs)):
        tmp2=inputs[j].split(" ")
        inputs[j]=[int(tmp2[0]),tmp2[1]]
    tmp1=tmp[1].split(" ")
    output=[int(tmp1[0]),tmp1[1]]
    reactions.append([inputs,output])



tree=[["ORE",0]]
curNode=0
while(curNode<len(tree)):
    toFind=tree[curNode][0]
    for i in range(len(reactions)):
        for j in range(len(reactions[i][0])):
            if(toFind==reactions[i][0][j][1]):
                maxDepth=0
                for k in range(len(reactions[i][0])):
                    valid=0
                    for l in range(len(tree)):
                        if(tree[l][0]==reactions[i][0][k][1]):
                            valid=1
                            maxDepth=max(maxDepth,tree[l][1])
                    if(valid==0):
                        break
                for k in range(len(tree)):
                    if(reactions[i][1][1]==tree[k][0]):
                        valid=0
                        break
                if(valid==1):
                    tree.append([reactions[i][1][1],maxDepth+1])
    curNode+=1

def sortingFunc(a):
    return -a[1]

tree=sorted(tree,key=sortingFunc)                                
print(tree)

pathing=[["FUEL",1]]
index=0
for index in range(len(tree)):
    toFind=tree[index][0]
    for i in range(len(pathing)):
        if(pathing[i][0]==toFind):
            numReq=pathing[i][1]
            for j in range(len(reactions)):
                if(reactions[j][1][1]==toFind):
                    multi=math.ceil(numReq/reactions[j][1][0])
                    for reactant in reactions[j][0]:
                        inPathing=0
                        for k in range(len(pathing)):
                            if(pathing[k][0]==reactant[1]):
                                inPathing=1
                                pathing[k][1]+=reactant[0]*multi
                        if(inPathing==0):
                            pathing.append([reactant[1],reactant[0]*multi])
                    
        

                                        

