import re
from typing import List

import scrapy
import os, sys
from scrapy import Spider, Request

from ..items import GoodItem


class JdSPider(Spider):
    name = 'JSearch'

    def __init__(self, keyword, max_page: str = '10', **kwargs):
        super(JdSPider, self).__init__()
        self.keyword = keyword
        self.url = 'https://search.jd.com/Search'
        self.max_page = int(max_page)
        #
        self.name_re = re.compile('</font>(?P<name>.*)</em>')

    def start_requests(self):
        for page in range(1, self.max_page + 2):
            meta = {
                'keyword': self.keyword,
                'enc': 'utf-8',
                'page': '{}'.format(page)
            }
            yield scrapy.FormRequest(url=self.url, formdata=meta, callback=self.parse, method='GET')

    def parse(self, response, **kwargs):
        selector = scrapy.Selector(response)

        items: List[scrapy.Selector] = selector.css('#J_goodsList > ul > li')
        for item in items:
            good = GoodItem()
            good['id'] = item.css('::attr(data-sku)').extract_first()
            good['link'] = 'https:{}'.format(item.css('div > div.p-commit > strong > a::attr(href)').extract_first())
            good['price'] = item.css('div > div.p-price > strong > i::text').extract_first()
            try:
                good['name'] = self.name_re.search(item.css('div > div.p-name > a > em').extract_first()).group('name')
            except AttributeError:
                good['name'] = item.css('div > div.p-name > a > em::text').extract_first()
            good['shop_name'] = item.css('div > div.p-shop > span > a::text').extract_first()
            # 增量爬取 当前商品对应评论
            # yield scrapy.Request(good['link'], meta={'good': good}, callback=self.parse_detail)
            yield good
    # def parse_detail(self, response: scrapy.http.HtmlResponse):
    #     good = response.meta['good']
    #     selector = scrapy.Selector(response)
