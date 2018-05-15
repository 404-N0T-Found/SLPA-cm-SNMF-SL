# encoding=utf-8
import random
import matplotlib.pyplot as plt
from pylab import *
def readFile(input_file):
    f = open(input_file, "r")
    lines = f.readlines()

    listInfo=[]

    tempDict=dict()

    for line in lines:
        tempList=line.strip().split(':');

        tempList1=float(tempList[0])
        tempList2 = map(float,tempList[1].split(" "))

        tempDict[tempList1]=tempList2

    for temp in tempDict:
        temptemp=sum(tempDict[temp])/len(tempDict[temp])
        newlist=[]
        for i in tempDict[temp]:
            newlist.append(i-temptemp)
        tempDict[temp]=newlist

    draw(tempDict)
    return





def draw(tempDict):
    x = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

    tempDictFloat=[0.1,0.15,0.20,0.25,0.3,0.35,0.4,0.45,0.5,0.55]

    for temp in tempDictFloat:
        tempLabel="mu="+str(temp)
        plt.plot(x, tempDict[temp],  label=tempLabel, linewidth=0.5)





    plt.legend(fontsize=10)  # 让图例生效
    plt.yticks(fontsize=7)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel("mu", fontsize=7)  # X轴标签
    plt.ylabel("EQ")  # Y轴标签
    # plt.title("A simple plot") #标题
    plt.subplots_adjust(bottom=0.1,top=0.95,left=0.1,right=0.95)
    plt.show()


if __name__ == '__main__':

    fileName="output_eq.txt"

    readFile(fileName)