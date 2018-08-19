import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = [
        'http://quotes.toscrape.come/page/1/',
        '/http://quotes.toscrape.com/page/2/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[:2] # checking he url , splitting it by character/extracting number after slash
        # use page variable to define filename
        filename = 'quotes.%s.html' # tutorial has \ page but it I was getting line cont. error
        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('Saved file % s' % filenam) # message to ourself

