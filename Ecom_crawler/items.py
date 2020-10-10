# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EcomCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # define the fields for your item here like:
    Name = scrapy.Field()
    Brand= scrapy.Field()
    Price= scrapy.Field()
    Image_Url = scrapy.Field()
    Product_Url = scrapy.Field()

    pass
