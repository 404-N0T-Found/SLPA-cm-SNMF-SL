# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0.1', '0.15', '0.20', '0.25', '0.30','0.35', '0.40', '0.45', '0.50','0.55']
x = range(len(names))

SLPA_cm = [0.951,	0.954	,0.941,	0.891,	0.812	,0.742,	0.711,	0.667	,0.567,	0.55]
LPPB    = [0.947,	0.921,	0.901,	0.841,	0.775	,0.745,	0.722,	0.674,	0.575,	0.52]
SLPA    =[0.932,	0.912,	0.895,	0.831,	0.766,	0.69	,0.63,	0.575,	0.499,	0.47]
COPRA   = [0.871,	0.861,	0.86,	0.781	,0.721,	0.654	,0.58,	0.501,	0.475,	0.465]


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
plt.ylabel("Omega") #Y轴标签
#plt.title("A simple plot") #标题

plt.show()

