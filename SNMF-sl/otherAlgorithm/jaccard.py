import numpy as np
def getJaccardM(A,N):

    newJaccard=np.zeros([N,N],float)

    tempDict=dict()
    for i in range(N):
        tempDict[i]=set()
        for j in range(N):
            if A[i,j]==1:
                tempDict[i].add(j)

    for i in range(N):
        for j in range(N):
            tempSetI=tempDict[i]
            tempSetj = tempDict[j]
            if len(tempSetj)>len(tempSetI):
                temptemp=tempSetI
                tempSetI=tempSetj
                tempSetI=temptemp
            temp=0
            tempSetHe=set()
            for k in tempSetI:
                if k in tempSetj:
                    temp+=1

            for k in tempSetI:
                tempSetHe.add(k)
            for k in tempSetj:
                tempSetHe.add(k)
            tempc=float(temp)/float(len(tempSetHe))
            newJaccard[i][j]=tempc

    return newJaccard