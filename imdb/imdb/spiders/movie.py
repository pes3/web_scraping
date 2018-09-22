# -*- coding: utf-8 -*-
import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['https://www.imdb.com/search/title?start=1']
    start_urls = ['https://www.imdb.com/search/title?start=1/']

    def parse(self, response):
        titles = response.xpath('//div[@class="lister-item mode-advanced"]') # grabbing top div class, that encapsulates the below

        for subject in titles:
            yield {
                'Title': subject.xpath('.//h3[@class="lister-item-header"]/a/text()').extract_first(),
                'Runtime': subject.xpath('.//span[@class="runtime"]/text()').extract_first(),
                'Description': subject.xpath('.//p[@class="text-muted"]/text()').extract_first(),
                'Director': subject.xpath('.//p[contains(text(),"Director")]/a[1]/text()').extract_first(),
                'Gross Revenue': subject.xpath('.//span[@name="nv" and contains(text(), "$")]/text()').extract_first(),
                'Rating': subject.xpath('.//div[@class="inline-block ratings-imdb-rating"]/strong/text()').extract_first(),
            }



        
