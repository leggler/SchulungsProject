import matplotlib.pyplot as plt
import numpy as np


y1 = np.array([3,4,7,9])
y2 = np.array([5,3,1,6])


plt.plot(y1, linewidth='5')
plt.plot(y2)

font1 = {'family': 'serif', 'color': 'blue', 'size': 10}
font2 = {'family': 'serif', 'color': 'brown', 'size': 14}

plt.title("beispiel titel", fontdict=font2)
plt.xlabel("t",font1)
plt.ylabel("kWh",font1)

#plt.grid(axis='x', color="red", linewidth=0.4)
#plt.grid(axis="y", color="green", linewidth=0.2, linestyle='--')


#design als dictionary definiert -- mit ** können argumente an funktionen übergeben werden
design={"color":"green", "linewidth":0.2}
plt.grid(axis="y", **design)







plt.show()