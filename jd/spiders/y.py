# -*- coding: utf-8 -*-
import scrapy
from jd.items import JdItem
from scrapy.http import Request
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Spider1Spider(scrapy.Spider):
    name = 'yhd.com'
    start_urls = [
		'http://list.yhd.com/c5266-0-81574/b/a-s1-v4-p1-price-d0-f06-m1-rt0-pid-mid0-k/?tc=3.0.21.6.1&tp=52.5266.1502.0.1.Lp!DaF4-11-F3XOq&ti=G966Fb'
	]

    def parse(self, response):
		nodes = response.xpath('//div[@id="itemSearchList"]/div')
		for s in nodes:
			self.logger.info(s)
			self.logger.info(s.xpath('./div/p[@class="proPrice"]'))
			it = JdItem()
			it['url'] = s.xpath('./div/p[contains(@class,"proName")]/a[starts-with(@id, "pdlink2_")]/@href').extract()
			it['price']	= ''.join(s.xpath('./div/p[@class="proPrice"]/em/text()').extract()).replace(',', '') 
			it['name'] = s.xpath('./div/p[contains(@class,"proName")]/a[starts-with(@id, "pdlink2_")]/text()').extract()
			it['zy'] = s.xpath('./div/p[contains(@class,"storeName")]/a/text()').extract()
			yield {
				'自营':it['zy'],
				'商品链接':it['url'],
				'商品名':it['name'],
				'商品价格':it['price'],
			}

		# 获取分页
		pages = response.xpath('//div[@id="turnPageBottom"]/a')
		# 最大页
		maxPage = response.xpath('//div[@id="turnPageBottom"]/input[@id="pageCountPage"]').extract()
		self.logger.info(maxPage)
		self.logger.info(xmaxPage)
		for p in pages:
			page = ''.join(p.xpath('text()').extract())
			if '下一页'.encode('utf-8') in page :
			    #下一页
				suff = p.xpath('@parameter').extract()
				self.logger.info('1111')
				self.logger.info(suff)
				next_url = ''.join(response.url) + ''.join(suff)
				self.logger.info(next_url)
				yield Request(next_url, callback=self.parse)
				break
					
		
