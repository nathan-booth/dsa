# -*- coding: utf-8 -*-
import scrapy
# Import the CrawlerProcess
from scrapy.crawler import CrawlerProcess

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    # allowed_domains = ['datacamp.com/courses/tech:python']
    start_urls = ['http://datacamp.com/courses/tech:python/']

    def start_requests( self ):
      yield scrapy.Request(url = start_urls, callback=self.parse)

    def parse(self, response):
      # My version of the parser you wrote in the previous part
      crs_titles = response.xpath('//h4[contains(@class,"block__title")]/text()').extract()
      crs_descrs = response.xpath('//p[contains(@class,"block__description")]/text()').extract()
      for crs_title, crs_descr in zip( crs_titles, crs_descrs ):
        dc_dict[crs_title] = crs_descr

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(CoursesSpider)
process.start()

# Print a preview of courses
print(dc_dict)
