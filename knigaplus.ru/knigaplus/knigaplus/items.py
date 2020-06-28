# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KnigaplusItem(scrapy.Item):
    Url = scrapy.Field()
    Name = scrapy.Field()
    Author = scrapy.Field()
    Price = scrapy.Field()
    img_book = scrapy.Field()
