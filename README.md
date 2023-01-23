fake-plants scaper

This tutorial is for those new to Scrapy and aims to provide a comprehensive guide on how to create your first spider project using Python3. It covers the basics of crawling with a basic spider and walks you through building a complete tutorial project, including exporting the data to a CSV file. The tutorial will teach you how to scrape product names and prices from an online shop and also how to use the Scrapy shell to parse data, extract text and href attributes from HTML, and scrape multiple pages.

In the first Spider we would be using Crawlspider method for crawling the website "fake-plants.co.uk". The spider is called "PlantcrawlerSpider" and it inherits from the "CrawlSpider" class. The spider is set to only crawl the allowed domain "fake-plants.co.uk" and it starts from the URL "https://www.fake-plants.co.uk/".
The spider uses three LinkExtractor objects to extract links for plants, next pages, and categories. It also uses three Rule objects to follow the extracted links and parse the information of each plant page by calling the parse_item method. In the parse_item method, it uses an ItemLoader to extract the title, category, and tags of each plant and yield the item.


In the second spider we would be using the basic spider 
