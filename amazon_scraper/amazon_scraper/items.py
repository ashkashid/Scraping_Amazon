# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MobileItem(scrapy.Item):
    name = scrapy.Field()
    processor = scrapy.Field()
    ram = scrapy.Field()
    storage = scrapy.Field()
    display = scrapy.Field()
    camera = scrapy.Field()
    battery = scrapy.Field()
