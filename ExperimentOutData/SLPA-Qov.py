# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0.05','0.1', '0.15', '0.20', '0.25', '0.30','0.35', '0.40', '0.45', '0.50']
x = range(len(names))
SLPA_cm = [0.89,	0.87,	0.861	,0.811	,0.761,	0.705	,0.621,	0.465,	0.35	,0.31]
LPPB    = [0.901,	0.861,	0.855,	0.791,	0.741,	0.69	,0.605,	0.422,	0.3	,0.28]
SLPA    = [0.845,	0.79,	0.76,	0.722,	0.651	,0.601,	0.55	,0.35,	0.22	,0.22]
COPRA   = [0.851,	0.788,	0.741	,0.712,	0.631,	0.591	,0.55	,0.33	,0.23,	0.19]


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
plt.ylabel("EQ") #Y轴标签
#plt.title("A simple plot") #标题

plt.show()

