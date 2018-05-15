#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import time
import operator

def initselfx(SNMFSl):
    tempx = np.zeros((SNMFSl.N, SNMFSl.aimNumber), float)

    for i in range(SNMFSl.N):
        tempMatrix=np.zeros((SNMFSl.mSize,SNMFSl.mSize),float)

        SNMFSl.x[i][0] = i
        tempx[i][0]=i


        for j in range(SNMFSl.mSize):
            tempMatrix[j][1]=SNMFSl.w[i][j]
            tempMatrix[j][0] = j
        idex=np.lexsort([-1*tempMatrix[:,1]])

        #如果想重叠社区
        # tempx[i][j+1]  =idex[0]
        #如果想单个社区
        tempx[i][j] = idex[0]

        for j in range(SNMFSl.mSize):
            if j+1 >= SNMFSl.aimNumber:
                break
            tempx[i][j+1] = idex[j]
            temp1=tempMatrix[idex[j]][1]
            temp2=tempMatrix[idex[0]][1]* SNMFSl.kuadu
            if tempMatrix[idex[j]][1]  >= tempMatrix[idex[0]][1]* SNMFSl.kuadu:

                SNMFSl.x[i][j+1] = idex[j]
            else:
                SNMFSl.x[i][j+1] = -1
                break
    control(SNMFSl,tempx)


    #for i in range(SNMFSl.N):
        #SNMFSl.x[i][0] =i
        #SNMFSl.x[i][1] =0
        #tempMax =0
        #for j in range(SNMFSl.mSize):
            #if SNMFSl.w[i][j] >tempMax:
                #SNMFSl.x[i][1] = j
               # tempMax =SNMFSl.w[i][j]


def control(SNMFSl,tempx):
    #以排序的结果为准
    #当某节点隶属于两个社区重要性接近的时候，采用小世界网络中的连接强度

    #for temp in SNMFSl.x:

    return


def sort_by_value(d):

    items=d.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort()
    return [ backitems[i][1] for i in range(0,len(backitems))]
