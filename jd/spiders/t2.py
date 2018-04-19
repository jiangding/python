# -*- coding: utf-8 -*-
import scrapy
from jd.items import JdItem
from scrapy.http import Request
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Spider1Spider(scrapy.Spider):
    name = 'jd2.com'
    start_urls = [
		'http://www.cnblogs.com/fnng/default.aspx?page=1'
	]

    def parse(self, response):
		nodes = response.xpath('//div[contains(@class, "post-list-item")]')
		for s in nodes:	
			it = JdItem()
			it['title'] = s.xpath('./h2/a').select('text()').extract()
			it['href']= s.xpath('./h2/a').select('@href').extract()
			yield it
		# 获取分页
		pages = response.xpath('//div[@id="pager"]/a')
		for p in pages:
			page = ''.join(p.xpath('text()').extract())
			if page == '下一页'.encode('utf-8') or 'Next' in page:
				next_url = ''.join(p.xpath('@href').extract())
				self.logger.info(next_url)
				yield Request(next_url, callback=self.parse)
				break
					
		
