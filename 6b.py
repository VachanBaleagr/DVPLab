import matplotlib.pyplot as plt
import numpy as np
overs=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
Runs=[6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,102,108,114,120]
plt.plot(overs,Runs,marker='x',markerfacecolor='blue',markersize=8,linestyle='dashed',linewidth=2,color='red')
plt.xlabel("overs",color='black')
plt.ylabel("Runs",color='red')
plt.title("line format-Vachan-1KI23CS173")
plt.show()