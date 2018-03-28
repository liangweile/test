import re, scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from liangweile.items import LiangweileItem

class Myspider(scrapy.Spider):
    name = 'liangweile'
    allowed_domains = ['23wx.com']
    bash_url = 'http://wwww.23wx.com/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)
        yield Request('http://www.23wx.com/quanben/1', self.parse)
    def parse(self, response):
        print(response.text)
