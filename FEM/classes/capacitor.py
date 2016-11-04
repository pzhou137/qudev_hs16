# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 17:39:20 2016

Author: Peng Zhou <peng.zhou137@gmail.com>
"""

from __future__ import division, print_function
import numpy as np
from plate import Plate


class Capacitor(object):
    """
    Base class for Capacitor. 
    A capacitor consists of two plates.
    """
    
    def __init__(self, fname1=None, fname2=None):
        self.plate1 = Plate(fname1)
        self.plate2 = Plate(fname2)
        
    @property    
    def d_eff(self):
        """
        effective distance between center of charge (COC) of two plates
        """
        coc1 = self.plate1.coc
        coc2 = self.plate2.coc
        np.linalg.norm(coc1 - coc2)
        
if __name__ == "__main__":
    print(Capacitor().d_eff)
        
        