# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LoginItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Requester = scrapy.Field()
    Title = scrapy.Field()
    HITs = scrapy.Field()
    Reward = scrapy.Field()
    Created = scrapy.Field()
    Actions = scrapy.Field()
    Description = scrapy.Field()
    TimeAllotted = scrapy.Field()
    Expires = scrapy.Field()
    # pass
