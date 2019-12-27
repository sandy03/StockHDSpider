# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:49:28 2019

@author: Sandy Lin
"""
from Parser import get_page,parse_page
if __name__=='__main__':
    customers=[]
    with open("C:\\Users\\Sandy Lin\\Desktop\\1.txt","r")as f:
         data=f.readlines()
         for line in data:
                 target=line.split('.')[0]
                 json0=get_page(0,target)
                 json1=get_page(1,target)
                 json2=get_page(2,target)
                 StockHDs_2019=parse_page(json0,target)
                 StockHDs_2018=parse_page(json1,target)
                 StockHDs_2016=parse_page(json2,target)
                 if len(StockHDs_2019)!=0 and len(StockHDs_2018)!=0 and len(StockHDs_2016)!=0:
                     for item0 in StockHDs_2019:
                         for item1 in StockHDs_2018:
                             if item0.name==item1.name:
                                item0.score=item0.score+1
                                break
                         for item2 in StockHDs_2016:
                             if item0.name==item2.name:
                                item0.score=item0.score+1
                                break
                         if item0.score==2:
                            print(item0)
                            customers.append(item0)
    print(customers)