import os

#for NMI
f = open("output.txt", "r")
lines = f.readlines()


tempDict=dict()

for line in lines:
    # get all the neighbors of the current node
    tempInfo = line.strip().split(" ");
    tempInt1=int(tempInfo[0])
    tempInt2 = int(tempInfo[1])
    if tempInt2 in tempDict.keys():
        tempList=tempDict[tempInt2]
        tempList.append(tempInt1)
    else:
        tempList=[]
        tempList.append(tempInt1)
        tempDict[tempInt2]=tempList

f_out = open("outPutVonconvert.txt", "w+")
for i in tempDict:

    f_out.write("%d" % i)
    f_out.write(" ")

    tempList=tempDict[i]
    for j in tempList:
        tempj=int(j)
        f_out.write("%d" % tempj)
        f_out.write(" ")
    f_out.write("\n")
f_out.close()