#!/usr/bin/python  
#-*-coding:utf-8-*-  

import scrapy
import re
from whaleywt.items import WhaleywtItem

class MySpider(scrapy.Spider):
    name='MySpider'
    start_urls=['https://list.tmall.com/search_product.htm?q=%CE%A2%BE%A8%CE%A2%CD%B6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton']
    
#    def start_requests(self):
#        url = "http://db.bioon.com/list.php?channelid=1016&classid=951"
#        cookies = {
#            'dz_username':'wst_today',
#            'dz_uid':'1322052',
#            'buc_key':'ofR1I78RBaCHkGp8MdBBRjMx7ustawtY',
#            'buc_token':'a91b8fef55c66846d3975a9fd8883455'
#             }
#        return [
#            scrapy.Request(url,cookies=cookies),
#        ]
#    
    def parse(self,response):
        item=WhaleywtItem()
        #root
        contents=response.xpath('//*[@id="J_ItemList"]/div')
        
        for box in contents:
            item['price'] = box.xpath('*/p[1]/em/text()').extract()
            #extract name by re
            item['sales'] =  box.xpath('*/p[3]/span[1]/em/text()').extract()[0]     
            name = box.xpath('*/p[2]/a').extract()[0]
            namere = re.findall(r'title="(.+)" data-p', name)
            item['products_name'] = namere
            item['comments_number'] = box.xpath('*/p[3]/span[2]/a/text()').extract()
                   
            yield item

