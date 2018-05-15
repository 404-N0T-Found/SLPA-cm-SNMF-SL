#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
import networkx as nx
import numpy as np

#slpa讨论一下有向带权问题
class ClusterRank:
    #一维记录节点编号
    #二维记录邻居节点数目
    #三维记录聚集系数
    #四维记录邻居节点的kout累计和
    def __init__(self,nodeSize,adjacency_list,LAMDA):
       # print(type(adjacency_list))
        tempAdjacency_list=list()

        i=0
        while i<LAMDA:
            adjacency_list.append([adjacency_list[i][1],adjacency_list[i][0]])

            #如果无向
            #adjacency_list.append([adjacency_list[i][0],adjacency_list[i][1]])

            i=i+1


        self.rankList = np.zeros((nodeSize,5),float)
        i=0
        while i<nodeSize:
            self.rankList[i][0]=i+0.0
            i=i+1
        for i in adjacency_list:
            tempInt=i[0];
            self.rankList[tempInt-1][1]=self.rankList[tempInt - 1][1]+1
            self.rankList[i[1]-1][1] = self.rankList[i[1]-1][1] + 1
        self.ClusteringCoefficient()
        self.koutClusterRank(adjacency_list)

        self.vueCLusterRank()

        #self.rankList[np.lexsort(self.rankList.T)]
        #sorted(student_tuples, key=lambda student: student[2])

        #sorted(self.rankList,key=lambda x:x[1])
        self.clusterSort(0,nodeSize-1)

        inti=0;

    def ClusteringCoefficient(self):
        for tempNode in self.rankList:
            #tempMark=tempNode[0]
            tempSize=tempNode[1]
            if tempSize==1:
                tempNode[2]=1
            else:
                tempNode[2]=2*tempSize/(tempSize*(tempSize-1))
        return

    def koutClusterRank(self,adjacency_list):
        for tempNode in adjacency_list:
            self.rankList[tempNode[0]-1][3]+=self.rankList[tempNode[1]-1][1]+1
        return

    def vueCLusterRank(self):
        for tempNode in self.rankList:
            tempKey=tempNode[2]
            tempNode[4]=pow(10,-1*tempKey)*tempNode[3]
        return

    def parttion(self,left, right):
        key = self.rankList[left]

        key0=key[0]
        key4=key[4]

        low = left
        high = right
        while low < high:
            while (low < high) and (self.rankList[high][4] >= key4):
                high -= 1
            self.rankList[low] = self.rankList[high]
            while (low < high) and (self.rankList[low][4] <= key4):
                low += 1
            self.rankList[high] = self.rankList[low]
            self.rankList[low][0] = key0
            self.rankList[low][4] = key4
        return low

    def clusterSort(self, left, right):
        if left < right:
            p = self.parttion(left, right)
            self.clusterSort(left, p - 1)
            self.clusterSort(p + 1, right)
