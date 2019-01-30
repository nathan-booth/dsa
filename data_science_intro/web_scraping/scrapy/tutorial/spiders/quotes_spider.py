import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes" #  identifies the Spider.
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        """ a method that will be called to handle the response downloaded for each of the requests made. The response parameter is an instance of TextResponse that holds the page content and has further helpful methods to handle it.
        """
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        next_pg = response.css('li.next a::attr(href)').extract_first()
        if next_pg is not None:
            next_pg = response.urljoin(next_pg)
            yield scrapy.Request(next_pg, callback=self.parse)
