#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


def readFile(input_file,changeDict):
    #filesNum=len(files)

    info=[]

    f = open(input_file, "r")
    lines = f.readlines()

    communityDict = dict()
    for line in lines:
        # get all the neighbors of the current node
        tempInfo = line.strip().split(" ");
        # self.adjacency_list.append([int(i) for i in line.strip().split("\t")])

        if communityDict.has_key(int(tempInfo[1])):
            tempList = communityDict.get(int(tempInfo[1]))
            tempList.append(tempInfo[0])
        else:
            tempList = []
            communityDict[int(tempInfo[1])] = tempList
            tempList.append(tempInfo[0])

    info.append(communityDict)

    tempdict=change(info,changeDict)
    outPut(tempdict)

def change(info,changeDict):
    tempdict=dict()

    fromDict=info[0]

    for key in changeDict:

        tempdict[key]=fromDict[changeDict[key]]

        tempdict[changeDict[key]]=fromDict[key]

    for key in fromDict:
        if tempdict.has_key(key):
            continue
        else:
            tempdict[key] = fromDict[key]

    return tempdict


def outPut(out):
    f_out = open("output2.txt", "w+")
    for key in out:

        tempList=out[key]

        for j in range(len(tempList)):
            f_out.write("%d" % int(tempList[j]))
            f_out.write(" ")
            f_out.write("%d" % int(key))
            f_out.write("\n")
    f_out.close()
    return

if __name__ == '__main__':


    changeDict=dict()
    changeDict[0]=1

    readFile("output.txt", changeDict)

name=set()