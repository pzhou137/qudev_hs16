# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:46:44 2016

Author: Peng Zhou <peng.zhou137@gmail.com>
"""
from __future__ import print_function, division
from classes import Capacitor

def main():
    fname1 = "Q:\\USERS\\Peng\\_fromAdrian\\qsurf_n.fld"
    fname2 = "Q:\\USERS\\Peng\\_fromAdrian\\qsurf_p.fld" 
    myplate = Capacitor(fname1, fname2)
    
    print(myplate.d_eff)
    
if __name__ == "__main__":
    main()
