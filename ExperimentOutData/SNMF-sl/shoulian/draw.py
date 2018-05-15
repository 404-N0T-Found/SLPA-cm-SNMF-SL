import sys

reload(sys)

sys.setdefaultencoding("utf8")
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

times=98
floata=1.00
for i in range(20):
    x.append(floata)
    floata-=0.05

f = open("gaibiandedongxi", "r")
lines = f.readlines()
for line in lines:
    # get all the neighbors of the current node
    tempInfo = line.strip();
    # self.adjacency_list.append([int(i) for i in line.strip().split("\t")])
    y.append(float(tempInfo))

#y.sort()
plt.figure()
plt.plot(x, y)
#plt.plot(x, y, marker='o', mec='r', mfc='w')
plt.xlabel("Number of iterations")
plt.ylabel("loss")
plt.title("football")

plt.show()