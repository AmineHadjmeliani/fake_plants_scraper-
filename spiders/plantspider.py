import scrapy
from scrapy.loader import ItemLoader 
from ..items import FakeplantItem 

class PlantspiderSpider(scrapy.Spider):
    name = 'plantspider' # spider name
    allowed_domains = ['fake-plants.co.uk'] # allowed domains to crawl
    start_urls = ['https://www.fake-plants.co.uk/'] # starting url

    def parse(self, response):
        # extract links for categories
        for link in response.css("li.product-category a::attr(href)"):
            yield response.follow(link.get(), callback=self.parse_cat)
    
    def parse_cat(self, response):
        # extract links for plants
        for link in response.css("div.astra-shop-thumbnail-wrap a::attr(href)"):
            yield scrapy.Request(link.get(), callback=self.parse_plant)
            
            # extract links for next pages
            next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page :
            yield scrapy.Request(next_page, callback = self.parse_cat)
    
    def parse_plant(self, response):
        # extract plant information
        il = ItemLoader(item=FakeplantItem(), selector=response)
        il.add_css('title', 'h1.product_title.entry-title')
        il.add_css('category', 'span.posted_in a')
        il.add_css('tags', 'span.tagged_as a')
        yield il.load_item() # yield the extracted item
