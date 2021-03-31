import scrapy
from AbitSearch.items import SpecItem

class SpecialnostySpider(scrapy.Spider):
    name = 'specialnosty'
    start_urls = ['https://abit-poisk.org.ua/specialities2020/?year=2020&regions=&okrs=2&education_forms=&branches=&directions=&subjects=&univers=&state=0&price_from=0&price_to=0']

    def parse(self, response):
        specialities = response.css("div#specialities div.card div.card-header")
        for item in specialities:
            spec = SpecItem()
            name = item.css("h2 a::text").get()
            spanList = item.css("span::text").getall()
            studyForm = ""

            for i in range(len(spanList)):
                if "форма" in spanList[i]:
                    studyForm = spanList[i].replace("\n","").replace("&bullet;","").strip().replace("  ","")
                    break

            faculty = item.css("span::attr(title)").get()
            countOfRequest = item.css("div.grid div.col-4-12 a::text").get().replace("\n","").strip()
            numOfBudgetPlacesList = item.css("div.subhead-2::text").getall()
            numOfBudgetPlaces = ""
            for i in range(len(numOfBudgetPlacesList)):
                if numOfBudgetPlacesList[i].replace("\n","").replace("&bullet;","").strip().isdigit():
                    numOfBudgetPlaces = numOfBudgetPlacesList[i].replace("\n","").replace("&bullet;","").strip()
                    break
            university = item.css("div a::attr(title)").get()
            spec['name']=name
            spec['studyForm']=studyForm
            spec['faculty']=faculty
            spec['countOfRequest']=countOfRequest
            spec['numOfBudgetPlaces']=numOfBudgetPlaces
            spec['university'] = university
            yield spec
        nextPage = 'https://abit-poisk.org.ua'+response.css("div.card-footer div.content-left a::attr(href)").getall()[-1]
        if nextPage != None:
            yield response.follow(nextPage,self.parse)
