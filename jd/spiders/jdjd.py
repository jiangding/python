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
	endIdx = 0
	workbook = wx.Workbook('./d1.xlsx')
	worksheet = workbook.add_worksheet()
	name = 'jdjd'
	start_urls=[
		'牛肉干','辣条'
		# '休闲零食','饼干','蛋糕','橄榄油','坚果蜜饯','糖果','进口牛奶','方便食品','饮料冲调',
		# '进口食品','猪肉脯','薯片','鸭脖','海苔','牛肉干','果蔬干','果冻','辣条',
		# '进口饼干','曲奇','面包','蛋糕','饼干','派','蛋卷','威化','肉松饼',
		# '瓜子','核桃','夏威夷果','松子','开心果','碧根果','腰果','巴旦木','花生',
		# '枣夹核桃','枣','葡萄干','芒果干','梅','山楂','枸杞','蔓越莓干','栗子','薯干',
		# '进口巧克力','巧克力','口香糖','棒棒糖','喜糖','糖','润喉糖','黑巧克力',
		# '进口牛奶','牛奶','酸奶','风味奶','儿童奶','鲜奶','成人奶粉','乳酸饮料',
		# '铁观音','乌龙茶','龙井','普洱','红茶','绿茶','白茶','黑茶','养生茶','花果茶','花草茶',
		# '饮用水','碳酸','中草药饮料','功能饮料','运动饮料','茶饮','蛋白质饮料','果蔬饮料','果味饮料',
		# '麦片','咖啡','奶茶','蜂蜜','蜂产品','柚子茶','营养奶粉','谷粉豆浆',
		# '椰子油','橄榄油','调和油','玉米油','葵花籽油','花生油','大豆油','菜籽油','茶油',
		# '东北大米','籼米','五常大米','进口大米','稻花香','面粉','挂面',
		# '小米','红小豆','黄豆','薏米','绿豆','黑米','糯米','黑芝麻','杂粮礼盒',
		# '酱油','醋','盐','白糖','红糖','烘焙原料','味精','复合调味料','香油',
		# '方便面','方便米饭','火腿肠','罐头','八宝粥','速食汤','粥麦片','谷物','方便粉丝',
		# '老干妈','香辣酱','辣椒酱','豆瓣酱','番茄酱','花生酱','香菇酱','拌饭酱','沙拉酱',
		# '洗发','护发','染发','造型','沐浴露','剃须刀','牙刷','牙膏','牙线','卫生巾','私密护理','香皂','纸巾','洗衣粉','洗手液','洗洁精'
	]
	def start_requests(self):
		script = """
		function main(splash)
			splash:go(splash.args.url)
			splash:autoload("https://code.jquery.com/jquery-2.1.3.min.js")
			splash:runjs("$('html,body').animate({scrollTop:$(document).height()},200)")
			splash:wait(3.0)
			return splash:html()
		end
		"""
		splash_args = {
			'wait': 5,
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
			myUrl = "https://search.jd.com/Search?keyword=%s&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wtype=1&click=1&page=1&s=1" % url
			yield SplashRequest(myUrl,self.parse,endpoint='execute',args=splash_args)
	def parse(self, response):
		nodes = response.xpath('//div[@id="J_goodsList"]/ul/li')
		for s in nodes:
			it = JdItem()
			it['url'] = s.xpath('./div/div[contains(@class,"p-name")]/a//@href').extract()
			it['price']	= s.xpath('./div/div[@class="p-price"]/strong/i/text()').extract()
			data = s.xpath('./div/div[contains(@class,"p-name")]/a/em')
			it['name'] = data.xpath('string(.)').extract()
			it['zy'] = s.xpath('./div/div[@class="p-icons"]/i[contains(@class,"goods-icons J-picon-tips J-picon-fix")]/text()').extract()
			if it['url']:
				if "http" in it['url'][0]:
					r = Request(it['url'][0], self.parse_img)
				else:		
					r = Request('http:' + it['url'][0], self.parse_img)
				r.meta['itmod'] = it
				yield r
			else:
				pass
		# 获取分页
		cur = response.xpath('//div[@id="J_bottomPage"]/span[@class="p-num"]/a[@class="curr"]/text()').extract()
		if cur:
			cur = cur[0]
			s = 60 * int(cur) + 1
			d = (int(cur)+1) * 2 - 1
			#next_url = ''.join(response.url) + '&page=%d&s=%d' % (d, s)
			# 截取字符串算出下一页
			next_url = ''.join(response.url).split('&page=')[0] + '&page=%d&s=%d' % (d, s)
			script = """
			function main(splash)
				splash:go(splash.args.url)
				splash:autoload("https://code.jquery.com/jquery-2.1.3.min.js")
				splash:runjs("$('html,body').animate({scrollTop:$(document).height()},200)")
				splash:wait(3.0)
				return splash:html()
			end
			"""
			yield SplashRequest(next_url,self.parse,endpoint='execute', args={'wait':5,'lua_source': script})
		else:
			self.endIdx += 1
			totalcount = len(self.start_urls)
			self.logger.info(totalcount)
			self.logger.info(self.endIdx)
			if totalcount <= self.endIdx :
				self.workbook.close()

	def parse_img(self, response):
 		it = response.meta['itmod']
		pic = response.xpath('//div[@id="spec-n1"]/img/@data-origin').extract()
		linkUrl = response.xpath('//head/link[@rel="canonical"]/@href').extract()
		if pic:
			pass
		else:
			pic = response.xpath('//div[@id="spec-n1"]/img/@src').extract()

		smallPic = response.xpath('//div[@id="spec-list"]/ul/li[@class="img-hover"]/img/@src').extract()
		if smallPic :
			smallPic = smallPic[0]
		else:
			smallPic = response.xpath('//ul/li/img[@class="img-hover"]/@src').extract()[0]
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
		if it['name']:		
			self.worksheet.write('B'+i,it['name'][0])
		if it['price']:
			self.worksheet.write('C'+i,it['price'][0])
		if linkUrl:
			self.worksheet.write('D'+i,linkUrl[0])
		if it['zy']:							
			self.worksheet.write('E'+i,it['zy'][0])
		self.worksheet.write('F'+i,pic[0])
