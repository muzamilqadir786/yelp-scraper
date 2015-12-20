# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YelpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    date_created = scrapy.Field()
    rating_stars = scrapy.Field()
    review_count = scrapy.Field()
    street_address = scrapy.Field()
    address_locality = scrapy.Field()
    postal_code = scrapy.Field()
    hours_range = scrapy.Field()
    price_range = scrapy.Field()
    phone = scrapy.Field()
    image_url = scrapy.Field()


