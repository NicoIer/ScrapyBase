import pymysql
import pandas as pd
import re
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Float, Integer
import sklearn
import numpy as np


class DealOriginData:
    def __init__(self, good_csv_path, comment_csv_path):
        # 原始数据
        goods = pd.read_csv(good_csv_path)
        comments = pd.read_csv(comment_csv_path)
        # 原始数据的预处理
        goods = goods.drop_duplicates(subset=['id'])
        goods.reset_index(drop=True, inplace=True)
        comments.reset_index(drop=True, inplace=True)
        # 这里需要修改 根据id进行join
        self.data = pd.merge(goods, comments)
        # 处理中间变量
        self.score_columns = [_ for _ in comments.columns if _ not in ['info_list', 'percent', 'id']]
        # 处理工具
        self.num_re = re.compile('[()+]')
        self.info_re = re.compile('[()0-9]')
        # 中间结果
        self.info_list = self._get_infos(comments['info_list'])
        self.info_dict = {key: 0 for key in self.info_list}
        # 自动处理
        # self.process_data()

    def _parse_score_util(self, score_text):
        if str(score_text) == 'nan':
            return ''

        base_str = self.num_re.sub('', score_text)
        point_index = base_str.find('.')
        if point_index != -1:
            return int(base_str.replace('.', '').replace('万', '000'))
        else:
            return int(base_str.replace('万', '0000'))

    def _parse_score(self):
        for column in self.score_columns:
            self.data[column] = self.data[column].map(self._parse_score_util)

    @classmethod
    def _get_infos(cls, series: pd.Series):
        title_re = re.compile('[()0-9]')
        info_list = []
        for infos in series:
            try:
                info_list.extend(title_re.sub('', infos).split(','))
            except TypeError:
                pass
        return list(set(info_list))

    @classmethod
    def _get_pair(cls, pair: str):
        search = re.search('(?P<info>[\u4e00-\u9fa5]*)(?P<num>[0-9]*)', pair)
        return search.group('info'), search.group('num')

    def process_data(self):
        info_data = pd.DataFrame(data=self.info_dict, index=list(range(0, len(self.data))))
        self.data = self.data.join(info_data)
        self._parse_score()
        for index, value in enumerate(self.data['info_list'], 0):
            value = str(value)
            if value == 'nan':
                continue
            else:
                pairs = re.sub('[()]', '', value)
                pair_list = pairs.split(',')
                for pair in pair_list:
                    key, value = self._get_pair(pair)
                    self.data.loc[index, key] = value

        self.data.drop(columns=['info_list'], inplace=True)

    def to_sql(self, host, port, user, password, database, table_name):
        """
        将处理完毕的Pandas数据上传到SQL服务器....就这样吧
        :params MySQL连接的参数
        """
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
        connection = engine.connect()
        self.data.to_sql(name=table_name, con=connection, if_exists='replace', index=False)
        # 根据columns 生成 SQL 列属性字段


if __name__ == '__main__':
    data = DealOriginData('格力空调.csv', 'Comment_格力空调.csv')
    data.process_data()
    data.to_sql(
        host='114.116.48.59',
        port=3306,
        user='nico',
        password='cj2441962996.',
        database='NicoDB',
        table_name='GREE_AIR'
    )
