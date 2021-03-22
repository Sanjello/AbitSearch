import scrapy


class AbitSpider(scrapy.Spider):
    name = 'AbitSpider'
    start_urls = ['http://https://abit-poisk.org.ua/rate2020/']

    def parse(self, response):
        pass
