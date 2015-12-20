# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from datetime import datetime
from yelp.items import YelpItem

class YelpspiderSpider(scrapy.Spider):
    name = "yelpspider"
    allowed_domains = ["yelp.de"]
    start_urls = (
        # 'http://www.yelp.de/',
        "http://www.yelp.de/search?find_desc=McDonald's&find_loc=berlin&start=10",
    )
    base_url = 'http://www.yelp.de'
    def parse(self, response):
    	print "here"
    	hxs = Selector(response)

    	biz_urls = hxs.xpath('//a[@class="biz-name"]/@href').extract()
    	for biz_url in biz_urls:
    		yield Request(self.base_url+biz_url,self.parse_link,dont_filter=True)

    	#pagination
    	next_url = hxs.xpath('//a[@class="page-option prev-next next"]/@href').extract()
    	if next_url:
    		next_url = next_url[0]
    		yield Request(self.base_url+next_url,self.parse,dont_filter=True)

    def parse_link(self, response):
    	print response.url
    	hxs = Selector(response)
    	f = open('check.html','wb')
    	f.write(response.body)

    	item = YelpItem()

    	item['url'] = response.url
    	print item
    	item['date_created'] = datetime.now()

    	rating_stars = hxs.xpath('//div[@class="rating-very-large"]/i/@title').extract()
    	if rating_stars:
    		item['rating_stars'] = rating_stars[0].encode('utf-8')
    	

    	review_count = hxs.xpath('//span[@itemprop="reviewCount"]/text()').extract()
    	if review_count:
    		item['review_count'] = review_count


    	street_address = hxs.xpath('//span[@itemprop="streetAddress"]/text()').extract()
    	if street_address:
    		item['street_address'] = street_address    		

    	address_locality = hxs.xpath('//span[@itemprop="addressLocality"]/text()').extract()
    	if address_locality:
    		item['address_locality'] = address_locality

    	postal_code = hxs.xpath('//span[@itemprop="postalCode"]/text()').extract()
    	if postal_code:
    		item['postal_code'] = postal_code


    	hours_range = hxs.xpath('//span[@class="hour-range"]//text()').extract()
    	if hours_range:
    		item['hours_range'] = hours_range

    	price_range =  hxs.xpath('normalize-space(//dd[@class="nowrap price-description"]//text())').extract()
    	if price_range:
    		item['price_range'] = ' '.join(price_range)
    	

    	image_url = hxs.xpath('//div[@class="showcase-photo-box"]/a/img/@src').extract()
    	if image_url:
    		item['image_url'] = image_url    	

    	phone = hxs.xpath('//span[@class="biz-phone"]/text()').extract()
    	if phone:
    		item['phone'] = phone

    	# print item
    	print item
    	yield item
    	
