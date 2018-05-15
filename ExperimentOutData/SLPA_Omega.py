# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0.05','0.1', '0.15', '0.20', '0.25', '0.30','0.35', '0.40', '0.45', '0.50']
x = range(len(names))

SLPA_cm = [0.79,	0.74	,0.72	,0.67,	0.64,	0.62	,0.595,	0.527	,0.44,	0.39]
LPPB    =[0.781,	0.721	,0.7	,0.65,	0.622	,0.601,	0.574,	0.502,	0.41	,0.37]
SLPA    =[0.74,	0.701	,0.67	,0.6	,0.574,	0.555,	0.521,	0.444,	0.37	,0.32]
COPRA = [0.732,	0.712,	0.667,	0.587	,0.567,	0.567	,0.515,	0.414,	0.365,	0.33]


#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, SLPA_cm, marker='o', label=u'SLPA-cm',linewidth=0.5)
plt.plot(x, LPPB, marker='*', label=u'LPPB',linewidth=0.5)
plt.plot(x, SLPA, marker='>',label=u'SLPA',linewidth=0.5)
plt.plot(x, COPRA, marker='_', label=u'COPRA',linewidth=0.5)

plt.legend(fontsize=7)  # 让图例生效
plt.xticks(x, names, rotation=45,fontsize=7)
plt.yticks(fontsize=7)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("mu", fontsize=7) #X轴标签
plt.ylabel("Omega") #Y轴标签
#plt.title("A simple plot") #标题

plt.show()

