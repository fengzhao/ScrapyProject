# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from  twisted.enterprise import  adbapi
import pymysql
from dbmovie import  settings
from dbmovie.items import  DbmovieItem
from pymysql import  cursors



class DbmoviePipeline(object):
    def __init__(self):
        db_settings = {
            'host': 'localhost',
            'db': 'douban_movie',
            'user': 'root',
            'password': 'fengzhao',
            'charset': 'utf8',
            'use_unicode': True
        }

        self.dbpool = adbapi.ConnectionPool("pymysql", **db_settings)




    def process_item(self, item, spider):
    # pipeline默认调用

        query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item





    def _conditional_insert(self,cursor, item):
        # print item['name']
        sql ="insert into movie(title,rating,inf) values(%s,%s,%s)"
        length = len(item['topid'])
        for i in range(len(item['topid'])):

            params = (item["title"][i], item["rating"][i],item["inf"][i])
            cursor.excute(sql, params)
            #print("item[title'']")


    def _handle_error(self, cursor, item, spider):
        print (item['name'])
    #     sql = "insert into movie(title,rating,inf) values(%s,%s,%s)"
    #     length = len(item['topid'])
    #     for i in range(len(item['topid'])):
    #         params = (item["title"][i], item["rating"][i], item["inf"][i])
    #         cursor.excute(sql, params)
    #         # print("item[title
            # '']")
    #     #print("item['title']")
