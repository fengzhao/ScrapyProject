# -*- coding: utf-8 -*-
import scrapy
from dbmovie.items import  DbmovieItem
import  re

class DoubanSpider(scrapy.Spider):
    name = 'douban_spider'
    # 设置http请求头部为浏览器
    headler = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/61.0.3163.91 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    # 允许爬取的域名，生成spider时就有的一个属性
    allowed_domains = ['douban.com']
    # 开始爬取的url
    start_urls = ['https://movie.douban.com/top250/']


    # 重写scrapy.spider.start_request()方法.
    # def start_requests(self):
    #     # 遍历start_urls中的链接
    #     for url in self.start_urls:
    #     # 通过yield发送Request请求,三个参数：1、url为遍历后的链接，2、发完请求回调parse()处理，3、设置请求头部.
    #         yield  scrapy.Request(url=url,callback=self.parse(response),headers=self.headler)
    def parse(self, response):

        item = DbmovieItem()
        item['title'] = response.xpath('//div[@class="hd"]//span[@class="title"][1]/text()').extract()
        item['rating'] = response.xpath('//div[@class="star"]/span[2]/text()').extract()
        item['inf'] = response.xpath('//span[@class="inq"]/text()').extract()
        item['topid'] = response.xpath('//div[@class="pic"]/em/text()').extract()
        yield  item
        # 遍历所有电影，每部电影的div的class都是item.

        # for quote in response.css('div.item'):
            # 枚举电影名称，评分，引言
            # yield  {"title": quote.css('div.info div.hd a span.title::text').extract_first(),
            #         "rating": quote.css('div.info div.bd div.star span.rating_num::text').extract(),
            #         "inf": quote.css('div.info div.bd p.quote span.inq::text').extract()
            #        }
            # 下一页
        next_url = response.css('div.paginator span.next a::attr(href)').extract()
        if next_url:
            next_url = "https://movie.douban.com/top250" + next_url[0]
            print(next_url)
            yield scrapy.Request(next_url,callback=self.parse ,headers=self.headler)

