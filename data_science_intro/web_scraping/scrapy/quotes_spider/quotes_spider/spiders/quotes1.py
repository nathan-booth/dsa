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
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@class="keywords"]/@content').extract_first()
            # similar but returns a list
            # quote.xpath('.//*[@class="tag"]/text()').extract()

            # print(text, "\n", author, "\n", tags, "\n\n")
            yield {'text': text,
                   'author': author,
                   'tags': tags}

        next_page_relative = response.xpath('//*[@class="next"]/a/@href').extract_first()
        next_page_absolute = response.urljoin(next_page_relative)
        yield scrapy.Request(next_page_absolute)
