import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes2"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = (
        "http://quotes.toscrape.com/",
        )

    def parse(self, response):
        #h1_tag = response.xpath('//h1/a/text()').extract_first()
        #tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        quoted = response.xpath('//*[@class="quote"]')# find everyclass instance that has the value of the quote
        for quote in quoted:
            text = quoted.xpath('.//*[@class="text"]/text()').extract_first() # we found htis in our shell, pulls out clean text of quote
            author = quoted.xpath('.//*[@itemprop="author"]/text()').extract_first()# find every value with the item prop of author
            tags = quoted.xpath('.//*[@class="tag"]/text()').extract()
            
            print(text)
            print(author)
            print(tags)
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()# returns link/value of next page url which we will use below
        absolute_next_page_url = response.urljoin(next_page_url) # here we are grabbing the next page url that we found / stored in variable above  
        yield scrapy.Request(absolute_next_page_url)        
    
        

    
