# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs' # name of the spider
    allowed_domains = ['https://santabarbara.craigslist.org/d/software-qa-dba-etc/search/sof'] # the list of domains the spider is allowed to scrape
    start_urls = ['https://santabarbara.craigslist.org/d/software-qa-dba-etc/search/sof/'] # this list of one or more urls the spider starts crawling

    def parse(self, response): # the main functino of the spider, dont delete but you can add extra funtions
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()#is a [list] of text portions extracted based on a rule.
        # is simply the whole html source code retrieved from the page. Actually, “response” has a deeper meaning because if you print(response) you will get something like <200 https://newyork.craigslist.org/search/egr> which means “you have managed to connect to this web page”; however, if you print(response.body) you will get the whole source code. Anyhow, when you use XPath expressions to extract HTML nodes, you should directly use response.xpath()
        #xpath  is how we will extract portions of text and it has rules.
        #//  means instead of starting from the <html>, just start from the tag that I will specify after it. /a  simply refers to the <a> tag.

        #[@class="result-title hdrlnk"]  that is directly comes after /a means the <a> tag must have this class name in it.

        #text()  refers to the text of the  <a> tag, which is”Chief Engineer”.

        #extract()  means extract every instance on the web page that follows the same XPath rule into a [list].

        #extract_first()  if you use it instead of extract() it will extract only the first item in the list.
        print(titles)
        # run scrapy crawl jobs in terminal/root path
        # this prints the result is a list of Unicode strings. So you can loop on them, and yield one title per time in a form of dictionary.
        for title in titles:
            yield {'Title': title}
        
