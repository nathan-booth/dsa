# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['washingtondc.craigslist.org'] # may need to be removed
    start_urls = ['http://washingtondc.craigslist.org/d/software-qa-dba-etc/search/sof']

    def parse(self, response):
        listings = response.xpath('//li[@class="result-row"]')
        for listing in listings:
            date = listing.xpath('.//time[@class="result-date"]/@datetime').extract_first()
            title = listing.xpath('.//*[@class="result-title hdrlnk"]/text()').extract_first()
            url = listing.xpath('.//*[@class="result-title hdrlnk"]/@href').extract_first()

            yield scrapy.Request(url, 
                                 callback=self.parse_listing_page,
                                 meta={'date': date,
                                       'title': title,
                                       'url': url})

        next_page_url = response.xpath('//a[text()="next > "]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

    def parse_listing_page(self, response):
        date = response.meta['date']
        title = response.meta['title']
        url = response.meta['url']
        
        compensation_type = response.xpath('//p[@class="attrgroup"]/span[1]/b/text()').extract_first()
        employment_type = response.xpath('//p[@class="attrgroup"]/span[2]/b/text()').extract_first()
        description = response.xpath('//section[@id="postingbody"]/text()').extract()

        yield {'date': date,
               'title': title,
               'url': url,
               'compensation_type': compensation_type,
               'employment_type': employment_type,
               'description': description}
