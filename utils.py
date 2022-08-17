import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap

def graficarVector(ax, vec, cmap='viridis', color='blue'):

    out = None
    if np.ndim(vec) == 2:
        if isinstance(cmap, str):
            colors = plt.cm.get_cmap(cmap, len(vec))
            colors = colors(np.linspace(0.1,1,len(vec)))
        elif isinstance(cmap, Colormap):
            colors = cmap
            colors = colors(np.linspace(0.1,1,len(vec)))
        elif isinstance(cmap, list):
            assert len(vec) == len(cmap)
            colors = cmap
        for v, c in zip(vec, colors):
            out = graficarVector(ax, v, color=c)
    else:    
        x = np.concatenate(([0,0], vec))
        out = ax.quiver(*x, angles='xy', scale_units='xy', scale=1, color=color)
    ax.set_ylim(-np.max(np.abs(vec)), np.max(np.abs(vec)))
    ax.set_xlim(-np.max(np.abs(vec)), np.max(np.abs(vec)))
    # ax.spines.right.set_visible = False
    # ax.spines.top.set_visible = False
    return out
    
def graficarMatriz(ax, matriz, cmap='viridis', color='green', vectors=True):
    x = np.linspace(-1,1,1000)
    y = np.sqrt(1-x**2)
    
    x1 = matriz[0,0]*x + matriz[0,1]*y
    y1 = matriz[1,0]*x + matriz[1,1]*y
    x1_neg = matriz[0,0]*x - matriz[0,1]*y
    y1_neg = matriz[1,0]*x - matriz [1,1]*y
    
    u1 = [matriz[0,0], matriz[1,0]]
    v1 = [matriz[0,1], matriz[1,1]]
    
    # ax = f.add_subplot(111)
    if vectors:
        out = graficarVector(ax, [u1, v1], cmap=cmap)
    ax.plot(x1, y1, color=color, alpha=0.7)
    out = ax.plot(x1_neg, y1_neg,color, alpha=0.7 )
    ax.set_ylim(-np.max(np.abs(matriz))-1, np.max(np.abs(matriz))+1)
    ax.set_xlim(-np.max(np.abs(matriz))-1, np.max(np.abs(matriz))+1)
    ax.spines.left.set_position('center')
    ax.spines.bottom.set_position('center')
    ax.spines.top.set_visible(False)
    ax.spines.right.set_visible(False)
    return out
        