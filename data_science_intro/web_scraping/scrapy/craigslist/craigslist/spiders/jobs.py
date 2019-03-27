# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['washingtondc.craigslist.org'] # may need to be removed
    start_urls = ['https://washingtondc.craigslist.org/d/software-qa-dba-etc/search/nva/sof']

    def parse(self, response):
        listings = response.xpath('//li[@class="result-row"]')
        for listing in listings:
            date = listing.xpath('.//time[@class="result-date"]/@datetime').extract_first()
            title = listing.xpath('.//*[@class="result-title hdrlnk"]/text()').extract_first()
            url = listing.xpath('.//*[@class="result-title hdrlnk"]/@href').extract_first()

            yield {'date': date,
                   'title': title,
                   'url': url}

        next_page_url = response.xpath('//a[text()="next > "]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

