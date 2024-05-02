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

def add_data_fit(ax:plt.Axes, data_x:np.ndarray, data_y:np.ndarray,
                 fit_func, fit_params:np.ndarray, x_err:np.ndarray = None, y_err:np.ndarray = None,
                 data_label:str = 'Data', fit_label:str = 'Fit')->tuple:
    '''
    Adds a data points and a fitted curve to the provided axes.  

    Parameters
    ----------
    ax : plt.Axes
        The axes to add the plot to
    data_x : np.ndarray
        Data values x coordinate
    data_y : np.ndarray
        Data values y coordinate
    fit_func : function
        The function used to fit the data 
    fit_params : np.ndarray
        Parameters for the function fit
    x_err : np.ndarray, optional
        Error in the x coordinate, by default None
    y_err : np.ndarray, optional
        Error in the y coordinate, by default None
    data_label : str, optional
        Legend key for the data, by default 'Data'
    fit_label : str, optional
        Legend key for the fit, by default 'Fit'

    Returns
    -------
    tuple
        The axes object, the scatter/errorbar plot, the curve line
    '''
    if x_err == None and y_err == None:
        pts = ax.scatter(data_x, data_y, label = data_label)
    else:
        pts = ax.errorbar(data_x, data_y, xerr = x_err, yerr = y_err, label = data_label, fmt = '.')
        
    fine_x = np.linspace(np.min(data_x), np.min(data_x),int(data_x.shape[0] * 10))
    line = ax.plot(fine_x, fit_func(fine_x, *fit_params), label = fit_label)
    
    return ax, pts, line 