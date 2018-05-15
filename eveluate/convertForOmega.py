import os

#for NMI
f = open("community.dat", "r")
lines = f.readlines()


tempList=[]

for line in lines:
    # get all the neighbors of the current node
    tempInfo = line.strip().split(" ");
    tempList.append( map(eval, tempInfo)  )

f_out = open("outPutVonconvertForOmega.txt", "w+")
for i in range(len(tempList)):

    f_out.write("%d" % i)
    f_out.write(" ")

    tempLine=tempList[i]
    for j in tempLine:
        f_out.write("%d" % j)
        f_out.write(" ")

    f_out.write("\n")

f_out.close()