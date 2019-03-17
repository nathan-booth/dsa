# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BooksSpider(CrawlSpider):
    name = 'books'
    start_urls = ['http://books.toscrape.com'] # twisted doesn't like 'www` in start URLs. I don't know why yet.

    rules = (Rule(LinkExtractor(), callback='parse_page', follow=False), )

    def parse_page(self, response):
        pass
