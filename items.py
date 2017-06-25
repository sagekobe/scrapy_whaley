# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WhaleywtItem(scrapy.Item):
    # define the fields for your item here like:
    sales = scrapy.Field()
    comments_number = scrapy.Field()
    price = scrapy.Field()
    products_name = scrapy.Field()
    
