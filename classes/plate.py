# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 17:00:35 2016

Author: Peng Zhou <peng.zhou137@gmail.com>
"""

from __future__ import division, print_function
import numpy as np

class Plate(object):
    """
    Analysis for Qsurf field distribution
    """
    def __init__(self, fname=None):
        """Initialize a Plate with fname
        
        fname : contains Qsurf distribution.
            string, needs to be of format '*.fld'
        """
        if fname == None:
            self.qsurf = np.ones([2,4])
        else:
            self.qsurf = np.loadtxt(fname)
        
        
    @property
    def coc(self):
        """
        Calculate the coordinates for center of charge 
        of a charge distribution. 
        """
        
        coord = np.zeros(3)
        
        for component in range(3):
            line = 0
            for x in self.qsurf[:,component]:
                coord[component] += x * self.qsurf[line,3]
                line += 1
                
        q_tot = np.sum(self.qsurf[:,3])
        coord /= q_tot
        
        return coord
    
    
if __name__ == "__main__":
    print (Plate().coc)
    
        
