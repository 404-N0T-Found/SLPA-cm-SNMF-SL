#coding=utf-8
import numpy as np
import time
import copy



def achiveFormat(fileName):
    f = open(fileName, "r")
    lines = f.readlines()

    dictCOmmunit=dict()
    i=0
    for line in lines:
        # arr = map(int,arr)
        tempInfo=line.strip().split(" ")
        dictCOmmunit[i]=map(int,tempInfo)
        i+=1

    return dictCOmmunit

def getAm(fileName,nodeNumber):
    f = open(fileName, "r")
    lines = f.readlines()

    a = np.array([nodeNumber,nodeNumber],int)

    for line in lines:
        # arr = map(int,arr)
        tempInfo = line.strip().split(" ")
        a[int(tempInfo[0])][int(tempInfo[1])]=1
        a[int(tempInfo[1])][int(tempInfo[0])] = 1

    return a

# A是邻接矩阵
#com是划分结果
#sums是边的数量
#vertices nodeNumber
def Modulartiy(A, coms, sums,vertices):
    Q = 0.0
    for eachc in coms:
        li = 0
        for eachp in coms[eachc]:
            for eachq in coms[eachc]:
                li += A[eachp][eachq]
        li /= 2
        di = 0
        for eachp in coms[eachc]:
            for eachq in range(vertices):
                di += A[eachp][eachq]
        Q = Q + (li - (di * di) /(sums*4))
    Q = Q / float(sums)
    return Q

#k是重叠社区标签
##节点长度的一维向量  111111
def ExtendQ(A,coms,sums,k,o):
    #k-每个节点的度数 o-每个节点属于的社区数
    EQ = 0.0
    for eachc in coms:
        for eachp in coms[eachc]:
            for eachq in coms[eachc]:
                EQ += (A[eachp][eachq] - k[eachp][1]*k[eachq][1]/(2*sums)) / (o[eachp]*o[eachq])
    EQ = EQ / float(2*sums)
    return EQ

if __name__ == '__main__':
    nodeNum=0
    bianNum=0

    communityDict=achiveFormat("community.dat")
    a=getAm("",nodeNum)

    tempList=[]
    for i in range(nodeNum):
        tempList.append(1)

    print(Modulartiy(a,communityDict,bianNum,nodeNum))

    print(ExtendQ(a, communityDict, bianNum, nodeNum))




