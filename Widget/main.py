# -*- coding: utf-8 -*-
import sys
from typing import Union, Any
from PySide6.QtWidgets import QTableWidgetItem
import PySide6
import pandas as pd
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QEventLoop, QTimer, QObject, Qt
from PySide6.QtWidgets import QApplication, QLabel, QWidget
from UIWidget import Ui_Widget, UiTableWidget
from JDSPider.command import command
import multiprocessing
from JDSPider.JDSPider.settings import MONITOR_SEC


class SpiderWidget(QWidget):
    def __init__(self, csv_path):
        super(SpiderWidget, self).__init__()
        # 数据
        try:
            self.data = pd.read_csv(csv_path)
        except FileNotFoundError:
            self.data = None
        self.csv_path = csv_path
        # UI界面
        self.ui = UiTableWidget()
        self.ui.setupUi(self)
        # 消息响应
        self.ui.update_btn.clicked.connect(self.update_clicked)
        # 显示table

    @QtCore.Slot()
    def update_clicked(self):
        self.update_table()

    @QtCore.Slot()
    def update_label(self):
        try:
            if self.data is None:
                self.data = pd.read_csv(self.csv_path)
            # 更新显示值
            self.ui.item_num_label.setText(str(len(self.data.index)))
        except AttributeError:
            pass
        except FileNotFoundError:
            pass

    @QtCore.Slot()
    def update_table(self):
        self.data = pd.read_csv(self.csv_path)
        if self.data is None:
            return
        else:
            self.update_label()
            self.init_table()

    def init_table(self):
        # 更新表单
        self.ui.tableWidget.setRowCount(len(self.data.index))
        self.ui.tableWidget.setColumnCount(len(self.data.columns))
        self.ui.tableWidget.setHorizontalHeaderLabels(list(self.data.columns))

        for row_index, row in self.data.iterrows():
            for col_index, value in enumerate(row.values, 0):
                self.ui.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(value)))


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        # 爬虫进程
        self.good_spider_process = None
        self.comment_spider_process = None
        # Designer UI 界面
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.GoodWidget: SpiderWidget = None
        self.CommentWidget: SpiderWidget = None
        # 监视窗口
        self.good_spider_timer = QTimer(self)
        self.good_spider_timer.timeout.connect(self.good_spider_timer_out)
        #
        self.comment_spider_timer = QTimer(self)
        self.comment_spider_timer.timeout.connect(self.comment_spider_timer_out)

    def comment_spider_timer_out(self):
        if self.comment_spider_process.is_alive():
            pass
        else:
            self.comment_spider_process.join()
            self.comment_spider_timer.stop()
            self.CommentWidget.update_table()
            self.CommentWidget.show()
            self.ui.start_btn.setEnabled(True)

    def good_spider_timer_out(self):
        if self.good_spider_process.is_alive():
            # 这里检测到 进程依旧在执行
            # 更新监视窗口label
            pass
        else:
            # 这里商品爬虫任务结束
            self.good_spider_process.join()
            self.good_spider_timer.stop()
            self.GoodWidget.update_table()
            self.GoodWidget.show()
            # 开始商品详情爬虫任务
            self.comment_spider_process.start()
            self.comment_spider_timer.start(MONITOR_SEC)

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        if self.good_spider_process is None:
            pass
        elif self.good_spider_process.is_alive():
            flag = QtWidgets.QMessageBox().question(self, "警告", "后台任务依旧在执行,确认退出么")
            print((flag == QtWidgets.QMessageBox.StandardButton.Yes))
            if flag == QtWidgets.QMessageBox.StandardButton.Yes:
                self.good_spider_process.terminate()
                self.good_spider_process.join()
            else:
                return event.ignore()
        return None

    @QtCore.Slot()
    def start_spider(self):
        if self.ui.keyword_edit.text() == '':
            keyword = self.ui.keyword_edit.placeholderText()
        else:
            keyword = self.ui.keyword_edit.text()
        if self.ui.maxpage_edit.text() == '':
            max_page = self.ui.maxpage_edit.placeholderText()
        else:
            max_page = self.ui.maxpage_edit.text()
        if self.ui.save_path_edit.text() == '':
            save = self.ui.save_path_edit.placeholderText()
        else:
            save = self.ui.save_path_edit.text()

        # 开一个新进程执行 shell
        self.good_spider_process = multiprocessing.Process(name='GoodSpider', target=command.start_good_spider,
                                                           args=(keyword, max_page, save))
        self.good_spider_process.start()
        # 预备一个进程用于执行 comment shell
        self.comment_spider_process = multiprocessing.Process(name='CommentSpider', target=command.start_comment_spider,
                                                              args=(save, 'Comment_{}.csv'.format(keyword)))
        # 打开监视器 开启监视窗口
        self.good_spider_timer.start(MONITOR_SEC)
        self.GoodWidget = SpiderWidget(save)
        self.CommentWidget = SpiderWidget('Comment_{}.csv'.format(keyword))
        # 打开一个加载窗口...提示正在爬取
        self.ui.start_btn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    app.exec()
