import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = 'xkcd'
    start_urls = []
    url = 'https://xkcd.com/'

    for comic_number in range(1, 50): # 1st 50 comics
        start_urls.append(url + str(comic_number) + '/')

    def parse(self, response):
        dict = {
                'title' : response.css('title::text').extract_first()[6:],
                'comic_txt' : response.css('#comic').extract_first().split('""')[5][1:],
                'source' : response.css('#comic').extract_first.split('""')[-2][:-3]
        }
        with open('xkcd_comics.json', 'a') as fh:
            fh.write(json.dumps(dict) + '\n')
