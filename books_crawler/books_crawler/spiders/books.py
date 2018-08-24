# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BooksSpider(CrawlSpider): # input CrawlSpider to accesss Rules, which gave us LinkExtractor, follow = true will search until each url is found
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = (
        'http://books.toscrape.com/',
    )

    rules = (Rule(LinkExtractor(), callback='parse_page', follow=True),)

    def parse_page(self, response):
        yield{'URL': response.url}

