#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import time
import operator

from clusterRank import ClusterRank
import os

class Slpa:
    """Identify overlapping nodes and overlapping communities in social networks

    Attributes:
       N: number of nodes
       ITERATION: number of iterations
       THRESHHOLD: r => [0,1], if the probability is less than r,
                   remove it during post processing

       adjacency_list: int[N][K] for each node a list of its neighbours' id
       node_memory: [int]{id:count} first dimension is a list of all nodes
                    for each node we have a dictionary keeping the count 
                    of the labels it received 
        
    """    
 
    def __init__(self, input_file):

        self.maxCoummnity=3
        """Initialize the instance with input data

        create adjacency_list after reading the input file

        Args:
            input_file: the file path to the input file
                        The file 
        """
        f = open(input_file, "r")
        lines = f.readlines()

        tempLine=lines.pop(0).strip().split(" ")

        self.N = int(tempLine.pop(0))
        self.LAMDA = int(tempLine.pop(0))



        print "N=%d" % self.N
        print "LAMDA=%d" % self.LAMDA
 
        self.adjacency_list = []
        self.node_memory = []        

        for line in lines:
            # get all the neighbors of the current node
            tempInfo = line.strip().split("\t");
            #self.adjacency_list.append([int(i) for i in line.strip().split("\t")])
            self.adjacency_list.append([int(tempInfo[0])-1,int(tempInfo[1])-1])

        print "self.adjacency_list has length %d" % len(self.adjacency_list)

        for i in range(self.N):     
            self.node_memory.append({i:1})  #append a dictionary containing single entry to node_memory

        #
        self.ClusterRank=ClusterRank(self.N, self.adjacency_list,self.LAMDA)


        print "self.node_memory has length %d" % len(self.node_memory)

    #end of __init__ 


    def perform_slpa(self, ITERATION):
        """Performs SLPA algorithm 
        
        Use multinomial sampling for speaker rule
        Use maximum vote for listener rule
        Args:
            TERATION: number of iterations
        """
        self.ITERATION = ITERATION

        #标签队列
        self.labelDict = dict()
        i = 0
        while i < self.N:
            self.labelDict[i + 1] = 1
            i = i + 1

        order = np.zeros(self.N, int)

        i = 0;
        while i < self.N:
            order[i] = self.ClusterRank.rankList[i][0]
            i = i + 1

        for t in range(self.ITERATION):
              
            print "Performing %dth iteration..." % t
            #替换更新顺序

            #order = np.random.permutation(self.N)  # Nodes.ShuffleOrder()


           # order=self.ClusterRank.rankList[0]
            for i in order:  #for each node
                label_list = {}
               
                for j in self.adjacency_list[i]:  #for each neighbor of the listener
                    # select a label to propagate from speaker j to listener i
                    sum_label = sum(self.node_memory[j].itervalues())
                    label = self.node_memory[j].keys()[np.random.multinomial(1,[float(c)/sum_label for c in self.node_memory[j].values()]).argmax()]
                    if label not in label_list:
                        label_list[label] = 1
                    else:
			label_list[label] += 1
                
                #listener chose a received label to add to memory
                selected_label = max(label_list, key=label_list.get)

                if label_list[selected_label]>self.maxCoummnity:
                    tempLabel=selected_label
                    self.labelDict[tempLabel] -= 1
                    for i in label_list:
                        if label_list[i] <=self.maxCoummnity:
                            selected_label=i
                            self.labelDict[i]+=1
                    if tempLabel==selected_label:
                        self.labelDict[tempLabel]-=1

                #add the selected label to the memory
                if selected_label in self.node_memory[i]:
                    self.node_memory[i][selected_label] += 1
                else:
                    self.node_memory[i][selected_label] = 1
                                
    #end of perform_slpa

    def post_processing(self, THRESHHOLD):
        """performs post processing to remove the labels that are below the threshhold
           
        Args:
	    THRESHHOLD: r => [0,1], if the probability is less than r,
                        remove it during post processing
        """
        print "Performing post processing..."

        self.THRESHHOLD = THRESHHOLD

        for memory in self.node_memory:
            sum_label = sum(memory.itervalues())
            threshhold = sum_label * self.THRESHHOLD
            for k,v in memory.items():
                if v < threshhold:
                    del memory[k]  # remove the outliers
    #end of post_processing
    
 
#end of Slpa class

def main(file):

    start_time = time.time()
    slpa = Slpa(file)
    end_time = time.time()
    print("Elapsed time for initialization was %g seconds" % (end_time - start_time))

    start_time = time.time()
    slpa.perform_slpa(20)  #perform slpa for 20 iterations
    end_time = time.time()
    print("Elapsed time for slpa-cm was %g seconds" % (end_time - start_time))

    start_time = time.time()
    slpa.post_processing(0.2)  #perform postprocessing with threshhold 0.1
    end_time = time.time()
    print("Elapsed time for post processing was %g seconds" % (end_time - start_time))

    #临时注释

    f_out = open("output.txt","w+")
    for i in range(len(slpa.node_memory)):
        f_out.write("Node %d" % i)
        f_out.write("%s\n" % str(slpa.node_memory[i]))        
    f_out.close()

    # dictionary to maintain the size of all the groups
    group_size = {}

    for i in range(len(slpa.node_memory)):
        for j in slpa.node_memory[i].keys():
            if j in group_size:
                group_size[j] += 1
            else:
                group_size[j] = 1

    f_out = open("stats.txt","w+")
    f_out.write("Graph of %d nodes\n" % slpa.N)
    f_out.write("Total %d groups\n" % len(group_size.keys()))

    sum_membership = sum(group_size.itervalues())
    f_out.write("Each node has membership in %.2f groups on average\n" % (float(sum_membership) / slpa.N) )

    f_out.write("group\tcount\n")

    sorted_group_size = sorted(group_size.iteritems(), key=operator.itemgetter(1))

    for item in sorted_group_size:
        if item[1] > 0:
            f_out.write("{}\t{}\n".format(item[0], item[1]))

    f_out.close()

#end of main().

if __name__ == "__main__":

    main("karate.txt")
    '''
    path = "/home/zhaoyulu/Desktop/my-master-paper/slpa-cm/lfrData"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    strs = []
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            strs.append(path + "/" + file)

    spendTime=[]
    for i in range(len(strs)):
        start_time = time.time()
        main(strs[i])
        end_time = time.time()
        spendTime.append(end_time-start_time)

    f_out = open("output_time.txt", "w+")
    for i in range(len(spendTime)):
        f_out.write("%f" % spendTime[i])
        f_out.write("\n")
    f_out.close()
    '''




