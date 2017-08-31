# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector,Selector


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['http://jandan.net/ooxx']
    start_urls = ['http://jandan.net/ooxx']

    def parse(self, response):
        print(response.text)

