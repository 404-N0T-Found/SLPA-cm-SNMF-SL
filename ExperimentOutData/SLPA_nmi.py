# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0.05','0.1', '0.15', '0.20', '0.25', '0.30','0.35', '0.40', '0.45', '0.50']
x = range(len(names))
SLPA_cm = [0.811, 0.792  , 0.771 , 0.741 , 0.691 ,0.63  , 0.59  , 0.54  , 0.47  , 0.41]
LPPB    = [0.8  , 0.791  , 0.761 , 0.731 , 0.655  ,0.59  , 0.55  , 0.50 , 0.42 , 0.36]
SLPA    = [0.75 , 0.72   , 0.69 , 0.65 , 0.6    ,0.51  , 0.42  , 0.35 , 0.29 , 0.2]
COPRA   = [0.76 , 0.71   , 0.66 , 0.630 , 0.61  ,0.52  , 0.4  , 0.33 , 0.289 , 0.18]


#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围

# 代码中的“...”代表省略的其他参数
#ax = plt.subplot(111)
# 设置刻度字体大小
#plt.xticks(fontsize=20)
#plt.yticks(fontsize=20)
# 设置坐标标签字体大小
#ax.set_xlabel(..., fontsize=20)
#ax.set_ylabel(..., fontsize=20)
# 设置图例字体大小
#ax.legend(..., fontsize=20)

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
plt.ylabel("NMI", fontsize=7) #Y轴标签
#plt.title("A simple plot") #标题

plt.show()

