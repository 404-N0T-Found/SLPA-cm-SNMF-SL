#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


def readFile(files):
    filesNum=len(files)

    info=[]

    for i in range(filesNum):
        f = open(str(files[i]), "r")
        lines = f.readlines()

        communityDict = dict()
        #	dict.get(key, default=None)

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

    tempset=compare(info)
    outPut(tempset)

def compare(info):
    tempset=set()

    for i in range(len(info)):
        j = i + 1
        for j in range(len(info)):
            tempi=info[i]
            tempj=info[j]

            for key in tempi:
                templisti=tempi[key]
                templistj = tempj[key]
                ret_list = list(set(templisti) ^ set(templistj))

                tempset.update(ret_list)

                #tempset.add()  # b中有而a中没有的

    return tempset


def outPut(out):
    f_out = open("output.txt", "w+")
    for i in out:

        f_out.write("%d" % int(i))
        f_out.write("\n")
    f_out.close()
    return

if __name__ == '__main__':
    path = "/home/zhaoyulu/Desktop/my-master-paper/SNMFOUT"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    strs=[]
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开

            strs.append(path + "/" + file)
    readFile(strs)

name=set()