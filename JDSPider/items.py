# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GoodItem(scrapy.Item):
    name, price, id = [Field()] * 3
    link = Field()
    shop_name = Field()


class CommentItem(scrapy.Item):
    id = Field()
    info_list = scrapy.Field()
    percent = scrapy.Field()

    count = scrapy.Field()
    images, videos, append = [Field()] * 3
    good, medium, bad = [Field()] * 3
