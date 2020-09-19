import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits
from matplotlib import rc,rcParams
from mpl_toolkits.mplot3d import axes3d

X,Y,Z = np.loadtxt("csv_file",
                  unpack=True,
                  delimiter=',')
rc('text', usetex=True)
# Plot X,Y,Z
fig = plt.figure(figsize=(12,12))

ax = fig.add_subplot(projection='3d')
ax.set_xlabel(r'\textbf{X axis}')
ax.set_ylabel(r'\textbf{Y axis}')
ax.set_zlabel(r'\textbf{Z axis}')

# Reference - https://towardsdatascience.com/visualizing-three-dimensional-data-heatmaps-contours-and-3d-plots-with-python-bd718d1b42b4
# Remove gray panes and axis grid
ax.xaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('white')
ax.yaxis.pane.fill = False
ax.yaxis.pane.set_edgecolor('white')
ax.zaxis.pane.fill = False
ax.zaxis.pane.set_edgecolor('white')
ax.grid(False)

p = ax.scatter(X, Y, Z, c=Z, cmap='coolwarm')
fig.colorbar(p,shrink=0.5,cmap='coolwarm')
plt.savefig('q3plot.jpg', bbox_inches='tight')
plt.show()
