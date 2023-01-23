import scrapy
from w3lib.html import remove_tags
from scrapy.loader.processors import MapCompose, Join, TakeFirst

class FakeplantItem(scrapy.Item):
    title = scrapy.Field(input_processor = MapCompose(remove_tags),
                         output_processor = TakeFirst())
    category = scrapy.Field(input_processor = MapCompose(remove_tags),
                            output_processor = Join())
    tags = scrapy.Field(input_processor = MapCompose(remove_tags),
                        output_processor = Join())
    
