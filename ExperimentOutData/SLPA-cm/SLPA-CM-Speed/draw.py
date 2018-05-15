#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = [5000, 10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000,65000,70000,75000,80000,85000,90000,95000,100000]
y = []

f = open("outTime.txt", "r")
lines = f.readlines()
for line in lines:
    # get all the neighbors of the current node
    tempInfo = line.strip();
    # self.adjacency_list.append([int(i) for i in line.strip().split("\t")])
    y.append(float(tempInfo.strip().split(":")[1]))

y.sort()



plt.figure()
#plt.plot(x, y)
plt.plot(x, y, marker='o', mec='r', mfc='w')
plt.xlabel("Number of nodes")
plt.ylabel("Spend time(s)")
plt.title("")

plt.show()