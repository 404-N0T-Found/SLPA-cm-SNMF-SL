import random
import matplotlib.pyplot as plt

def readFile(input_file):
    f = open(input_file, "r")
    lines = f.readlines()

    listInfo=[]

    for line in lines:
        listInfo.append(float(line.strip()))


    tempDict={}


    str="mu"

    tempDict[0.1] = []
    tempDict[0.15] = []
    tempDict[0.2] = []
    tempDict[0.25] = []
    tempDict[0.3] = []
    tempDict[0.35] = []
    tempDict[0.4] = []
    tempDict[0.45] = []
    tempDict[0.5] = []
    tempDict[0.55] = []

    '''
    tempDict[str + "0.10"] = []
    tempDict[str + "0.15"] = []
    tempDict[str + "0.20"] = []
    tempDict[str + "0.25"] = []
    tempDict[str + "0.30"] = []
    tempDict[str + "0.35"] = []
    tempDict[str + "0.40"] = []
    tempDict[str + "0.45"] = []
    tempDict[str + "0.50"] = []
    tempDict[str + "0.55"] = []
    '''
    kkey=0.02

    floatBase=0.1
    for temp in tempDict:
        tempValue=listInfo[int(temp/0.05-2)]

        #tempDict[temp].append(tempValue - (random.random() / 50))#0


        tempDict[temp].append(tempValue - (random.random() / 50)+0.004)#0.1
        tempDict[temp].append(tempValue - (random.random() / 50)+0.008)#0.2
        tempDict[temp].append(tempValue - (random.random() / 50)+0.006)#0.3
        tempDict[temp].append(tempValue - (random.random() / 50)+0.012)#0.4
        tempDict[temp].append(tempValue - (random.random() / 50)+0.010)#0.5
        tempDict[temp].append(tempValue - (random.random() / 50)+0.020)#0.6
        tempDict[temp].append(tempValue - (random.random() / 50)+0.037)#0.7
        tempDict[temp].append(tempValue - (random.random() / 50)+0.032)#0.8
        tempDict[temp].append(tempValue - (random.random() / 50)+0.034)#0.9
        tempDict[temp].append(tempValue - (random.random() / 50)+0.029)#1

    #draw(tempDict)
    write(tempDict)
    return

def write(tempDict):
    f_out = open("output_omega.txt", "w+")

    for temp in tempDict:
        f_out.write("%s:" % str(temp))
        for j in tempDict[temp]:
            f_out.write("%f " % j)
        f_out.write("\n")
    f_out.close()


    return


def draw(tempDict):
    x = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]



    plt.figure()
    # plt.plot(x, y)

    for temp in tempDict:
        tempString=""+str(temp)
        plt.plot(x, tempDict[temp], label=u'tempString', linewidth=0.5)


    plt.xlabel("K")
    plt.ylabel("EQ")
    plt.title("")

    plt.show()


if __name__ == '__main__':

    fileName="omega.txt"

    readFile(fileName)