#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy,json
from jd.items import JdItem
from scrapy.http import Request
from scrapy_splash import SplashRequest
import sys
import urllib2
import urllib
import time
import xlsxwriter as wx
from openpyxl import Workbook
reload(sys)
sys.setdefaultencoding('utf8')

class Spider1Spider(scrapy.Spider):
	# cookies = """
	# 	user-key=48d19681-5daf-490e-b2e5-d560c0eda94e; cn=0; __jdv=122270672|direct|-|none|-|1500531405987; mt_xid=V2_52007VwMXWl1fUVgaSBBUAm4DFVVbUVFTGk0ZbFY0ABNRDVwGRk9KEVgZYgoXAEFQVg8WVRpVAmcGElQOW1JSSnkaXQVhHxNUQVtWSx9NEl4EbAcSYl9oUmofSBhbDGcEGlFtWFdcGA%3D%3D; mx=0_X; ipLocation=%u5E7F%u4E1C; areaId=19; ipLoc-djd=19-1601-3633-0; _jrda=3; _jrdb=1501063911685; wlfstk_smdl=ulyitd2j842zbi5cnryrmgojahneybds; TrackID=1GIOyWkg-srri0U3AtBq3unPpW6rEsaSOZvEBzGOtvhPyd_udjGgmV-x0OUcnTetttnYELcmvcEI0dCG50OQpVkYxhSPyyBY8FNZmkG3MYBA; pinId=--iZ70m20Kkay1Zok1eEqw; pin=%E5%B0%8F%E6%98%8E%E6%9D%A5%E4%B9%B0%E4%B9%A6; unick=%E5%B0%8F%E6%98%8E%E6%9D%A5%E4%B9%B0%E4%B9%A6; thor=9A0AB0EAD99538C98F857AB0EFAC4D1ACE555EE2027D17204DBC3F6CAC75226B256CC189E353CABB20B19E7DBD2B3B6BB17897B96917768A8F54BFE8B6123B53C146367C1EFF7290EF8BB2001C05BB89DFD31AC7BF213F6EECC62EC194BAA2428415A8A2F3C9676C1916FCB80BDDF5A8194518F8296F406C052AE81A97355C69; _tp=e2gWXtW0yroTedlUzd158waZlVn%2BghFjzD%2BbcDBNcBxvtsGg1tS%2B71DJ4hHjo%2BEB; _pst=%E5%B0%8F%E6%98%8E%E6%9D%A5%E4%B9%B0%E4%B9%A6; ceshi3.com=000; __jda=122270672.14916234089681667828451.1491623408.1501057500.1501062167.101; __jdb=122270672.23.14916234089681667828451|101.1501062167; __jdc=122270672; rkv=V0600; xtest=4086.cf6b6759; __jdu=14916234089681667828451; 3AB9D23F7A4B3C9B=IASUP7B6GNTBHZNLSIYUUPXVJBEPSHFPYZ4TZMBU2QJIA2SAQHW3523VF6DT62LEQTC5ITMSGZI3DNSXO6SFEGJALQ
	# """
	idx = 1
	workbook = wx.Workbook('./dd1.xlsx')
	worksheet = workbook.add_worksheet()
	name = 'jdjdbar'
	start_urls=[
		#'http://search.jd.com/Search?keyword=%E9%86%8B&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%86%8B&wtype=1&click=2',

		'http://search.jd.com/Search?keyword=%E8%B0%B7%E7%89%A9&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%B0%B7%E7%89%A9&wtype=1&click=1'
	]
	def start_requests(self):

		script = """
		function main(splash)
			splash:go(splash.args.url)
			splash:autoload("https://code.jquery.com/jquery-2.1.3.min.js")
			splash:runjs("$('html,body').animate({scrollTop:$(document).height()},100)")
			splash:wait(0.5)
			return splash:html()
		end
		"""
		splash_args = {
			'wait': 2,
			'lua_source': script,
			# "cookies":self.cookies,
			#"http_method":"GET",
			# "images":0,
			#"timeout":800,
			#"render_all":1,			
			#"headers":headers,
			# "proxy":"http://101.200.153.236:8123",
		}
		for url in self.start_urls:
			yield SplashRequest(url,self.parse,endpoint='execute',args=splash_args)
	def parse(self, response):
		nodes = response.xpath('//div[@id="J_goodsList"]/ul/li')
		for s in nodes:
			it = JdItem()
			it['url'] = s.xpath('./div/div[contains(@class,"p-name")]/a//@href').extract()
			it['price']	= s.xpath('./div/div[@class="p-price"]/strong/i/text()').extract()
			data = s.xpath('./div/div[contains(@class,"p-name")]/a/em')
			it['name'] = data.xpath('string(.)').extract()
			it['zy'] = s.xpath('./div/div[@class="p-icons"]/img/@data-tips').extract()
			r =  Request('http:' + it['url'][0], self.parse_img)
			r.meta['itmod'] = it
			yield r

		# 获取分页
		nxt = response.xpath('//div[@id="J_bottomPage"]/span[@class="p-num"]/a[@class="pn-next"]')
		if nxt:
			cur = response.xpath('//div[@id="J_bottomPage"]/span[@class="p-num"]/a[@class="curr"]/text()').extract()[0]
			self.logger.info(int(cur))
			s = 60 * int(cur) + 1
			d = (int(cur)+1) * 2 - 1
			next_url = ''.join(self.start_urls[0]) + '&page=%d&s=%d' % (d, s)
			script = """
			function main(splash)
				splash:go(splash.args.url)
				splash:autoload("https://code.jquery.com/jquery-2.1.3.min.js")
				splash:runjs("$('html,body').animate({scrollTop:$(document).height()},100)")
				splash:wait(0.5)
				return splash:html()
			end
			"""
			self.logger.info(next_url)
			yield SplashRequest(next_url,self.parse,endpoint='execute', args={'wait':2,'lua_source': script})
		else:
			self.workbook.close()

	def parse_img(self, response):
 		it = response.meta['itmod']
		pic = response.xpath('//div[@id="spec-n1"]/img/@data-origin').extract()
		if pic:
			pass
		else:
			pic = response.xpath('//div[@id="spec-n1"]/img/@src').extract()

		smallPic = response.xpath('//div[@id="spec-list"]/ul/li[@class="img-hover"]/img/@src').extract()[0]
		#name = response.xpath('//div[@class="itemInfo-wrap"]/div[@class="sku-name"]/text()')
		if smallPic:
			picurl = 'http:' + smallPic
			content = urllib2.urlopen(picurl).read()
			picNo = smallPic[-21:-3]
			path = '././images/jd/%sjpg' % picNo
			with open(path, 'wb') as f:
				f.write(content)
		else:
			pass

		if self.idx == 1:
			self.worksheet.write('A1', '图片')
			self.worksheet.write('B1', '商品名')
			self.worksheet.write('C1', '价格')
			self.worksheet.write('D1', '地址')
			self.worksheet.write('E1', '自营')
			self.worksheet.write('F1', '图片地址')
		self.idx += 1
		i = str(self.idx)
		self.worksheet.insert_image('A'+i,path)		
		self.worksheet.write('B'+i,it['name'][0])
		self.worksheet.write('C'+i,it['price'][0])
		self.worksheet.write('D'+i,it['url'][0])
		if it['zy']:							
			self.worksheet.write('E'+i,it['zy'][0])
		else:
			self.worksheet.write('E'+i,'')
		self.worksheet.write('F'+i,pic[0])
