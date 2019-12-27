# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:46:50 2019

@author: Sandy Lin
"""

from urllib.parse import urlencode
import requests
from StockHD import StockHD
target_date=['2019-09-30','2018-09-30','2016-09-30']
def get_page(i,target=None):
    base_url="http://data.eastmoney.com/DataCenter_V3/gdfx/stockholder.ashx?"
    headers={
        'Host': 'data.eastmoney.com',
'Referer': 'http://data.eastmoney.com/gdfx/stock/'+target+'.html',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
        }
    params={
            'code':target,
            'date':target_date[i],
            'type':'Sd',
            }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
            print('Error',e.args)
from pyquery import PyQuery as pq
def parse_page(json,target):
    result=[]
    if json:
        data=json.get('data')
        for item in data:
            StockHolder=StockHD()
            StockHolder.CompIndex=target
            StockHolder.name=item.get('SHAREHDNAME')
            StockHolder.rank=item.get('RANK')
            result.append(StockHolder)
    return result