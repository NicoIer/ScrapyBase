import re
from typing import List
import pandas as pd
import scrapy
import os, sys
from scrapy import Spider, Request
from ..settings import CSV_PATH
from ..items import CommentItem


class CommentSpider(Spider):
    name = 'JComment'

    def __init__(self, csv_path: str = CSV_PATH):
        super(Spider, self).__init__()
        self.data = pd.read_csv(csv_path, index_col=0)

    def start_requests(self):
        for url in list(self.data.loc[:, 'link']):
            yield scrapy.Request(url=url, callback=self.parse, method='GET')

    def parse(self, response, **kwargs):
        comment = CommentItem()
        #
        selector = scrapy.Selector(response)
        comment['id'] = selector.css('#detail > div.tab-con > div:nth-child(1) > div.p-parameter > '
                                     'ul.parameter2.p-parameter-list > li:nth-child(2)::attr(title)').extract_first()
        # 评论词条信息
        infos = selector.css('#comment > div.mc > div.comment-info.J-comment-info')
        # Item解析
        comment['info_list'] = infos.css('div.percent-info > div > span::text').extract()
        comment['percent'] = infos.css('div.comment-percent > div::text').extract_first()
        # 评价好坏信息
        reviews = selector.css('#comment > div.mc > div.J-comments-list.comments-list.ETab > div.tab-main.small > ul')
        # Item解析
        comment['count'] = reviews.css('li.current > a > em::text').extract_first()
        comment['images'] = reviews.css('li:nth-child(2) > a > em::text').extract_first()
        comment['videos'] = reviews.css('li:nth-child(3) > a > em::text').extract_first()
        comment['append'] = reviews.css('li:nth-child(4) > a > em::text').extract_first()
        comment['good'] = reviews.css('li:nth-child(5) > a > em::text').extract_first()
        comment['medium'] = reviews.css('li:nth-child(6) > a > em::text').extract_first()
        comment['bad'] = reviews.css('li:nth-child(7) > a > em::text').extract_first()
        yield comment
