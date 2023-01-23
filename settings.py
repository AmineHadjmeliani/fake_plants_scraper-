BOT_NAME = 'fakeplant'
SPIDER_MODULES = ['fakeplant.spiders']
NEWSPIDER_MODULE = 'fakeplant.spiders'
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
