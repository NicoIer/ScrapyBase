# -*- coding: utf-8 -*-
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget, QTableWidget)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(311, 98)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.save_path_edit = QLineEdit(Widget)
        self.save_path_edit.setObjectName(u"save_path_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_path_edit.sizePolicy().hasHeightForWidth())
        self.save_path_edit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.save_path_edit, 2, 1, 1, 1)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(10)
        font.setBold(False)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.maxpage_edit = QLineEdit(Widget)
        self.maxpage_edit.setObjectName(u"maxpage_edit")
        sizePolicy.setHeightForWidth(self.maxpage_edit.sizePolicy().hasHeightForWidth())
        self.maxpage_edit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.maxpage_edit, 1, 1, 1, 1)

        self.keyword_edit = QLineEdit(Widget)
        self.keyword_edit.setObjectName(u"keyword_edit")
        sizePolicy.setHeightForWidth(self.keyword_edit.sizePolicy().hasHeightForWidth())
        self.keyword_edit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.keyword_edit, 0, 1, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.start_btn = QPushButton(Widget)
        self.start_btn.setObjectName(u"start_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy2)
        self.start_btn.setMinimumSize(QSize(0, 10))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        self.start_btn.setFont(font2)

        self.verticalLayout.addWidget(self.start_btn)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Widget)
        self.start_btn.clicked.connect(Widget.start_spider)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(
            QCoreApplication.translate("Widget", u"\u4eac\u4e1c\u5546\u54c1\u6570\u636e\u91c7\u96c6", None))
        self.save_path_edit.setPlaceholderText(QCoreApplication.translate("Widget", u"\u683c\u529b.csv", None))
        self.label.setText(QCoreApplication.translate("Widget", u"KeyWord", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"MaxPage", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"SavePath", None))
        self.maxpage_edit.setPlaceholderText(QCoreApplication.translate("Widget", u"4", None))
        self.keyword_edit.setPlaceholderText(QCoreApplication.translate("Widget", u"\u683c\u529b", None))
        self.start_btn.setText(QCoreApplication.translate("Widget", u"Start", None))
    # retranslateUi


class UiTableWidget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(562, 539)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.item_num_label = QLabel(Form)
        self.item_num_label.setObjectName(u"item_num_label")

        self.gridLayout.addWidget(self.item_num_label, 1, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.update_btn = QPushButton(Form)
        self.update_btn.setObjectName(u"update_btn")

        self.gridLayout.addWidget(self.update_btn, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"SpiderMonitor", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u76d1\u89c6\u7a97\u53e3", None))
        self.item_num_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5df2\u83b7\u53d6\u5546\u54c1\u6570\u91cf", None))
        self.update_btn.setText(QCoreApplication.translate("Form", u"Update", None))
    # retranslateUi
