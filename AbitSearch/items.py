# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AbitsearchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field  ()
    pass

class UniversityItem(scrapy.Item):
    name = scrapy.Field()
    region = scrapy.Field()
    all_places = scrapy.Field()
    budget_places = scrapy.Field()
    applications = scrapy.Field()
    original_applications = scrapy.Field()

class SpecItem(scrapy.Item):
    name = scrapy.Field()
    studyForm = scrapy.Field()
    faculty = scrapy.Field()
    countOfRequest = scrapy.Field()
    numOfBudgetPlaces = scrapy.Field()
    university = scrapy.Field()


