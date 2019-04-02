# -*- coding: utf-8 -*-
import scrapy


class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    # allowed_domains = ['class-central.com']
    start_urls = ['https://class-central.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject: 
            subject_url = response.xpath('//*[contains(@title, "' + self.subject + '")]/@href').extract_first()

            yield scrapy.Request(response.urljoin(subject_url), callback=self.parse_subject)

        else: 
            self.logger.info('Scraping all subjects...')
            subjects = response.xpath('//*[@class="text--blue"]/@href').extract()
            for subject in subjects:
                yield scrapy.Request(response.urljoin(subject), callback=self.parse_subject)

    def parse_subject(self, response):
        subject = response.xpath('//title/text()').extract_first().split('|')[0].split()[1:]
        subject = ' '.join(subject)

        courses = response.xpath('//*[@class="text--charcoal text-2 medium-up-text-1 block course-name"]')
        for course in courses:
            course_title = course.xpath('.//@title').extract_first()
            course_url = course.xpath('.//@href').extract_first()
            abs_course_url = response.urljoin(course_url)

            yield {
                'subject': subject,
                'course_title': course_title,
                'abs_course_url': abs_course_url
            }