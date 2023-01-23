import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader 
from ..items import FakeplantItem 

class PlantcrawlerSpider(CrawlSpider):
    name = 'plantcrawler'
    allowed_domains = ['fake-plants.co.uk']
    start_urls = ['https://www.fake-plants.co.uk/']
    
    le_plant = LinkExtractor(restrict_css='div.astra-shop-thumbnail-wrap') 
    le_next = LinkExtractor(restrict_css='a.next.page-numbers')
    le_cats = LinkExtractor(restrict_css='li.product-category.product a')
    
    rule_plant = Rule(le_plant, callback='parse_item', follow = False)
    rule_next = Rule(le_next,follow = True)
    rule_cats = Rule(le_cats,follow = True)
    
    rules = (rule_plant,
             rule_next, 
             rule_cats
             )

    def parse_item(self, response):
        il = ItemLoader(item=FakeplantItem(), selector=response)
        il.add_css('title', 'h1.product_title.entry-title')
        il.add_css('category', 'span.posted_in a')
        il.add_css('tags', 'span.tagged_as a')
        yield il.load_item()
