from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,QSize, Qt)
from PySide6.QtGui import (QCursor, QPalette, QBrush, QColor, QSyntaxHighlighter, QTextCharFormat, QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout, QFormLayout,
                               QLabel, QLayout, QPushButton, QComboBox,
                               QSizePolicy, QStackedWidget, QTextEdit, QVBoxLayout, QGroupBox,
                               QWidget, QPlainTextEdit, QLineEdit, QTableWidget, QHeaderView, QListWidget)
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
import re
# from .resources_rc import *

class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 719)
        MainWindow.setMinimumSize(QSize(1400, 560))

        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"QWidget{\n"
                                      "	color: #333;\n"
                                      "	font: 10pt \"Segoe UI\";\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Tooltip */\n"
                                      "QToolTip {\n"
                                      "	color: #333;\n"
                                      "	background-color: #f8f8f2;\n"
                                      "	border: 1px solid #CCC;\n"
                                      "	background-image: none;\n"
                                      "	background-position: left center;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 2px solid rgb(121, 179, 255);\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 8px;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Bg App */\n"
                                      "#bgApp {	\n"
                                      "	background-color: #f5f5fa;\n"
                                      "	border: 1px solid #CCC;\n"
                                      "	color: #44475a;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Left Menu */\n"
                                      "#leftMenuBg {	\n"
                                      "	background-color: #ffffff;\n"
                                      "	border-right: 1px solid #c0c0c0;\n"
                                      "}\n"
                                      "#topLogo {\n"
                                      "	background-color: #ffffff;\n"
                                      "	background-image: ur"
                                      "l(:/resources/images/media/logo.png);\n"
                                      "	background-position: centered;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "}\n"
                                      "#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; color: #2f93e1; }\n"
                                      "#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #2f93e1; }\n"
                                      "\n"
                                      "/* MENUS */\n"
                                      "#topMenu {\n"
                                      "	padding-right: 1px;\n"
                                      "}\n"
                                      "#topMenu .QPushButton {	\n"
                                      "	background-position: left center;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 22px solid transparent;\n"
                                      "	background-color: transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "	color: #083838;\n"
                                      "}\n"
                                      "#topMenu .QPushButton:hover {\n"
                                      "	background-color: #f2f6ff;\n"
                                      "}\n"
                                      "#topMenu .QPushButton:pressed {	\n"
                                      "	background-color: #2f93e1;\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "#bottomMenu .QPushButton {	\n"
                                      "	background-position: left center;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 20px solid transparent;\n"
                                      "	background-color:transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-l"
                                      "eft: 44px;\n"
                                      "	color: #4d4d4d;\n"
                                      "}\n"
                                      "#bottomMenu .QPushButton:hover {\n"
                                      "	background-color: #2f93e1;\n"
                                      "}\n"
                                      "#bottomMenu .QPushButton:pressed {	\n"
                                      "	background-color: #2f93e1;\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "#leftMenuFrame{\n"
                                      "	border-top: 0px solid #ffffff;\n"
                                      "}\n"
                                      "\n"
                                      "/* Toggle Button */\n"
                                      "#toggleButton {\n"
                                      "	background-position: left center;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 15px solid transparent;\n"
                                      "	background-color: #ffffff;\n"
                                      "}\n"
                                      "#toggleButton:hover {\n"
                                      "	background-color: #f2f6ff;\n"
                                      "}\n"
                                      "#toggleButton:pressed {	\n"
                                      "	background-color: #f2f6ff;\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "/* Title Menu */\n"
                                      "#titleRightInfo { padding-left: 10px; }\n"
                                      "\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Extra Tab */\n"
                                      "#extraLeftBox {	\n"
                                      "	background-color: #f2f6ff;\n"
                                      "	border-right: 1px solid rgb(224, 224, 224);\n"
                                      "	color: #2f93e1;\n"
                                      "}\n"
                                      "#extraTopBg{	\n"
                                      "	b"
                                      "ackground-color: #f2f6ff;\n"
                                      "	border-right: 1px solid rgb(224, 224, 224);\n"
                                      "	border-left: 1px solid rgb(224, 224, 224);\n"
                                      "}\n"
                                      "\n"
                                      "/* Icon */\n"
                                      "#extraIcon {\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "	background-image: url(:/resources/images/icons/icon_settings_black.png);\n"
                                      "}\n"
                                      "\n"
                                      "/* Label */\n"
                                      "#extraLabel { color: rgb(88, 88, 88); }\n"
                                      "\n"
                                      "/* Btn Close */\n"
                                      "#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
                                      "#extraCloseColumnBtn:hover { background-color: rgb(161, 196, 249); border-style: solid; border-radius: 4px; }\n"
                                      "#extraCloseColumnBtn:pressed { background-color: rgb(161, 196, 249); border-style: solid; border-radius: 4px; }\n"
                                      "\n"
                                      "/* Extra Content */\n"
                                      "#extraContent{\n"
                                      "	border-top: 3px solid #2f93e1;\n"
                                      "}\n"
                                      "\n"
                                      "/* Extra Top Menus */\n"
                                      "#extraTopMenu .QPushButton {\n"
                                      "	background-position: left center;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 22px solid tran"
                                      "sparent;\n"
                                      "	background-color:transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "	color: #2f93e1;\n"
                                      "}\n"
                                      "#extraTopMenu .QPushButton:hover {\n"
                                      "	background-color: #ffffff;\n"
                                      "}\n"
                                      "#extraTopMenu .QPushButton:pressed {	\n"
                                      "	background-color: rgb(161, 196, 249);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "/* Extra Bottom Menus */\n"
                                      "#extraBottom .QPushButton {\n"
                                      "	background-position: left center;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 22px solid tran"
                                      "sparent;\n"
                                      "	background-color:transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "	color: #2f93e1;\n"
                                      "}\n"
                                      "#extraBottom .QPushButton:hover {\n"
                                      "	background-color: #ffffff;\n"
                                      "}\n"
                                      "#extraBottom .QPushButton:pressed {	\n"
                                      "	background-color: rgb(161, 196, 249);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Content App */\n"
                                      "#contentTopBg{	\n"
                                      "	background-color: #ffffff;\n"
                                      "}\n"
                                      "#contentBottom{\n"
                                      "	border-top: 3px solid #2f93e1;\n"
                                      "}\n"
                                      "#titleRightInfo{\n"
                                      "	color: #0f2c52;\n"
                                      "}\n"
                                      "\n"
                                      "/* Top Buttons */\n"
                                      "#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
                                      "#rightButtons .QPushButton:hover { background-color: #f2f6ff; border-style: solid; border-radius: 4px; }\n"
                                      "#rightButtons .QPushButton:pressed { background-color: #2f93e1; border-style: solid; border-radius: 4px; }\n"
                                      "\n"
                                      "/* Theme Settings */\n"
                                      "#extraRightBox {"
                                      " \n"
                                      "	background-color: #ffffff;\n"
                                      "}\n"
                                      "\n"
                                      "/* Bottom Bar */\n"
                                      "#bottomBar { background-color: #beceff }\n"
                                      "#bottomBar QLabel { font-size: 11px; color: #525252; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
                                      "\n"
                                      "/* CONTENT SETTINGS */\n"
                                      "/* MENUS */\n"
                                      "#contentSettings .QPushButton {\n"
                                      "	background-position: left center;\n"
                                      "	background-repeat: no-repeat;\n"
                                      "	border: none;\n"
                                      "	border-left: 22px solid transparent;\n"
                                      "	background-color:transparent;\n"
                                      "	text-align: left;\n"
                                      "	padding-left: 44px;\n"
                                      "	color: #333333;\n"
                                      "}\n"
                                      "#contentSettings .QPushButton:hover {\n"
                                      "	background-color: #2f93e1;\n"
                                      "	color: #f2f6ff;\n"
                                      "}\n"
                                      "#contentSettings .QPushButton:pressed {	\n"
                                      "	background-color: #46afff;\n"
                                      "	color: #f2f6ff;\n"
                                      "}\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "QTableWidget */\n"
                                      "QTableWidget {	\n"
                                      "	background-color: transparent;\n"
                                      "	padding: 10px;\n"
                                      "	border-radius: 5px;\n"
                                      "	gridline-color: #9faeda;\n"
                                      ""
                                      "	outline: none;\n"
                                      "}\n"
                                      "QTableWidget::item{\n"
                                      "	border-color: #9faeda;\n"
                                      "	padding-left: 5px;\n"
                                      "	padding-right: 5px;\n"
                                      "	gridline-color: #9faeda;\n"
                                      "}\n"
                                      "QTableWidget::item:selected{\n"
                                      "	background-color: rgb(189, 147, 249);\n"
                                      "	color: #f8f8f2;\n"
                                      "}\n"
                                      "QHeaderView::section{\n"
                                      "	background-color: #ffffff;\n"
                                      "	max-width: 30px;\n"
                                      "	border: none;\n"
                                      "	border-style: none;\n"
                                      "}\n"
                                      "QTableWidget::horizontalHeader {	\n"
                                      "	background-color: #ffffff;\n"
                                      "}\n"
                                      "QHeaderView::section:horizontal\n"
                                      "{\n"
                                      "	border: 1px solid #ffffff;\n"
                                      "	background-color: #ffffff;\n"
                                      "	padding: 3px;\n"
                                      "	border-top-left-radius: 7px;\n"
                                      "	border-top-right-radius: 7px;\n"
                                      "	color: #000000;\n"
                                      "}\n"
                                      "QHeaderView::section:vertical\n"
                                      "{\n"
                                      "	border: 1px solid #ffffff;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "LineEdit */\n"
                                      "QLineEdit {\n"
                                      "	background-color: #ffffff;\n"
                                      "	border-radius: 2px;\n"
                                      "	border: 1px solid #5f5f5f;\n"
                                      "	padding-left: 10px;\n"
                                      ""
                                      "	padding-bottom: 5px;\n"
                                      "	padding-top: 5px;\n"
                                      "	selection-color: rgb(255, 255, 255);\n"
                                      "	selection-background-color: #2f93e1;\n"
                                      "	color: #868686;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "	border: 1px solid #6a7cb1;\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "	border: 1px solid #2f93e1;;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "PlainTextEdit */\n"
                                      "QPlainTextEdit {\n"
                                      "	background-color: #ffffff;\n"
                                      "	border-radius: 5px;\n"
                                      "	padding: 10px;\n"
                                      "	selection-color: rgb(255, 255, 255);\n"
                                      "	selection-background-color: 2f93e1;\n"
                                      "	color: #000000;\n"
                                      "}\n"
                                      "QPlainTextEdit  QScrollBar:vertical {\n"
                                      "	width: 8px;\n"
                                      "}\n"
                                      "QPlainTextEdit  QScrollBar:horizontal {\n"
                                      "	height: 8px;\n"
                                      "}\n"
                                      "QPlainTextEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QPlainTextEdit:focus {\n"
                                      "	border: 2px solid #2f93e1;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "ScrollBars */\n"
                                      "QScrol"
                                      "lBar:horizontal {\n"
                                      "	border: none;\n"
                                      "	background: #ffffff;\n"
                                      "	height: 8px;\n"
                                      "	margin: 0px 21px 0 21px;\n"
                                      "	border-radius: 0px;\n"
                                      "}\n"
                                      "QScrollBar::handle:horizontal {\n"
                                      "	background: rgb(189, 147, 249);\n"
                                      "	min-width: 25px;\n"
                                      "	border-radius: 4px\n"
                                      "}\n"
                                      "QScrollBar::add-line:horizontal {\n"
                                      "	border: none;\n"
                                      "	background: #ffffff;\n"
                                      "	width: 20px;\n"
                                      "	border-top-right-radius: 4px;\n"
                                      "	border-bottom-right-radius: 4px;\n"
                                      "	subcontrol-position: right;\n"
                                      "	subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:horizontal {\n"
                                      "	border: none;\n"
                                      "	background: #ffffff;\n"
                                      "	width: 20px;\n"
                                      "	border-top-left-radius: 4px;\n"
                                      "	border-bottom-left-radius: 4px;\n"
                                      "	subcontrol-position: left;\n"
                                      "	subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
                                      "{\n"
                                      "	background: none;\n"
                                      "}\n"
                                      "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                      "{\n"
                                      "	background: none;\n"
                                      "}\n"
                                      "QScrollBar:vertical {\n"
                                      "	border: none;\n"
                                      "	background-"
                                      "color: #ffffff;\n"
                                      "	width: 8px;\n"
                                      "	margin: 21px 0 21px 0;\n"
                                      "	border-radius: 0px;\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical {	\n"
                                      "	background: rgb(189, 147, 249);\n"
                                      "	min-height: 25px;\n"
                                      "	border-radius: 4px\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical {\n"
                                      "	border: none;\n"
                                      "	background: #ffffff;\n"
                                      "	height: 20px;\n"
                                      "	border-bottom-left-radius: 4px;\n"
                                      "	border-bottom-right-radius: 4px;\n"
                                      "	subcontrol-position: bottom;\n"
                                      "	subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical {\n"
                                      "	border: none;\n"
                                      "	background: #ffffff;\n"
                                      "	height: 20px;\n"
                                      "	border-top-left-radius: 4px;\n"
                                      "	border-top-right-radius: 4px;\n"
                                      "	subcontrol-position: top;\n"
                                      "	subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "	background: none;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "	background: none;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "CheckBox *"
                                      "/\n"
                                      "QCheckBox::indicator {\n"
                                      "	border: 3px solid #5e5e5e;\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius: 10px;\n"
                                      "	background: #f5f7ff;\n"
                                      "}\n"
                                      "QCheckBox::indicator:hover {\n"
                                      "	border: 3px solid #2f93e1\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "	background: 3px solid #2f93e1;\n"
                                      "	border: 3px solid #2f93e1;\n"
                                      "	background-image: url(:/resources/images/icons/cil-check-alt.png);\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "RadioButton */\n"
                                      "QRadioButton::indicator {\n"
                                      "	border: 3px solid #5e5e5e;\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius: 10px;\n"
                                      "	background: #f5f7ff;\n"
                                      "}\n"
                                      "QRadioButton::indicator:hover {\n"
                                      "	border: 3px solid rgb(119, 136, 187);\n"
                                      "}\n"
                                      "QRadioButton::indicator:checked {\n"
                                      "	background: 2px solid #2d6d9e;\n"
                                      "	border: 3px solid #2f93e1;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "ComboBox */\n"
                                      "QComb"
                                      "oBox{\n"
                                      "	background-color: #ffffff;\n"
                                      "	border-radius: 2px;\n"
                                      "	border: 1px solid #505050;\n"
                                      "	padding: 5px;\n"
                                      "	padding-left: 10px;\n"
                                      "	color: #424242;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "	border: 1px solid #2f93e1;\n"
                                      "}\n"
                                      "QComboBox::drop-down {\n"
                                      "	subcontrol-origin: padding;\n"
                                      "	subcontrol-position: top right;\n"
                                      "	width: 25px; \n"
                                      "	border-top-right-radius: 3px;\n"
                                      "	border-bottom-right-radius: 3px;	\n"
                                      "	background-image: url(:/resources/images/icons/cil-arrow-bottom.png);\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-reperat;\n"
                                      "}\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "	color: #505050; \n"
                                      "	background-color: #ffffff;\n"
                                      "	padding: 10px;\n"
                                      "	selection-background-color: #2f93e1;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Sliders */\n"
                                      "QSlider::groove:horizontal {\n"
                                      "	border-radius: 5px;\n"
                                      "	height: 10px;\n"
                                      "	margin: 0px;\n"
                                      "	background-color: #ffffff;\n"
                                      "}\n"
                                      "QSlider::handle:horizontal {\n"
                                      "	backgro"
                                      "und-color: #2f93e1;  \n"
                                      "	border: none;\n"
                                      "	height: 10px;\n"
                                      "	width: 10px;\n"
                                      "	margin: 0px;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:hover {\n"
                                      "	background-color: rgb(195, 155, 255);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:pressed {\n"
                                      "	background-color: #2f93e1\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::groove:vertical {\n"
                                      "	border-radius: 5px;\n"
                                      "	width: 10px;\n"
                                      "	margin: 0px;\n"
                                      "	background-color: #ffffff;\n"
                                      "}\n"
                                      "QSlider::groove:vertical:hover {\n"
                                      "	background-color: #ffffff;\n"
                                      "}\n"
                                      "QSlider::handle:vertical {\n"
                                      "	background-color: rgb(189, 147, 249);\n"
                                      "	border: none;\n"
                                      "	height: 10px;\n"
                                      "	width: 10px;\n"
                                      "	margin: 0px;\n"
                                      "	border-radius: 5px;\n"
                                      "}\n"
                                      "QSlider::handle:vertical:hover {\n"
                                      "	background-color: rgb(195, 155, 255);\n"
                                      "}\n"
                                      "QSlider::handle:vertical:pressed {\n"
                                      "	background-color: #2f93e1;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "CommandLinkButton */\n"
                                      "#pagesContainer QCommandLinkButton {	\n"
                                      ""
                                      "	color: #2f93e1;\n"
                                      "	border-radius: 5px;\n"
                                      "	padding: 5px;\n"
                                      "	border: 2px solid #2f93e1;\n"
                                      "	color: #2f93e1\n"
                                      "}\n"
                                      "#pagesContainer QCommandLinkButton:hover {	\n"
                                      "	color: #2f93e1;\n"
                                      "	background-color: #ffffff;\n"
                                      "}\n"
                                      "#pagesContainer QCommandLinkButton:pressed {	\n"
                                      "	color: rgb(189, 147, 249);\n"
                                      "	background-color: #586796;\n"
                                      "}\n"
                                      "\n"
                                      "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                      "Button */\n"
                                      "#pagesContainer QPushButton {\n"
                                      "	border: 2px solid #2f93e1;\n"
                                      "	border-radius: 5px;	\n"
                                      "	background-color: #ffffff;\n"
                                      "	color: #000000;\n"
                                      "}\n"
                                      "#pagesContainer QPushButton:hover {\n"
                                      "	background-color: #7082b6;\n"
                                      "	border: 2px solid #7082b6;\n"
                                      "}\n"
                                      "#pagesContainer QPushButton:pressed {	\n"
                                      "	background-color: #2f93e1;\n"
                                      "	border: 2px solid #2f93e1;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "")
        self.setup_font(self.styleSheet)

        self.appMargins = self.create_vertical_layout(self.styleSheet, u"appMargins", spacing=0,
                                                      margins=(10, 10, 10, 10))

        self.bgApp = self.create_frame(self.styleSheet, u"bgApp")
        self.appLayout = self.create_horizontal_layout(self.bgApp, u"appLayout", spacing=0)

        self.leftMenuBg = self.create_frame(self.bgApp, u"leftMenuBg", min_size=(60, 0), max_size=(60, 16777215))
        self.verticalLayout_3 = self.create_vertical_layout(self.leftMenuBg, u"verticalLayout_3", spacing=0)

        self.setup_top_logo_info()
        self.setup_left_menu()
        self.setup_extra_left_box()

        self.appLayout.addWidget(self.leftMenuBg)

        # Close application button
        self.horizontalLayout_2.addWidget(self.closeAppBtn)

        # Right buttons layout
        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)

        # Top content layout
        self.verticalLayout_2.addWidget(self.contentTopBg)

        # Content bottom setup
        self.contentBottom = self.create_content_bottom()
        self.verticalLayout_2.addWidget(self.contentBottom)

        # Stacked widget setup
        self.stackedWidget = QStackedWidget(self.contentBottom)
        self.create_home_page()
        self.create_shot_collection_page()

    def setup_font(self, widget):
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        widget.setFont(font)

    def create_frame(self, parent, name, min_size=(0, 0), max_size=(16777215, 16777215)):
        frame = QFrame(parent)
        frame.setObjectName(name)
        frame.setMinimumSize(QSize(*min_size))
        frame.setMaximumSize(QSize(*max_size))
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Raised)
        return frame

    def create_vertical_layout(self, parent, name, spacing=0, margins=(0, 0, 0, 0)):
        layout = QVBoxLayout(parent)
        layout.setSpacing(spacing)
        layout.setObjectName(name)
        layout.setContentsMargins(*margins)
        return layout

    def create_horizontal_layout(self, parent, name, spacing=0, margins=(0, 0, 0, 0)):
        layout = QHBoxLayout(parent)
        layout.setSpacing(spacing)
        layout.setObjectName(name)
        layout.setContentsMargins(*margins)
        return layout

    def setup_top_logo_info(self):
        self.topLogoInfo = self.create_frame(self.leftMenuBg, u"topLogoInfo", min_size=(0, 50), max_size=(16777215, 50))
        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.topLogo = self.create_frame(self.topLogoInfo, u"topLogo", min_size=(42, 42), max_size=(42, 42))
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))

        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 15, 160, 20))
        self.setup_title_font(self.titleLeftApp)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

    def setup_title_font(self, label):
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(12)
        label.setFont(font)
        label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

    def setup_left_menu(self):
        self.leftMenuFrame = self.create_frame(self.leftMenuBg, u"leftMenuFrame")
        self.verticalMenuLayout = self.create_vertical_layout(self.leftMenuFrame, u"verticalMenuLayout")

        self.topMenu = self.create_frame(self.leftMenuFrame, u"topMenu")
        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.setup_top_menu_buttons()

        self.bottomMenu = self.create_frame(self.leftMenuFrame, u"bottomMenu")
        self.setup_bottom_menu()

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)
        self.verticalLayout_3.addWidget(self.leftMenuFrame)

    def setup_top_menu_buttons(self):
        self.verticalLayout_8 = self.create_vertical_layout(self.topMenu, u"verticalLayout_8")

        self.toggleBox = self.create_frame(self.topMenu, u"toggleBox", max_size=(16777215, 45))
        self.verticalLayout_4 = self.create_vertical_layout(self.toggleBox, u"verticalLayout_4", spacing=0)
        self.verticalLayout_8.addWidget(self.toggleBox)

        self.btn_chartview = self.create_button(self.topMenu, u"btn_chartview",
                                                u"background-image: url(:/resources/images/icons/icon_apps_black.png);")
        self.verticalLayout_8.addWidget(self.btn_chartview)

        self.btn_scriptconf = self.create_button(self.topMenu, u"btn_scriptconf",
                                                 u"background-image: url(:/resources/images/icons/cil-file-black.png);")
        self.verticalLayout_8.addWidget(self.btn_scriptconf)

        self.btn_collectionmanag = self.create_button(self.topMenu, u"btn_collectionmanag",
                                                      u"background-image: url(:/resources/images/icons/cil-file-black.png);")
        self.verticalLayout_8.addWidget(self.btn_collectionmanag)

    def setup_bottom_menu(self):
        self.verticalLayout_9 = self.create_vertical_layout(self.bottomMenu, u"verticalLayout_9")

        self.toggleLeftBox = self.create_button(self.bottomMenu, u"toggleLeftBox",
                                                u"background-image: url(:/resources/images/icons/icon_settings_black.png);")
        self.verticalLayout_9.addWidget(self.toggleLeftBox)

    def create_button(self, parent, name, stylesheet):
        button = QPushButton(parent)
        button.setObjectName(name)
        button.setMinimumSize(QSize(0, 45))
        button.setFont(parent.font())
        button.setCursor(QCursor(Qt.PointingHandCursor))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setStyleSheet(stylesheet)
        return button

    def setup_extra_left_box(self):
        self.extraLeftBox = self.create_frame(self.bgApp, u"extraLeftBox", min_size=(0, 0), max_size=(0, 16777215))
        self.extraColumLayout = self.create_vertical_layout(self.extraLeftBox, u"extraColumLayout")

        self.extraTopBg = self.create_frame(self.extraLeftBox, u"extraTopBg", min_size=(0, 50), max_size=(16777215, 50))
        self.extraTopLayout = self.create_extra_top_layout(self.extraTopBg)
        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = self.create_frame(self.extraLeftBox, u"extraContent")
        self.extraCenter = self.create_frame(self.extraContent, u"extraCenter")

        self.setup_mds_connection_test()

        self.extraColumLayout.addWidget(self.extraContent)

    def create_extra_top_layout(self, parent):
        layout = QGridLayout()
        layout.setObjectName(u"extraTopLayout")
        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(0)
        layout.setContentsMargins(10, -1, 10, -1)

        self.extraIcon = self.create_frame(parent, u"extraIcon", min_size=(20, 0), max_size=(20, 20))
        layout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(parent)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        layout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = self.create_close_button(parent)
        layout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)

        return layout

    def create_close_button(self, parent):
        button = QPushButton(parent)
        button.setObjectName(u"extraCloseColumnBtn")
        button.setMinimumSize(QSize(28, 28))
        button.setMaximumSize(QSize(28, 28))
        button.setCursor(QCursor(Qt.PointingHandCursor))

        icon = QIcon()
        icon.addFile(u":/resources/images/icons/cil-x-black.png", QSize(), QIcon.Normal, QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QSize(20, 20))

        return button

    def setup_mds_connection_test(self):
        self.mdsconntest = QGroupBox()
        self.mdsconntest.setTitle(u"数据库连接测试")
        self.mdsconntest.setFixedSize(QSize(230, 120))

        self.mdsconnLayout = QVBoxLayout(self.mdsconntest)
        self.mdsiplabel = QLabel()
        self.mdsiplabel.setObjectName(u"mdsiplabel")
        self.mdsiplabel.setAlignment(Qt.AlignLeft)
        self.mdsconnLayout.addWidget(self.mdsiplabel)

        self.mdsip = QLineEdit()
        self.mdsip.setObjectName(u"mdsip")
        self.mdsip.setAlignment(Qt.AlignCenter)
        self.mdsconnLayout.addWidget(self.mdsip)

        self.btn_mdsconn = QPushButton(self.extraCenter)
        self.btn_mdsconn.setObjectName(u"btn_mdsconn")
        self.btn_mdsconn.setText(u"连接")
        self.mdsconnLayout.addWidget(self.btn_mdsconn)


        def setup_extra_center_layout(self):
            # Adding mds connection test group
            self.extraCenterLayout.addWidget(self.create_mds_connection_test_group(), 0, Qt.AlignTop)

            # Adding Chart Display Layout group
            self.configgrop = QGroupBox()
            self.configgrop.setObjectName(u"configgrop")
            self.configgrop.setTitle(u"图表显示布局")
            self.configgrop.setFixedSize(QSize(230, 180))
            self.extraCenterLayout.addWidget(self.configgrop, 1, Qt.AlignTop)

            self.verticalLayout_10 = QFormLayout(self.configgrop)
            self.verticalLayout_10.setObjectName(u"verticalLayout_10")

            # Chart Configuration Label and Input
            self.ChartConfLabel = QLabel()
            self.ChartConfLabel.setObjectName(u"ChartConfLabel")
            self.ChartConfLabel.setText(u"图表显示列数：")
            self.ChartConfLabel.setStyleSheet(u"background: transparent;")
            self.ChartConfLabel.setFrameShape(QFrame.NoFrame)
            self.verticalLayout_10.addWidget(self.ChartConfLabel)

            self.ChartConf = QLineEdit()
            self.ChartConf.setObjectName(u"ChartConf")
            self.ChartConf.setStyleSheet(u"background: transparent;")
            self.ChartConf.setText(u"2")
            self.verticalLayout_10.addWidget(self.ChartConf)

            # Chart Configuration Table
            self.ChartConfTable = QTableWidget()
            self.ChartConfTable.setObjectName(u"ChartConfTable")
            self.ChartConfTable.setRowCount(1)
            self.ChartConfTable.verticalHeader().setVisible(False)
            self.ChartConfTable.horizontalHeader().setVisible(True)
            self.ChartConfTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.ChartConfTable.setStyleSheet(u"background: transparent;")
            self.verticalLayout_10.addWidget(self.ChartConfTable)

        def create_extra_bottom(self):
            self.extraBottom = self.create_frame(self.extraContent, u"extraBottom")
            self.extraBottomLayout = QVBoxLayout(self.extraBottom)
            self.extraBottomLayout.setSpacing(0)
            self.extraBottomLayout.setContentsMargins(0, 0, 0, 0)

            # Save Button
            self.btn_confsave = self.create_button(self.extraBottom, u"btn_confsave",
                                                   u"background-image: url(:/resources/images/icons/cil-save-black.png);")
            self.extraBottomLayout.addWidget(self.btn_confsave)
            self.extraColumLayout.addWidget(self.extraContent, 0, Qt.AlignBottom)

        def setup_content_top_bg(self):
            # Top Content Frame
            self.contentTopBg = self.create_frame(self.contentBox, u"contentTopBg", min_size=(0, 50),
                                                  max_size=(16777215, 50))
            self.horizontalLayout = self.create_horizontal_layout(self.contentTopBg, u"horizontalLayout",
                                                                  margins=(0, 0, 10, 0))

            # Left Box with toggle button and title
            self.leftBox = self.create_frame(self.contentTopBg, u"leftBox")
            self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
            self.horizontalLayout_3.setSpacing(0)
            self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

            # Toggle Button
            self.toggleButton = self.create_button(self.leftBox, u"toggleButton",
                                                   u"background-image: url(:/resources/images/icons/icon_menu_black.png);",
                                                   size=(50, 50))
            self.horizontalLayout_3.addWidget(self.toggleButton)

            # Title Label
            self.titleRightInfo = QLabel(self.leftBox)
            self.titleRightInfo.setObjectName(u"titleRightInfo")
            self.titleRightInfo.setFont(self.styleSheet.font())
            self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
            self.titleRightInfo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
            self.horizontalLayout_3.addWidget(self.titleRightInfo)

            self.horizontalLayout.addWidget(self.leftBox)

            # Right Buttons (Settings, Minimize, Maximize/Restore, Close)
            self.rightButtons = self.create_frame(self.contentTopBg, u"rightButtons", min_size=(0, 28))
            self.horizontalLayout_2 = self.create_horizontal_layout(self.rightButtons, u"horizontalLayout_2", spacing=5)

            # Settings Button
            self.settingsTopBtn = self.create_icon_button(self.rightButtons, u"settingsTopBtn",
                                                          u":/resources/images/icons/icon_settings_black.png")
            self.horizontalLayout_2.addWidget(self.settingsTopBtn)

            # Minimize Button
            self.minimizeAppBtn = self.create_icon_button(self.rightButtons, u"minimizeAppBtn",
                                                          u":/resources/images/icons/icon_minimize_black.png")
            self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

            # Maximize/Restore Button
            self.maximizeRestoreAppBtn = self.create_icon_button(self.rightButtons, u"maximizeRestoreAppBtn",
                                                                 u":/resources/images/icons/icon_restore_black.png")
            self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

            # Close Button
            self.closeAppBtn = self.create_icon_button(self.rightButtons, u"closeAppBtn",
                                                       u":/resources/images/icons/icon_close_black.png")
            self.horizontalLayout_2.addWidget(self.closeAppBtn)

            self.horizontalLayout.addWidget(self.rightButtons)

        def create_icon_button(self, parent, name, icon_path, size=(28, 28)):
            button = QPushButton(parent)
            button.setObjectName(name)
            button.setMinimumSize(QSize(*size))
            button.setMaximumSize(QSize(*size))
            button.setCursor(QCursor(Qt.PointingHandCursor))

            icon = QIcon()
            icon.addFile(icon_path, QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon)
            button.setIconSize(QSize(20, 20))
            return button

    def create_content_bottom(self):
        content_bottom = QFrame(self.contentBox)
        content_bottom.setObjectName("contentBottom")
        content_bottom.setFrameShape(QFrame.NoFrame)
        content_bottom.setFrameShadow(QFrame.Raised)

        vertical_layout = QVBoxLayout(content_bottom)
        vertical_layout.setSpacing(0)
        vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.content = self.create_inner_content()
        vertical_layout.addWidget(self.content)

        return content_bottom

    def create_inner_content(self):
        content = QFrame(self.contentBottom)
        content.setObjectName("content")
        content.setFrameShape(QFrame.NoFrame)
        content.setFrameShadow(QFrame.Raised)

        horizontal_layout = QHBoxLayout(content)
        horizontal_layout.setSpacing(0)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)

        self.pagesContainer = self.create_pages_container()
        horizontal_layout.addWidget(self.pagesContainer)

        return content

    def create_pages_container(self):
        pages_container = QFrame(self.content)
        pages_container.setObjectName("pagesContainer")
        pages_container.setFrameShape(QFrame.NoFrame)
        pages_container.setFrameShadow(QFrame.Raised)

        vertical_layout = QVBoxLayout(pages_container)
        vertical_layout.setSpacing(0)
        vertical_layout.setContentsMargins(0, 0, 0, 0)

        return pages_container

    def create_home_page(self):
        self.home = QWidget()
        self.home.setObjectName("home")
        self.home.setStyleSheet("background-color:#FFFFFF; background-position: center; background-repeat: no-repeat;")

        home_layout = QVBoxLayout(self.home)
        chartview_layout = QGridLayout()
        chartview_layout.setSpacing(0)
        chartview_layout.setContentsMargins(0, 0, 0, 0)
        home_layout.addLayout(chartview_layout)

        home_bottom_widget = self.create_home_bottom_widget()
        home_layout.addWidget(home_bottom_widget, alignment=Qt.AlignBottom)

        self.stackedWidget.addWidget(self.home)

    def create_home_bottom_widget(self):
        home_bottom_widget = QWidget()
        home_bottom_widget.setStyleSheet("background-color:#0FFFFF;")
        home_bottom_widget.setFixedSize(1000, 50)

        bottom_layout = QHBoxLayout(home_bottom_widget)
        bottom_layout.setSpacing(0)

        # Add elements to the bottom layout
        self.shot_label = QLabel("炮号:")
        bottom_layout.addWidget(self.shot_label, alignment=Qt.AlignLeft)

        self.shot_text = QLineEdit("120001;120002;120003;")
        self.shot_text.setFixedWidth(350)
        bottom_layout.addWidget(self.shot_text, alignment=Qt.AlignLeft)

        bottom_layout.addWidget(self.create_button("btn_shot", "Shot"), alignment=Qt.AlignLeft)
        bottom_layout.addWidget(self.create_button("btn_collshot", "Collect Shot"), alignment=Qt.AlignLeft)

        bottom_layout.addStretch()
        bottom_layout.addWidget(QLabel("已有布局:"), alignment=Qt.AlignRight)

        self.layout_combobox = QComboBox()
        bottom_layout.addWidget(self.layout_combobox, alignment=Qt.AlignRight)

        bottom_layout.addWidget(self.create_button("btn_readlayoutcollection", "Read Layout"), alignment=Qt.AlignRight)
        bottom_layout.addWidget(self.create_button("btn_layoutcollection", "Layout Collection"),
                                alignment=Qt.AlignRight)

        return home_bottom_widget

    def create_button(self, object_name, text):
        button = QPushButton(text)
        button.setObjectName(object_name)
        button.setFixedSize(80, 35)
        return button

    def create_shot_collection_page(self):
        self.shot_collection_page = QWidget()
        self.shot_collection_page.setObjectName("shotcollection_page")

        vertical_layout = QHBoxLayout(self.shot_collection_page)
        self.shot_collection_layout = QVBoxLayout()
        layout_collection_layout = QVBoxLayout()

        vertical_layout.addLayout(self.shot_collection_layout)
        vertical_layout.addWidget(self.create_separator())
        vertical_layout.addLayout(layout_collection_layout)

        self.create_shot_collection_widgets()

        self.stackedWidget.addWidget(self.shot_collection_page)

    def create_shot_collection_widgets(self):
        shot_coll_view_layout = QVBoxLayout()

        self.search_entry = QLineEdit()
        self.search_entry.setPlaceholderText("请输入搜索文本")
        shot_coll_view_layout.addWidget(self.search_entry)

        self.shot_collection_list_widget = QListWidget()
        shot_coll_view_layout.addWidget(self.shot_collection_list_widget)

        shot_coll_view_layout.addStretch()
        self.shot_collection_layout.addLayout(shot_coll_view_layout)

        # Bottom buttons for shot collection
        self.shot_collection_bottom_layout = QHBoxLayout()
        self.shot_collection_bottom_layout.addStretch()
        self.shot_collection_bottom_layout.addWidget(self.create_button("btn_readshotcoll", "提取炮号"),
                                                     alignment=Qt.AlignRight)
        self.shot_collection_bottom_layout.addWidget(self.create_button("btn_deleteshotcoll", "删除炮号"),
                                                     alignment=Qt.AlignRight)

        self.shot_collection_layout.addLayout(self.shot_collection_bottom_layout, Qt.AlignBottom)

        # Layout collection
        layout_coll_view_layout = QVBoxLayout()
        layout_collection_layout.addLayout(layout_coll_view_layout)
        layout_collection_layout.addStretch()

        self.layout_collection_bottom_layout = QHBoxLayout()
        self.layout_collection_bottom_layout.addStretch()
        self.layout_collection_bottom_layout.addWidget(self.create_button("btn_readlayoutcoll", "提取布局"),
                                                       alignment=Qt.AlignRight)
        self.layout_collection_bottom_layout.addWidget(self.create_button("btn_deletelayoutcoll", "删除布局"),
                                                       alignment=Qt.AlignRight)

        layout_collection_layout.addLayout(self.layout_collection_bottom_layout, Qt.AlignBottom)

    def create_separator(self):
        separator = QFrame()
        separator.setFrameShape(QFrame.VLine)
        separator.setFrameShadow(QFrame.Plain)
        separator.setLineWidth(3)
        return separator

    def createScriptConfigPage(self):
        script_page = QWidget()
        script_layout = QVBoxLayout(script_page)

        script_label = QLabel("脚本信息")
        script_label.setFixedHeight(30)
        script_layout.addWidget(script_label, Qt.AlignmentFlag.AlignTop)

        script_text = QPlainTextEdit()
        script_text.setTabStopDistance(18)
        script_layout.addWidget(script_text)

        highlighter = PythonHighlighter(script_text.document())

        chart = QChart()
        chart.setTitle("Line chart")
        chart.legend().setAlignment(Qt.AlignBottom)
        series = QLineSeries(chart)
        series.setName("Series")
        chart.createDefaultAxes()
        chart.legend().setInteractive(True)

        chart_view = QChartView(chart)
        chart_view.setStyleSheet("QChartView { padding: 0px; }")

        subscript_layout = QHBoxLayout()
        subscript_layout.addWidget(script_text)
        # subscript_layout.addWidget(chart_view)
        script_layout.addLayout(subscript_layout, Qt.AlignmentFlag.AlignTop)

        btn_run = QPushButton("Run Script")
        btn_run.setObjectName("btn_scriptrun")
        script_layout.addWidget(btn_run, Qt.AlignmentFlag.AlignBottom)

        return script_page

    def createShotCollectionPage(self):
        shot_collection_page = QWidget()
        # Configure shot collection page layout here
        return shot_collection_page

    def createPagesContainer(self):
        container = QFrame(self)
        container.setFrameShape(QFrame.NoFrame)
        container.setFrameShadow(QFrame.Raised)
        layout = QVBoxLayout(container)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # Add content to the container if needed
        return container

    def createExtraRightBox(self):
        extra_box = QFrame()
        extra_box.setObjectName("extraRightBox")
        extra_box.setFrameShape(QFrame.NoFrame)
        extra_box.setFrameShadow(QFrame.Raised)

        vertical_layout = QVBoxLayout(extra_box)
        vertical_layout.setSpacing(0)
        vertical_layout.setContentsMargins(0, 0, 0, 0)

        content_settings = self.createContentSettings()
        vertical_layout.addWidget(content_settings)

        return extra_box

    def createContentSettings(self):
        content_settings = QFrame()
        content_settings.setObjectName("contentSettings")
        content_settings.setFrameShape(QFrame.NoFrame)
        content_settings.setFrameShadow(QFrame.Raised)

        vertical_layout = QVBoxLayout(content_settings)
        vertical_layout.setSpacing(0)
        vertical_layout.setContentsMargins(0, 0, 0, 0)

        top_menus = self.createTopMenus()
        vertical_layout.addWidget(top_menus, 0, Qt.AlignTop)

        return content_settings

    def createTopMenus(self):
        top_menus = QFrame()
        top_menus.setObjectName("topMenus")
        top_menus.setFrameShape(QFrame.NoFrame)
        top_menus.setFrameShadow(QFrame.Raised)

        layout = QVBoxLayout(top_menus)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        btn_logout = QPushButton("Logout")
        btn_logout.setObjectName("btn_logout")
        btn_logout.setMinimumSize(QSize(0, 45))
        layout.addWidget(btn_logout)

        return top_menus

    def createBottomBar(self):
        bottom_bar = QFrame(self)
        bottom_bar.setObjectName("bottomBar")
        bottom_bar.setMinimumSize(QSize(0, 22))
        bottom_bar.setMaximumSize(QSize(16777215, 22))
        bottom_bar.setFrameShape(QFrame.NoFrame)
        bottom_bar.setFrameShadow(QFrame.Raised)

        horizontal_layout = QHBoxLayout(bottom_bar)
        horizontal_layout.setSpacing(0)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)

        credits_label = QLabel("Credits")
        credits_label.setObjectName("creditsLabel")
        credits_label.setMaximumSize(QSize(16777215, 16))
        credits_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        horizontal_layout.addWidget(credits_label)

        version_label = QLabel("Version")
        version_label.setObjectName("version")
        version_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        horizontal_layout.addWidget(version_label)

        frame_size_grip = QFrame()
        frame_size_grip.setObjectName("frame_size_grip")
        frame_size_grip.setMinimumSize(QSize(20, 0))
        horizontal_layout.addWidget(frame_size_grip)

        return bottom_bar