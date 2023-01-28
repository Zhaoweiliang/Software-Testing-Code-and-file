

import numpy as np
import matplotlib.pyplot as plt

   
from time import sleep
from IPython.display import clear_output

from utils import underride

import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
from matplotlib.colors import LinearSegmentedColormap

class Cell2D:
    """Parent class for 2-D cellular automata."""

    def __init__(self, n, m=None):
        """Initializes the attributes.
        n: number of rows
        m: number of columns
        """
        self.n = n
        m = n if m is None else m
        self.array = np.zeros((n, m), np.uint8)

    def add_cells(self, row, col, *strings):
        """Adds cells at the given location.
        row: top row index
        col: left col index
        strings: list of strings of 0s and 1s
        """
        for i, s in enumerate(strings):
            self.array[row+i, col:col+len(s)] = np.array([int(b) for b in s])

    def loop(self, iters=1):
        """Runs the given number of steps."""
        for i in range(iters):
            self.step()

    def draw(self, **options):
        """Draws the array.
        """
        draw_array(self.array, **options)

    def animate(self, frames, interval=None, step=None):
        """Animate the automaton.
        
        frames: number of frames to draw
        interval: time between frames in seconds
        iters: number of steps between frames
        """
        if step is None:
            step = self.step
        plt.figure(7,figsize=(19.20, 9.61))    
        #plt.figure()
        try:
            for i in range(frames-1):
                self.draw()
                plt.show()
                if interval:
                    sleep(interval)
                step()
                clear_output(wait=True)
            self.draw()
            plt.show()
        except KeyboardInterrupt:
            pass
        

def draw_array(self):
    cmap1 = LinearSegmentedColormap.from_list('cmap', ['Black','Cyan'])

    cmap2 = (mpl.colors.ListedColormap(['1', 'red', 'grey']))
    """Draws the cells."""
        
    plt.figure(7,figsize=(20, 20))

    plt.xticks([])
    plt.yticks([])
    plt.imshow(self.prob_place,cmap=cmap1,interpolation='nearest')
    plt.imshow(self.place,cmap=cmap2,alpha = 0.85,interpolation='kaiser')
    pylab.show()