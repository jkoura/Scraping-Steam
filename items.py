# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted Data - Temporary containers
import scrapy


class WorkshopCommentsItem(scrapy.Item):
    # define the fields for your item here like:
    # post_author = scrapy.Field()
    post_time = scrapy.Field()
    post_content = scrapy.Field()
    post_author = scrapy.Field()
