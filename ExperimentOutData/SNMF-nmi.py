# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0.1', '0.15', '0.20', '0.25', '0.30','0.35', '0.40', '0.45', '0.50','0.55']
x = range(len(names))

SLPA_cm =[0.961,	0.934	,0.911	,0.851,	0.781	,0.72	,0.66	,0.62,	0.59	,0.57]
LPPB    = [0.951	,0.921,	0.901,	0.841,	0.775,	0.7,	0.65	,0.59	,0.56,	0.54]
SLPA    =[0.952,	0.922	,0.895	,0.831,	0.766,	0.69	,0.63,	0.595	,0.571	,0.555]
COPRA   =[0.921,	0.9,	0.86,	0.79	,0.69,	0.62,	0.58,	0.551,	0.522,	0.51]


#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, SLPA_cm, marker='o', label=u'SNMF-sl',linewidth=0.5)
plt.plot(x, LPPB, marker='*', label=u'SNMF-jaccard',linewidth=0.5)
plt.plot(x, SLPA, marker='>',label=u'SNMF',linewidth=0.5)
plt.plot(x, COPRA, marker='_', label=u'NMF-LSE',linewidth=0.5)

plt.legend(fontsize=7)  # 让图例生效
plt.xticks(x, names, rotation=45,fontsize=7)
plt.yticks(fontsize=7)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("mu", fontsize=7) #X轴标签
plt.ylabel("Q") #Y轴标签
#plt.title("A simple plot") #标题

plt.show()

