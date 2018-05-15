# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

def draw(y1Name,y2Name,y3Name,y4Name,path,yName):


    yNames=[y1Name,y2Name,y3Name,y4Name]
    paths=[]
    tempys=[]
    for temp in yNames:
        paths.append(path+temp+"/"+yName+".txt")

    tempset=set()
    for i in range(4):
        f = open(str(paths[i]), "r")
        lines = f.readlines()
        tempLineArr=[]
        for line in lines:
            tempLineArr.append(sum(map(float,line.strip().split(":")[1].split("\t")))/len(map(float,line.strip().split(":")[1].split("\t"))))
            tempset.add(float(line.strip().split(":")[0]))
        tempys.append(tempLineArr)

    names = list(tempset)
    x = range(len(names))

    plt.plot(x, tempys[0], marker='o', label=y1Name,linewidth=0.5)
    plt.plot(x, tempys[1], marker='*', label=y2Name,linewidth=0.5)
    plt.plot(x, tempys[2], marker='>',label=y3Name,linewidth=0.5)
    plt.plot(x, tempys[3], marker='_', label=y4Name,linewidth=0.5)

    plt.legend(fontsize=7)  # 让图例生效
    plt.xticks(x, names, rotation=45,fontsize=7)
    plt.yticks(fontsize=7)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel("mu", fontsize=7) #X轴标签
    plt.ylabel(yName, fontsize=7) #Y轴标签
    #plt.title("A simple plot") #标题

    plt.show()

if __name__ == '__main__':

    y1Name = "SLPA-cm"
    y2Name = "LPPB"
    y3Name = "SLPA"
    y4Name = "COPRA"

    path = "/home/zhaoyulu/Desktop/my-master-paper/ExperimentOutData/SLPA-cm/"

    yName="eq"

    draw(y1Name,y2Name,y3Name,y4Name,path,yName)

