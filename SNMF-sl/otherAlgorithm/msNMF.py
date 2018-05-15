#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import time
import math
import  smallWorldMatrix
import controlCommunity
import jaccard
class SNMFSl:
    def __init__(self, input_file,outDieDai):

        f = open(input_file, "r")
        lines = f.readlines()

        tempLine = lines.pop(0).strip().split("\t")

        self.N = int(tempLine.pop(0))
        self.LAMDA = int(tempLine.pop(0))
        #社区数目
        self.mSize=2
        #self.vm=0.3
        #决定是否进行重叠社区发现
        self.aimNumber= self.mSize
        self.aimNumber+=1
        self.kuadu=0.9
        #差距值

        print "N=%d" % self.N
        print "LAMDA=%d" % self.LAMDA

        #self.adjacency_list = []
        #self.node_memory = []

        self.aimM=np.zeros((self.N,self.N))
        self.D = np.zeros((self.N, self.N))

        for line in lines:
            # get all the neighbors of the current node
            tempInfo= line.strip().split("\t");
            self.aimM[int(tempInfo[0])-1,int(tempInfo[1])-1]=1
            self.aimM[int(tempInfo[1])-1,int(tempInfo[0])-1]=1



        for index, value in enumerate(self.aimM):
            self.D[index][index]=sum(value)

        self.L=self.aimM-self.D
        #相关系数
        self.v=abs(np.corrcoef(self.L))

        #self.aimM = smallWorldMatrix.createN(self.aimM, 2, self.N, 0.1,self.D)

        self.aimM=jaccard.getJaccardM(self.aimM,self.N)

        # 求方阵的特征值V和特征向量D
        #temphhh, self.ggg = np.linalg.eig(self.v)

        #self.hhh = np.zeros((self.N, self.N), float)
        #for index, value in enumerate(temphhh):
        #self.hhh[index][index] = value

        #self.DDD = sum(sum(self.v))

        self.W = abs(np.random.random((self.N,self.mSize)))
        self.H = abs(np.random.random((self.mSize, self.N)))

        #set.H=self.W.T

        self.diedai(outDieDai)
        np.isinf(self.W)
        np.isinf(self.H)

        self.w=np.zeros((self.N, self.mSize),float)
        # 归一化
        self.initselfw()

        #for i in range(self.mSize):
         #   self.w[:, i]=np.multiply(self.W[:, i],1/math.sqrt(sum(pow(self.W[:, i]),2)))
        self.x=np.zeros((self.N,self.aimNumber),float)

        #self.W=self.W.T

        controlCommunity.initselfx(self)

        self.outPut()


    def diedai(self,outDieDai):
        #for i in range(200):
            #wh=np.dot(self.W,self.H)

            #H1=np.dot(self.W.T,self.v)
            #H2=np.dot(np.dot(self.W.T,self.W),self.H)
            #self.H=np.multiply(self.H,H1)/H2

            #W1 = np.dot(self.v,self.H.T)
            #W2 = np.dot(np.dot(self.W,self.H),self.H.T)
            #self.W=np.multiply(self.W,W1)/W2

            #z=np.multiply((self.v-wh),(self.v-wh))
            #E=sum(sum(z))
            #outDieDai.append(float(E))

        for i in range(100):

            wi=self.W.shape[0]  #行数
            hi = self.W.shape[1]  #列数

            tempZi=np.dot(self.aimM,self.W)
            tempMu=np.dot(np.dot(2*self.W,self.W.T),self.W)

            for j in range(wi):
                for k in range(hi):
                    self.W[j][k]=self.W[j][k]*(0.5+tempZi[j][k]/tempMu[j][k])

            tempC=np.dot(self.W,self.W.T)
            z=np.multiply((self.aimM-tempC),(self.aimM-tempC))
            E=sum(sum(z))
            outDieDai.append(float(E))
            print("\n")
            print(i)



        where_are_nanW = np.isnan(self.W)
        self.W[where_are_nanW] = 0
        where_are_nanH = np.isinf(self.H)
        self.H[where_are_nanH] = 0
        return

    def initselfw(self):
        for i in range(self.mSize):
            tempPow=0
            for j in range(self.N):
                tempPow+=pow(self.W[j][i],2)
            tempSqrt=math.sqrt(tempPow)
            for j in range(self.N):
                self.w[j][i]=self.W[j][i]/tempSqrt
        return

    def initselfx(self):
        for i in range(self.N):
            self.x[i][0]=i
            self.x[i][1]=0
            tempMax=0
            for j in range(self.mSize):
                if self.w[i][j]>tempMax:
                    self.x[i][1] = j
                    tempMax=self.w[i][j]

    def outPut(self):
        f_out = open("output.txt", "w+")
        for i in range(self.N):
            #f_out.write("Node %d" % self.x[i][0])
            f_out.write("%d" % self.x[i][0])
            f_out.write(" ")
            #f_out.write("{ ")
            for j in range(self.aimNumber-1):
                if(self.x[i][j+1]>=0):
                    f_out.write("%d " % self.x[i][j+1])
                else:
                    break
            #f_out.write("}")
            f_out.write("\n")
        f_out.close()
        return



def main():

    #start_time = time.time()

    outDieDai=[]

    SNM = SNMFSl("karate.txt",outDieDai)

    f_out = open("outPutDieDai_5000.txt", "w+")
    for i in range(len(outDieDai)):
        f_out.write("%f" % outDieDai[i])
        f_out.write("\n")
    f_out.close()

    #end_time = time.time()
    #print("Elapsed time for snmf-sl was %g seconds" % (end_time - start_time))


    return


if __name__ == "__main__":
    main()
