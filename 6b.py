import matplotlib.pyplot as plt
import numpy as np
overs=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
Runs=[6,18,13,20,11,22,9,6,7,5,8,10,7,5,12,14,18,30,23,30]
plt.plot(overs,Runs,marker='x',markerfacecolor='blue',markersize=8,linestyle='dashed',linewidth=2,color='red')
plt.xlabel("overs",color='black')
plt.ylabel("Runs",color='red')
plt.title("line format-Vachan-1KI23CS173")
plt.show()