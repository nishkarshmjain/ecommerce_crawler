import scrapy
from bs4 import BeautifulSoup
import re
from ..items import EcomCrawlerItem


class EcomspiderSpider(scrapy.Spider):
    name = 'ecomspider'
    allowed_domains = ['www.matchesfashion.com']
    start_urls = ['https://www.matchesfashion.com/intl/mens/shop/shoes?page='+str(i+1)
                  for i in range(7)]
    handle_httpstatus_list = [403]

    #def parse(self, response):
     #   pass

    #def __init__(self):
    #    self.declare_xpath()

    #def declare_xpath(self):
        #self.getAllCategoriesXpath = ""
        #self.getAllSubCategoriesXpath = ""
        #self.getAllItemsXpath = ""
        #self.TitleXpath  = "//*[contains(concat( " ", @class, " " ), concat( " ", "lister__item__details", " " ))]"
        #self.BrandXpath = "//*[contains(concat( " ", @class, " " ), concat( " ", "lister__item__title", " " ))]"
        #self.PriceXpath = "//*[contains(concat( " ", @class, " " ), concat( " ", "lister__item__price-full", " " ))]"
        #self.ImageUrlXpath = "//*+[contains(concat( " ", @class, " " ), concat( " ", "lister__item", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "lister__item", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "lazy", " " ))]"

    def parse(self,response):
        item = EcomCrawlerItem()
        
        Title = response.css(".lister__item__title::text").extract()
        Brand = response.css(".lister__item__title::text").extract()
        Price = response.css(".lister__item__price-full::text").extract()
        Image_Url = response.css(".lazy::attr(data-original)").extract()
        Product_Url = response.css(".productMainLink::attr(href)").extract()


        #Put each element into its item attribute.
        item['Name']           = Title
        item['Brand']          = Brand
        item['Price']          = Price
        item['Image_Url']       = Image_Url
        string = "https://www.matchesfashion.com"
        Product_Url = [string + x for x in Product_Url]
        item['Product_Url']     = Product_Url
        return item
 