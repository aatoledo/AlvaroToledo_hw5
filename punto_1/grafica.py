import numpy as np
import corner 
import matplotlib.pyplot as plt
import pandas as pd


#Carga Datos
nombres = ['x','y','l']
data = np.genfromtxt('resultados.csv', delimiter = ',', names = nombres)

#Plots
fig,ax = plt.subplots()
fig.set_size_inches((6,6))
ax.plot(data['x'], data['y'], '.', alpha=0.2, label='random walk')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.grid()
ax.legend(loc='best')
fig.savefig('densityPlot.png')

#Corner
n = len(data['x'])
samples = np.array([data['x'], data['y']]).reshape((n,2))
fig = corner.corner(samples, labels=[r"$x$", r"$y$"],
show_titles=True, title_kwargs={"fontsize": 12})
fig.savefig('corner_plot.png')

#Seaborn
import seaborn as sns
data_df = pd.DataFrame(data, columns=["x","y"])
sns.jointplot(x="x", y="y", data=data_df);
plt.savefig('jointPlot.png')
