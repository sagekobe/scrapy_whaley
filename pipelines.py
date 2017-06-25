# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from sqlalchemymodel import Session,whayelinfo

class WhaleywtPipeline(object):
        
    #write into the database
    #open_spider一般用来连接数据库   
    def open_spider(self,spider):
        #Base.metadata.create_all(engine)
        self.session = Session()

    def process_item(self, item, spider):
        coco = whayelinfo(wt_prices=item['price'],wt_sales=item['sales'],wt_names=item["products_name"],wt_comments_number=item["comments_number"])   
        self.session.add(coco)
        self.session.commit()
                
    
    def close_spider(self,spider):
        self.session.close()
        
        
     #write into json file
#    def __init__(self):
#        self.file=codecs.open('data1.json','w',encoding='utf-8')
#    
#    def process_item(self, item, spider):
#        line=json.dumps(dict(item),ensure_ascii=False)+'\n'
#        
#        self.file.write(line)
#        return item