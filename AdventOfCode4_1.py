minVal=273025
maxVal=767253

count=0
for i in range(minVal,maxVal):
    if(i==int("".join(sorted([c for c in str(i)]))) and len(set(str(i)))<6):
        print(i)
        count=count+1
