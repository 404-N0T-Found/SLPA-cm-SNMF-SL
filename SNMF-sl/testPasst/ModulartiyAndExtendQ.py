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
        tempintLine=map(int,tempInfo)
        temptemp=[]
        for k in tempintLine:
            temptemp.append(k-1)
        dictCOmmunit[i]=temptemp
        i+=1


    return dictCOmmunit

def getAm(fileName,nodeNumber):
    f = open(fileName, "r")
    lines = f.readlines()

    a = np.zeros([nodeNumber,nodeNumber],int)

    for line in lines:
        # arr = map(int,arr)
        tempInfo = line.strip().split("\t")
        a[int(tempInfo[0])-1][int(tempInfo[1])-1]=int(1)
        a[int(tempInfo[1])-1][int(tempInfo[0])-1] = int(1)

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

#com是划分结果
##节点长度的一维向量  111111
def ExtendQ(A,coms,sums,k,o):
    #k-每个节点的度数 o-每个节点属于的社区数
    s = float(2*sums)
    k = sorted(k, key=lambda x: x[0], reverse=False)
    at = 0
    kt = 0
    EQ = 0.0
    for eachc in coms:
        for eachp in coms[eachc]:
            for eachq in coms[eachc]:
                at += A[eachp][eachq] / float(o[eachp]*o[eachq])
                kt += k[eachp][1]*k[eachq][1] / float(o[eachp]*o[eachq])
    EQ = at - kt / s
    return EQ/s

def Q(graph, cluster):
    e = 0.0
    a_2 = 0.0
    cluster_degree_table = {}
    for vtx, adj in graph.edge.iteritems():
        label = cluster[vtx]
        for neighbor in adj.keys():
            if label == cluster[neighbor]:
                e += 1
        if label not in cluster_degree_table:
            cluster_degree_table[label] =0
        cluster_degree_table[label] += len(adj)
    e /= 2 * graph.number_of_edges()

    for label, cnt in cluster_degree_table.iteritems():
        a = 0.5 * cnt / graph.number_of_edges()
        a_2 += a * a

    Q = e - a_2
    return Q

def findEveryK(fileName,nodeNum):
    f = open(fileName, "r")
    lines = f.readlines()

    tempDict=dict()
    for i in range(nodeNum):
        tempDict[i]=set()


    i = 0
    for line in lines:
        # arr = map(int,arr)
        tempInfo = line.strip().split("\t")
        tempDict[int(tempInfo[0])-1].add(int(tempInfo[1])-1)
        tempDict[int(tempInfo[1])-1].add(int(tempInfo[0])-1)

    aimArray=np.zeros([nodeNum,2],int)
    for i in range(nodeNum):
        aimArray[i][0]=i
        aimArray[i][1] = len(tempDict[i])

    return aimArray

def getO(filename,nodeNum):
    f = open(filename, "r")
    lines = f.readlines()
    tempDict=dict()
    for line in lines:
        # arr = map(int,arr)
        tempInfo = line.strip().split(" ")
        for j in tempInfo:
            if int(j)-1 in tempDict:
                tempDict[int(j)-1]+=1
            else:
                tempDict[int(j)-1]=1

    #tempList = np.zeros([1,nodeNum],int)
    tempList=[]
    for i in range(nodeNum):
        tempList.append(1)

    #for i in range(nodeNum-1):
        #tempList[i]=tempDict[i]


    return tempList

if __name__ == '__main__':
    ## Nodes: 1000, Edges: 7775, Weighted: 1

    nodeNum=1000
    bianNum=7775

    communityDict=achiveFormat("convertFormatoutPut_1.1.txt")
    #1000 7631
    a=getAm("network.dat",nodeNum)
    kList=findEveryK("network.dat",nodeNum)
    o=getO("community.dat",nodeNum)


    #tempList=[]
    #for i in range(nodeNum):
        #tempList.append(1)

    #print(Modulartiy(a,communityDict,bianNum,nodeNum))

    print(ExtendQ(a, communityDict, bianNum, kList,o))




