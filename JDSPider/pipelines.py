# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from .items import GoodItem
from scrapy.exceptions import DropItem


class JdspiderPipeline:
    def open_spider(self, spider):
        # print(f'open Spider{spider}')
        pass

    def process_item(self, item, spider):
        # 在这里对数据进行处理 传递到MySQL/MongoDB ....
        return item

    def close_spider(self, spider):
        # print(f'close Spider{spider}')
        pass


'''
class DuplicatePipeline:
    """Item去重"""

    def __init__(self):
        self.item_set = set()

    def process_item(self, item, spider):
        """在这里去重"""
        if isinstance(item, GoodItem):
            if item['link'] in self.item_set:
                raise DropItem('goodItem.link:{} repeat~~'.format(item['link']))
            else:
                self.item_set.add(item['link'])
        return item
'''
