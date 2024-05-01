"""
A module that loads preferred plot setting 
"""
import matplotlib.pyplot as plt
from glob import glob
import pickle
from cycler import cycler
plt.style.use('science')

ls_cycler = cycler(linestyle = ['-','--', ':', '-.','-','--',':'])

plt.rcParams.update({'axes.grid':True, #Adds gridlines 
                     'errorbar.capsize':2.0,
                     'image.cmap':'plasma',
                     'axes.prop_cycle': plt.rcParams['axes.prop_cycle'] + ls_cycler,
                     'legend.frameon':True, 'legend.handlelength':1.0,
                     'font.size':14,'figure.figsize':(6,4)})

def initiate_figure(shape:tuple, titles = None, xlabels = None, ylabels = None):
    '''
    Creates the figure canvas for a plot.  Also will add any aestetic features 
    of the plot

    Parameters
    ----------
    shape : tuple
        How many subplots to make.  Use (nrows, ncols).
    titles : list, optional
        Title to apply to each axis. The default is None.
    xlabels : list, optional
        The x-label for each axis. The default is None.
    ylabels : list, optional
        The y-label for each axis. The default is None.

    Returns
    -------
    fig : plt.Figure
        The generated plt.Figure object
    ax : np.ndarray
        The generated plt.Axes objects in a numpy array

    '''
    
    nrows, ncols = shape
    fig, ax = plt.subplots(nrows,ncols, figsize = (6 * ncols, 4 * nrows), 
                           constrained_layout = True)
    
    for i,axis in enumerate(ax.ravel()):
        if titles != None and titles[i] != '':
            axis.set_title(titles[i])
        if xlabels != None and xlabels[i] != '':
            axis.set_xlabel(xlabels[i])
        if ylabels != None and ylabels[i] != '':
            axis.set_ylabel(ylabels[i])
            
    return fig, ax

def better_save(fig:plt.Figure, ax:plt.Axes, filename:str, overwrite = False):
    '''
    Saves figures as two different filetypes and saves their fig/ax objects in a pickle

    Parameters
    ----------
    fig : plt.Figure
        Figure object for the figure to save
    ax : plt.Axes
        Axis object for the figure
    filename : str
        The filename prefix to be used
    overwrite : bool, optional
        If True, the last version will be saved on top of. The default is False.

    Returns
    -------
    None.
    '''
    version_number = len(glob(f'{filename}_V*.pdf')) + 1
    if overwrite:
        version_number -= 1
        
    whole_fname = f'{filename}_V{version_number}'
    fig.savefig(f'{whole_fname}.pdf')
    fig.savefig(f'{whole_fname}.svg')
    
    with open(f'{whole_fname}_data.pickle','wb') as f:
        pickle.dump((fig,ax), f)
        
    print(f'Version {version_number} successfully saved')
    
    
    
    

