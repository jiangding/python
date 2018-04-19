# -*- coding: utf-8 -*-

# Scrapy settings for jd project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jd'

SPIDER_MODULES = ['jd.spiders']
NEWSPIDER_MODULE = 'jd.spiders'


SPLASH_URL = 'http://localhost:8050'
FEED_EXPORT_ENCODING = 'utf-8'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jd (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
#	,'Accept-Encoding':'gzip, deflate, br'
#	,'Accept-Language':'zh-CN,zh;q=0.8'
#	,'Cookie':'_med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; x=__ll%3D-1%26_ato%3D0; l=AqqqBg4E34jV3sZ50dNfynNtehtMGy51; pnm_cku822=232UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockp3SnNNc0dySHRAdCI%3D%7CU2xMHDJ7G2AHYg8hAS8XIw0tA18%2BWDRTLVd5L3k%3D%7CVGhXd1llXWBdZFpkUGVfY1djVGlLcEt0S3ZIdE5yR3lGf0tyR2k%2F%7CVWldfS0QMAszBycbLg4gQXEYJkluBXleIFNvSCNfeAt4VgBW%7CVmhIGCUFOBgkHCAUNAw0CTMTLxcpEjIHPAUlGSEfJAQxDjVjNQ%3D%3D%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D; _m_user_unitinfo_=unit|unsz; _m_unitapi_v_=1498717160426; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; sm4=440106; _m_h5_tk=9e7a8265b6b0208b9f8adbaf53aa5ed6_1500965959019; _m_h5_tk_enc=0faa26781e3c46e7c6f598e94615ed42; _tb_token_=c68d7d66c5c55; uc1=cookie14=UoTcDzt7HU4H9g%3D%3D&lng=zh_CN&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie21=W5iHLLyFfoaZ&tag=8&cookie15=URm48syIIVrSKA%3D%3D&pas=0; uc3=sg2=WvdGOW9NC2%2B02U5bsckDVlsi4YOlILVqaV0Fo8guftI%3D&nk2=tyLGo4%2BuV2M%3D&id2=UUGmuTC%2F77wC3g%3D%3D&vt3=F8dBzWOafUmtXXue%2FrA%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; uss=UIX6B3ngJmxPCA24fsHLaQWIiwvb%2FKoDZCE%2BeYqdmxK%2FyBeG671elmZnXg%3D%3D; lgc=%5Cu8D3C%5Cu54C8%5Cu54C8%5Cu567B; tracknick=%5Cu8D3C%5Cu54C8%5Cu54C8%5Cu567B; cookie2=1631429928cfc8aced59d52fc1737e9a; sg=%E5%99%BB75; cookie1=BdTvXGQBPiwx1oB7QtrPd0skJYM%2BJlA4460fi%2FUQTkc%3D; unb=2947356837; t=96fb8612144fddd2a876e4eb15ff3ff8; _l_g_=Ug%3D%3D; _nk_=%5Cu8D3C%5Cu54C8%5Cu54C8%5Cu567B; cookie17=UUGmuTC%2F77wC3g%3D%3D; login=true; tt=login.tmall.com; cna=oU1vEQyMU0sCAbcGrW3UfAae; cq=ccp%3D0; isg=AnZ2naueM7fj0MbRTmpG8XsHx6y4P7x-fLLTAuBfdNn0Ixa9SCcK4dxRT8m0'
#	,'User-Agent':'"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",'
#} 
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
	'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    #'jd.middlewares.JdSpiderMiddleware': 543,
}
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 408]
RETRY_TIMES = 10
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
	'scrapy.downloadermiddlewares.retry.RetryMiddleware':80,
    'scrapy_splash.SplashCookiesMiddleware': 723,  
	'scrapy_splash.SplashMiddleware': 725,  
	'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,  
    #'jd.middlewares.MyCustomDownloaderMiddleware': 543,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jd.pipelines.JdPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
