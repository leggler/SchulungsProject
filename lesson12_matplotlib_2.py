import matplotlib.pyplot as plt
import numpy as np

#standard: x und y müssen in getrennten numpy-arrays der selben größe sein
#xpoints = np.array([3,4,7,9])
#ypoints = np.array([5,3,1,6])
#plt.plot(xpoints,ypoints)


#wenn nur y angegeben, wird x automatisch von 0 aufsteigend durch nummeriert
#ypoints = np.array([5,3,1,6])
#plt.plot(ypoints)

#nur scatter-plott (mit marker)
#xpoints = np.array([3,4,7,9])
#ypoints = np.array([5,3,1,6])
#plt.plot(xpoints,ypoints,'o')


#line plot mit markern überlegt scatter-plott (mit marker)
#(reihenfolge könnte geändert werden
#xpoints = np.array([3,4,7,9])
#ypoints = np.array([5,3,1,6])
#plt.plot(xpoints,ypoints)
#plt.plot(xpoints,ypoints,'o-.m') #'*-y' 'o:m'

#mit kurzform die eigenschaften verändert - points und line in einem
#plt.plot(xpoints,ypoints,'o-.m') #'*-y' 'o:m'


#lang-form
xpoints = np.array([3,4,7,9])
ypoints = np.array([5,3,1,6])
plt.plot(xpoints,ypoints, 'D',  ms=20, mec='r', mfc='g') #D = Lang form der eigenschaften. ms=marker size, mec=marker edge color, mfc=marker fill color






plt.show()

