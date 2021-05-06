import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,2,3,5])
y = np.array([10, 3, 5, 2])
plt.subplot(1, 2, 1) #eine Zeile, 2 spalten, was ab jetzt geplottet wird kommt ins erste diagramm
plt.plot(x, y)

#links eines rechts eines
'''
x = np.array([0,3,3,5])
y = np.array([10, 3, 5, 2])
plt.subplot(1, 2, 2)#eine zeile, 2 spalten, was ab jetzt geplottet wird kommt ins zweite diagramm
plt.plot(x, y, linewidth=4)
plt.xlabel("kwh")
'''

#links eines rechts zwei

x = np.array([1,3,3,5])
labels = ["kunde1", "kunde2", "kunde3", "kunde4"]
plt.subplot(2, 2, 2)#eine zeile, 2 spalten, zweites diagramm
plt.barh(labels,x)


x = np.array([2, 3, 3, 5])
special = [0.3, 0, 0, 0]
labels = ["kunde1", "kunde2", "kunde3", "kunde4"]
plt.subplot(2, 2, 4)#eine zeile, 2 spalten, drittes diagramm (bzw. veirtes "feld")
plt.pie(x, labels=labels, explode=special)




plt.show()