# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 16:24:08 2016

Author: Peng Zhou <peng.zhou137@gmail.com>
"""
import numpy as np

def com(data=np.ones([2,4])):
    """
    Calculate the coordinates for center of mass 
    of a charge distribution
    
    data: four-column dataset, [x, y, z, Qsurf]
    """
    
    coord = np.zeros(3)
    
    for component in range(3):
        line = 0
        for x in data[:,component]:
            coord[component] += x * data[line,3]
            line += 1
            
    q_tot = np.sum(data[:,3])
    coord /= q_tot
    
    return coord
    
    
if __name__ == "__main__":
    print (com())
    
        


        