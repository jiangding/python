# -*- coding: utf-8 -*-
import scrapy
from jd.items import JdItem
class Spider1Spider(scrapy.Spider):
    name = 'jd.com1'
    start_urls = [
		'https://www.cnblogs.com/#p%d' % i for i in range(1,10)	
	]

    def parse(self, response):
		nodes = response.xpath('//a[contains(@class, "titlelnk")]')
		for s in nodes:	
			it = JdItem()
			it['title'] = s.select('text()').extract()
			it['href']= s.select('@href').extract()
			yield it
