# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['washingtondc.craigslist.org'] # may need to be removed
    start_urls = ['https://washingtondc.craigslist.org/d/software-qa-dba-etc/search/nva/sof']

    def parse(self, response):
        pass
