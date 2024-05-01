import matplotlib.pyplot as plt
import numpy as np

def add_errorbar_hist(ax:plt.Axes, bin_edges:np.ndarray, bin_heights:np.ndarray, bin_errors:np.ndarray,
                      fit_x = False, label = ''):
    '''
    Draws a histograms on the provided Axes object

    Parameters
    ----------
    ax : plt.Axes
        The axes object to draw on
    bin_edges : np.ndarray
        All bin edges (including left-most and right-most)
    bin_heights : np.ndarray
        The height of each bin.  Should be len(bin_edges) - 1.
    bin_errors : np.ndarray
        The error in each bin.  Should be len(bin_edges) - 1.
    '''
    
    l = ax.step(bin_edges,np.append(np.zeros(1),bin_heights), where = 'pre')
    ax.step(bin_edges,np.append(bin_heights, np.zeros(1)), where = 'post', color = l[0].get_color())
    ax.errorbar((bin_edges[0:-1] + bin_edges[1:])/2, bin_heights, yerr = bin_errors, color = l[0].get_color(), fmt = 'none')
    
    if label != '':
        l[0].set_label(label)
    
    if fit_x:
        ax.set_xlim(bin_edges[0], bin_edges[-1])
        
    ax.set_ylim(0,None)
    
    return ax,l 