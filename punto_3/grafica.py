import numpy as np
import matplotlib.pyplot as plt
import corner

# Cargar datos
lv_c = np.genfromtxt('prueba.csv', delimiter=',')
lv_obs = np.genfromtxt('data.txt', delimiter=' ')
nombres =  ['alpha','beta','gamma','delta']
data = np.genfromtxt('resultados.csv', delimiter=',', names=nombres)

# Grafica de presas
ylims = [0,90];
plt.figure()
plt.plot(lv_c[:,0], lv_c[:,1], '.-', label='presas')
plt.plot(lv_c[:,0], lv_c[:,2], '.-', label='depredadores')
plt.xlabel('tiempo')
plt.ylabel('N')
plt.ylim(ylims)
plt.grid()
plt.legend()
plt.savefig('lv_c.png')

plt.figure()
plt.plot(lv_obs[:,0], lv_obs[:,1], '.-', label='presas')
plt.plot(lv_obs[:,0], lv_obs[:,2], '.-', label='depredadores')
plt.xlabel('tiempo')
plt.ylabel('N')
plt.ylim(ylims)
plt.grid()
plt.legend()
plt.savefig('lv_obs.png')

# corner plot
n = len(data['alpha'])
samples = np.array([data['alpha'], data['beta'], data['gamma'], data['delta']]).reshape((n,4))
fig = corner.corner(samples, labels=[r"$\alpha$", r"$\beta$", r"$\gamma$", r"$\delta$"],
show_titles=True, title_kwargs={"fontsize": 12})
fig.savefig('corner_plot.png')
