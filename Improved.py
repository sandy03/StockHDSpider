# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 23:23:45 2019

@author: Sandy Lin
"""

from Parser import get_page,parse_page
import xlwt
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
                            customers.append(item0)
book=xlwt.Workbook()
sheet=book.add_sheet('sheet1')
sheet.write(0,0,'name')
sheet.write(0,1,'rank')
sheet.write(0,2,'CompanyIndex')
i=1
for item in customers:
    sheet.write(i,0,item.name)
    sheet.write(i,1,item.rank)
    sheet.write(i,2,item.CompIndex)
    i=i+1
book.save("C:\\Users\\Sandy Lin\\Desktop\\result.xls")