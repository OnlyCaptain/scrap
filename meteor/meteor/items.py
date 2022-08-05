# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeteorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Date = scrapy.Field()
    HighestTemp = scrapy.Field()
    LowestTemp = scrapy.Field()
    Weather = scrapy.Field()
    WindDest = scrapy.Field()
    AirQual = scrapy.Field()
    # pass
