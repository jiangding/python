# -*- coding: utf-8 -*-
import scrapy
from jd.items import JdItem
from scrapy.http import Request
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    start_urls = [
		#'https://list.tmall.com//search_product.htm?q=%CD%D1%D6%AC%C5%A3%C4%CC&user_id=725677994&type=p&cat=50514008&spm=a3204.7933263.a2227oh.d100&from=chaoshi..pc_1_searchbutton'
		#'https://list.tmall.com//search_product.htm?q=%B0%FC%D7%D3&user_id=725677994&type=p&cat=50514008&spm=a3204.7933263.a2227oh.d100&from=chaoshi..pc_1_searchbutton'
		'https://list.tmall.com//search_product.htm?q=%B4%F3%C3%D7&user_id=725677994&type=p&cat=50514008&spm=a3204.7933263.a2227oh.d100&from=chaoshi..pc_1_searchbutton'
	]

    def parse(self, response):
		nodes = response.xpath('//ul[@id="J_ProductList"]/li')
		for s in nodes:
			yield {
				'price':s.xpath('./div[@class="productInfo"]/div[@class="item-summary"]/div[@class="item-price"]/span/strong/text()').extract(),
				'url':s.xpath('./div[@class="productInfo"]/h3/a/@href').extract(),
				'name':s.xpath('./div[@class="productInfo"]/h3/a/text()').extract()
			}
		# 获取分页
		next_url = response.xpath('//div[@class="page-bottom"]/a[@class="page-next"]/@href').extract()
		self.logger.info(next_url)
		if next_url:
			urls = 'https://list.tmall.com/search_product.htm' + ''.join(next_url)
			yield Request(urls, callback=self.parse)
		
					
		
