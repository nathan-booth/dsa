# -*- coding: utf-8 -*-
import scrapy


class BasicQuotesSpider(scrapy.Spider):
    name = 'quotes0'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quote_text = response.xpath('//*[@class="text"]/text()').extract()
        # equivalent css locator
        # response.css('span.text::text').extract()
        top10_tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        # equivalent css locator
        # response.css('span.tag-item a::text').extract()

        yield {'Quotes': quote_text, 'Top10': top10_tags}
