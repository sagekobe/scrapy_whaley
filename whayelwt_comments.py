# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 18:49:17 2017

@author: wim
"""
import codecs
from bs4 import BeautifulSoup
import requests
import urllib
import urllib2
import re
import pandas as pd


#天猫网页使用了ajax加密，可以在检查元素里的networks--all--Headers里找到 存放评论的网址（name一栏中）
#有些网站可能采用post 请求，因此需要自己提供post的方式查询信息

f1=codecs.open('ccc.json','a')
#N表示总的翻页数
N=9
for i in range(N):
    url='https://rate.tmall.com/list_detail_rate.htm?itemId=546667830469&spuId=849493276&sellerId=2526854452&order=3&currentPage={}'
    url=url.format(str(i+1))
    res=requests.get(url)

#通过此url获得内容为 JSON的轻量级数据交换格式，页面中的方括号[]里边的内容，才是一个正确的JSON规范文本
    my=re.findall('"rateList":(.+),"searchinfo":"","tags"',res.text)[0]

#以json的格式读取,mytable是一个19乘42的表 datframe格式
    mytable=pd.read_json(my)

#写入json
    mytable['rateContent'].to_json(f1,force_ascii=False)
    
f1.close()
    
