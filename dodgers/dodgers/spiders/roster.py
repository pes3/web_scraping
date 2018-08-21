# -*- coding: utf-8 -*-
import scrapy


class RosterSpider(scrapy.Spider):
    name = 'roster'
    allowed_domains = ['http://www.espn.com/mlb/team/roster/_/name/lad/los-angeles-dodgers']
    start_urls = ['http://www.espn.com/mlb/team/roster/_/name/lad/los-angeles-dodgers/']

    def parse(self, response):
        title = response.css('title::text').extract()
        print(title)
        for i in title:
            yield {'title': title}
