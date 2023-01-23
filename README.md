# fake-plants scaper

This tutorial is for those new to Scrapy and aims to provide a comprehensive guide on how to create your first spider project using Python3. It covers the basics of crawling with a basic spider and walks you through building a complete tutorial project, including exporting the data to a CSV file. The tutorial will teach you how to scrape product names and prices from an online shop and also how to use the Scrapy shell to parse data, extract text and href attributes from HTML, and scrape multiple pages.

## CrawlSpider
In the first Spider we would be using Crawlspider method for crawling the website "fake-plants.co.uk". The spider is called "PlantcrawlerSpider" and it inherits from the "CrawlSpider" class. The spider is set to only crawl the allowed domain "fake-plants.co.uk" and it starts from the URL "https://www.fake-plants.co.uk/".
The spider uses three LinkExtractor objects to extract links for plants, next pages, and categories. It also uses three Rule objects to follow the extracted links and parse the information of each plant page by calling the parse_item method. In the parse_item method, it uses an ItemLoader to extract the title, category, and tags of each plant and yield the item.

## Basic Spider
In the second spider we would be using the basic spider to crawl the website "fake-plants.co.uk" and extracting information about the plants available on the site. It inherits from the scrapy.Spider class and sets the allowed domains, start URLs, and spider name.
The spider starts by calling the parse function on the start_urls, which extracts links for categories from the website. For each category link, it calls the parse_cat function to extract links for plants and next pages. And for each plant link, it calls the parse_plant function to extract plant information and yield the item.
