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
            }



        
