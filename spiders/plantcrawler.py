import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader 
from ..items import FakeplantItem 

class PlantcrawlerSpider(CrawlSpider):
    name = 'plantcrawler' # spider name
    allowed_domains = ['fake-plants.co.uk'] # allowed domains to crawl
    start_urls = ['https://www.fake-plants.co.uk/'] # starting url

    le_plant = LinkExtractor(restrict_css='div.astra-shop-thumbnail-wrap') # extract links for plants
    le_next = LinkExtractor(restrict_css='a.next.page-numbers') # extract links for next pages
    le_cats = LinkExtractor(restrict_css='li.product-category.product a') # extract links for categories

    rule_plant = Rule(le_plant, callback='parse_item', follow = False) # follow links for plants and call parse_item function
    rule_next = Rule(le_next,follow = True) # follow links for next pages
    rule_cats = Rule(le_cats,follow = True) # follow links for categories

    rules = (rule_plant,
             rule_next, 
             rule_cats
             )

    def parse_item(self, response):
        il = ItemLoader(item=FakeplantItem(), selector=response)
        il.add_css('title', 'h1.product_title.entry-title') # extract plant title
        il.add_css('category', 'span.posted_in a') # extract plant category
        il.add_css('tags', 'span.tagged_as a') # extract plant tags
        yield il.load_item() # yield the extracted item

