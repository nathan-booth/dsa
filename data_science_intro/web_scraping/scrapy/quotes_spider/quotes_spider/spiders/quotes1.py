# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    """ This spider will scrape quotes, author, and tags together for each page on the site."""

    name = 'quotes1'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')

        for quote in quotes:
