import numpy as np
import math

def createN(V,characteristicPathLength,N,passt,MARKLIST,wii):
    temp = np.zeros([N,N,characteristicPathLength])
    for j in range(N):
        for k in range(N):
            if(V[j][k]==1):
                temp[j,k,0]=1

    tempDict=dict()

    allDict=dict()
    for i in range(N):
        allDict[i]=set()
        allDict[i].add(i)
        #tempDict[i]=[set()]

    for i in range(N):
        for j in range(N):
            if temp[i][j][0]==1:
                if i in tempDict:
                    tempList=tempDict[i]
                    tempSet=tempList[0]
                    tempSet.add(j)
                else:
                    tempSet=set()
                    tempSet.add(j)
                    tempList=[]
                    tempList.append(tempSet)
                    tempDict[i]=tempList
                allDict[i].add(j)

    #print(temp)

    for i in tempDict:
        tempList=tempDict[i]
        for j in range(characteristicPathLength-1):
            tempSet=tempList[j]
            tempSet2=set()
            tempList.append(tempSet2)

            tempsetAlldict=allDict[i]
            temptempDict=set()

            for k in tempSet:
                for p in range(N):
                    if temp[k,p,0]==1 and p not in allDict[i]:
                        temp[i,p,j+1]+=1
                        temptempDict.add(p)
                        tempSet2.add(p)

                '''
                if temp[i][k][j] ==1 and k not in tempsetAlldict:
                    tempsetAlldict.add(k)
                        if [p,k,0]==1:
                            temp[i,p,j+1]+=temp[i,p,j+1]
                '''
            for k in temptempDict:
                tempsetAlldict.add(k)

    ttmmep = np.zeros([N, N], float)
    for i in range(N):
        for j in range(N):
            ttmmep[i,j]=temp[i,j,1]

    newV=np.zeros([N,N],float)
    for i in range(N):
        for j in range(N):

            for k in range(characteristicPathLength ):
                tempFloat=float(temp[i,j,k])
                tempPow=pow(wii,-k)
                tempFloat=tempFloat*tempPow
                newV[i,j]+=tempFloat
                tempFlpat=newV[i,j]

    for j in range(N):
        for k in range(N):
            if(newV[j][k]<=passt ):
                newV[j][k] =0;


    #print(V)
    return newV

def dfs(V,x,y,l,N,characteristicPathLength):
    for i in range(N):
        if(V[y,i,l]==1):
            V[x,y,l+1]+=(V[x,y,l]*pow(characteristicPathLength,-1*(l+1)))