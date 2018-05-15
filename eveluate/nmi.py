#!/usr/bin/python

'''
Created on Oct 12, 2013
I did not complete this class because I found
previous implementation of the same method
@author: yiping
'''

import numpy as np
import math
import getopt
import sys


def usage():
    print "\nThis is the usage function\n"
    print 'Usage: ' + sys.argv[0] + ' -i <our output file> -g <gold standard file> -n <num nodes>'

def NMI(A,B):
    # len(A) should be equal to len(B)
    total = len(A)
    A_ids = set(A)
    B_ids = set(B)
    #Mutual information
    MI = 0
    eps = 1.4e-45
    for idA in A_ids:
        for idB in B_ids:
            idAOccur = np.where(A==idA)
            idBOccur = np.where(B==idB)
            idABOccur = np.intersect1d(idAOccur,idBOccur)
            px = 1.0*len(idAOccur[0])/total
            py = 1.0*len(idBOccur[0])/total
            pxy = 1.0*len(idABOccur)/total
            MI = MI + pxy*math.log(pxy/(px*py)+eps,2)
    # Normalized Mutual information
    Hx = 0
    for idA in A_ids:
        idAOccurCount = 1.0*len(np.where(A==idA)[0])
        Hx = Hx - (idAOccurCount/total)*math.log(idAOccurCount/total+eps,2)
    Hy = 0
    for idB in B_ids:
        idBOccurCount = 1.0*len(np.where(B==idB)[0])
        Hy = Hy - (idBOccurCount/total)*math.log(idBOccurCount/total+eps,2)
    MIhat = 2.0*MI/(Hx+Hy)
    return MIhat

def main(argv):
    """normalized mutual information measure
    measures the similarity of two covers, output a float number in range [0, 1]
    parameters:
        -i: the location of the file to store the output of overlapping community detection
        -g: the location of the file containing the gold standard
        -n: number of nodes
    """

    try:
        '''
        opts, args = getopt.getopt(argv, 'hi:g:n:', ['help', 'input file=', 'gold standard file=', 'number of nodes='])
        if not opts or len(opts) != 3:
            print 'Wrong number of options supplied'
            usage()
            sys.exit(2)

        # get sys arguments
        input_file = opts[0][1]
        print "input file at %s" % input_file
        gold_standard_file = opts[1][1]
        print "gold standard file at %s" % gold_standard_file
        num_nodes = int(opts[2][1])
        print "graph contains %d nodes" % num_nodes
        '''

        input_file = "/home/zhaoyulu/Desktop/my-master-paper/eveluate/community.dat"
        gold_standard_file =  "/home/zhaoyulu/Desktop/my-master-paper/eveluate/outPutVonconvert.txt"
        num_nodes=5000
        # read the clusters in the two covers
        clusters1 = []

        f = open(input_file, "r")
        lines = f.readlines()
        for line in lines:
            if ":" in line:
                line = line.split(":")[-1]
            line=line.strip()
            clusters1.append([int(node) for node in line.split(" ")])  # get the nodes that are separated by a space

        clusters2 = []

        f = open(gold_standard_file, "r")
        lines = f.readlines()
        for line in lines:
            if ":" in line:
                line = line.split(":")[-1]
            line = line.strip()
            clusters2.append([int(node) for node in line.split(" ")])  # get the nodes that are separated by a space

        entropy1 = []  # vector with length k, entrophy of each cluster in clusters1
        entropy2 = []  # vector with length l, entrophy of each cluster in clusters2
        # NOTE: relative entropy is not symetric
        relative_entropy_xy = []  # 2D array, l*k, relative entropy H(X_k,y_l)
        relative_entropy_yx = []  # 2D array, k*l, relative entropy H(y_l,x_k)

        for i in range(len(clusters1)):
            #prob = len(cluster) / num_nodes  # probability of a random node belongs to this cluster
            A=np.array(clusters1[i])
            B=np.array(clusters2[i])
            entropy1.append(NMI(A,B))


    except getopt.GetoptError, e:
        print e
        usage()
        sys.exit(2)

    # End of main().
    tempent=0.0
    pp=len(clusters1)
    for i in range(len(entropy1)):
        listlen=entropy1[i]*(float(len(clusters1[i]))/num_nodes)
        tempent+=listlen
    print(entropy1)
    return tempent

if __name__ == "__main__":
    print(main(sys.argv[1:]))