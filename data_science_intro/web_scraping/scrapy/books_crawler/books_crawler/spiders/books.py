# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request

def product_info(response, value):
    return response.xpath('//th[text()="' + value + '"]/following-sibling::td/text()').extract_first()

class BooksSpider(Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com'] # twisted doesn't like 'www` in start URLs. I don't know why yet.

    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            abs_url = response.urljoin(book)
            yield Request(abs_url, callback=self.parse_book)

        next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        abs_next_page_url = response.urljoin(next_page_url)
        yield Request(abs_next_page_url)

    def parse_book(self, response):
        title = response.xpath('//h1/text()').extract_first()
        price = response.xpath('//p[@class="price_color"]/text()').extract_first()
        img_url = response.xpath('//img/@src').extract_first()
        img_url = img_url.replace('../..', 'http://books.toscrape.com/')
        rating = response.xpath('//*[contains(@class, "star-rating")]/@class').extract_first().replace('star-rating ', '')
        description = response.xpath('//*[@id="product_description"]/following-sibling::p/text()').extract_first()

        upc = product_info(response, 'UPC')
        product_type = product_info(response, 'Product Type')
        price_without_tax = product_info(response, 'Price (excl. tax)')
        price_with_tax = product_info(response, 'Price (incl. tax)')
        tax = product_info(response, 'Tax')
        availability = product_info(response, 'Availability')
        number_of_reviews = product_info(response, 'Number of reviews')


        yield {
            'title': title,
            'price': price,
            'img_url': img_url,
            'rating': rating,
            'description': description,
            'upc': upc,
            'product_type': product_type,
            'price_without_tax': price_without_tax,
            'price_with_tax': price_with_tax,
            'tax': tax,
            'availability': availability,
            'number_of_reviews': number_of_reviews,
        }