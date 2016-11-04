# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:46:44 2016

Author: Peng Zhou <peng.zhou137@gmail.com>
"""
from plate import Plate

def main():
    myplate = Plate('Qsurf.fld')
    myplate.draw_qsurf2D()
    
if __name__ == "__main__":
    main()
