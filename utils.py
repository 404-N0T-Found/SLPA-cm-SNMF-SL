#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

#用于所有节点+1
def readFile(input_file,changeDict):
    #filesNum=len(files)

    info=[]

    f = open(input_file, "r")
    lines = f.readlines()

    for line in lines:
        # get all the neighbors of the current node
        tempInfo = line.strip().split("\t");
        # self.adjacency_list.append([int(i) for i in line.strip().split("\t")])
        info.append([int(tempInfo[0]),int(tempInfo[1])])



    outPut(info)



def outPut(out):
    f_out = open("dolphins2.txt", "w+")
    for i in range(len(out)):
        f_out.write("%d" % int(out[i][0]-1))
        f_out.write(" ")
        f_out.write("%d" % int(out[i][1]-1))
        f_out.write("\n")

    f_out.close()
    return

if __name__ == '__main__':


    changeDict=dict()
    changeDict[0]=1

    readFile("karate.txt", changeDict)

name=set()