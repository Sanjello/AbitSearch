import scrapy
from AbitSearch.items import UniversityItem

class UniversitySpider(scrapy.Spider):
    name = "university"
    start_urls = ["https://abit-poisk.org.ua/rate2020/region/3"]

    def parse(self, response):
        uni = UniversityItem()
        uni_count = len(response.xpath('/html/body//*[@class="table table-bordered"]/tbody/tr'))-2
        for i in range(uni_count):
            uni["name"] = response.xpath('/html/body//*[@class="table table-bordered"]/tbody/tr/td/a/text()')[i].getall()[0]
            uni["region"] = response.xpath('/html/body//*[contains(@class, "main-content")]/div[2]/div/div/div/div/h1/text()').getall()[0].split(' ')[2]
            uni["all_places"] = response.xpath('/html/body//*[@class="table table-bordered"]/tbody/tr/td[3]/text()')[i].getall()[0].strip()
            uni["budget_places"] = response.xpath('/html/body//*[@class="table table-bordered"]/tbody/tr/td[2]/text()')[i].getall()[0].strip()
            uni["applications"] = response.xpath('/html/body//*[@class="table table-bordered"]/tbody/tr/td[4]/text()')[i].getall()[0].strip()
            uni["original_applications"] = response.xpath('/html/body//*[@class="table table-bordered"]/tbody/tr/td[5]/text()')[i].getall()[0].strip()
            yield uni
        for j in range(3, 27): # go through 50 pages
            yield response.follow(f"https://abit-poisk.org.ua/rate2020/region/{j}", callback=self.parse)