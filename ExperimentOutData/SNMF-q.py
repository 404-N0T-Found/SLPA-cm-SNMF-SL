# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0.1', '0.15', '0.20', '0.25', '0.30','0.35', '0.40', '0.45', '0.50','0.55']
x = range(len(names))


SLPA_cm = [0.981	,0.964,	0.941,	0.901	,0.852	,0.792,	0.711,	0.647,	0.599,	0.52]
LPPB    =[0.951,	0.921	,0.901	,0.871	,0.775,	0.727	,0.612,	0.521,	0.439,	0.34]
SLPA    =[0.932	,0.922	,0.895	,0.891,	0.766	,0.691	,0.579	,0.455	,0.327	,0.29]
COPRA   =[0.921,	0.9	,0.86	,0.81	,0.731,	0.657,	0.578	,0.471	,0.398	,0.27]


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

