import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,10,0.001)
for i in range(1,9):
	x = np.sin(i*t)
	y = np.cos(t)
	plt.subplot(2,4,i)
	plt.plot(x,y)

plt.show()