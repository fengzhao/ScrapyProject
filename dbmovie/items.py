# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()  # 中文名
    rating= scrapy.Field()  # 评分
    inf = scrapy.Field()  # 评论人数
    topid = scrapy.Field()  # 排名序号
