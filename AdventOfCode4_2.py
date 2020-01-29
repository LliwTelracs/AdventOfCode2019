minVal=273025
maxVal=767253

count=0
for i in range(minVal,maxVal):
    if(i==int("".join(sorted([c for c in str(i)])))):
        for j in range(10):
            if(len(str(i).replace(str(j),""))==4):
                count=count+1
                break
print(count)
