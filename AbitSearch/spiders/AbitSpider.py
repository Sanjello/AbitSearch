import scrapy


class AbitspiderSpider(scrapy.Spider):
    name = 'AbitSpider'
    allowed_domains = ['https://abit-poisk.org.ua/rate2020']
    start_urls = ['http://https://abit-poisk.org.ua/rate2020/']

    def parse(self, response):
        pass
