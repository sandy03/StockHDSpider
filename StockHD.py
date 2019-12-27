# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:44:37 2019

@author: Sandy Lin
"""
class StockHD:
    def __init__(self,name=None,rank=None,CompIndex=None):
        self.name=name
        self.rank=rank
        self.CompIndex=CompIndex
        self.score=0
    def __repr__(self):
        return "({},{},{})".format(self.name,self.rank,self.CompIndex)
    def __iter__(self):
        for item in (self.name,self.rank,self.CompIndex,self.score):
            yield item

