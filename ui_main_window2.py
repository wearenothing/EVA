from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor, QPalette, QBrush, QColor, QSyntaxHighlighter, QTextCharFormat, QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout, QFormLayout,
                               QLabel, QLayout, QPushButton, QComboBox,
                               QSizePolicy, QStackedWidget, QTextEdit, QVBoxLayout, QGroupBox,
                               QWidget, QPlainTextEdit, QLineEdit, QTableWidget, QHeaderView, QListWidget)
import re
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
# from .resources_rc import *

class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.highlighting_rules = []

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("blue"))
        keyword_format.setFontWeight(QFont.Bold)
        keywords = ["and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "exec", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "not", "or", "pass", "print", "raise", "return", "try", "while", "with", "yield"]
        for keyword in keywords:
            self.highlighting_rules.append((re.compile(f"\\b{keyword}\\b"), keyword_format))

        string_format = QTextCharFormat()
        string_format.setForeground(QColor("red"))
        self.highlighting_rules.append((re.compile(r"\"[^\"]*\"|\'[^\']*\'"), string_format))

        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("green"))
        self.highlighting_rules.append((re.compile(r"#[^\n]*"), comment_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            match = pattern.search(text)
            while match:
                start = match.start()
                length = match.end() - start
                self.setFormat(start, length, format)
                match = pattern.search(text, start + length)

class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 719)
        MainWindow.setMinimumSize(QSize(1400, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
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
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 15, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.topMenu)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Plain)
        self.toggleBox.setLineWidth(-1)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_4.setContentsMargins(0, 2, 0, 0)

        self.verticalLayout_8.addWidget(self.toggleBox)

        self.btn_chartview = QPushButton(self.topMenu)
        self.btn_chartview.setObjectName(u"btn_chartview")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_chartview.sizePolicy().hasHeightForWidth())
        self.btn_chartview.setSizePolicy(sizePolicy)
        self.btn_chartview.setMinimumSize(QSize(0, 45))
        self.btn_chartview.setFont(font)
        self.btn_chartview.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chartview.setLayoutDirection(Qt.LeftToRight)
        self.btn_chartview.setStyleSheet(u"background-image: url(:/resources/images/icons/icon_apps_black.png);")

        self.verticalLayout_8.addWidget(self.btn_chartview)

        # self.btn_collectionmanag = QPushButton(self.topMenu)
        # self.btn_collectionmanag.setObjectName(u"btn_collectionmanag")
        # sizePolicy.setHeightForWidth(self.btn_collectionmanag.sizePolicy().hasHeightForWidth())
        # self.btn_collectionmanag.setSizePolicy(sizePolicy)
        # self.btn_collectionmanag.setMinimumSize(QSize(0, 45))
        # self.btn_collectionmanag.setFont(font)
        # self.btn_collectionmanag.setCursor(QCursor(Qt.PointingHandCursor))
        # self.btn_collectionmanag.setLayoutDirection(Qt.LeftToRight)
        # self.btn_collectionmanag.setStyleSheet(u"background-image: url(:/resources/images/icons/cil-file-black.png);")
        #
        # self.verticalLayout_8.addWidget(self.btn_collectionmanag)

        self.btn_scriptconf = QPushButton(self.topMenu)
        self.btn_scriptconf.setObjectName(u"btn_scriptconf")
        sizePolicy.setHeightForWidth(self.btn_scriptconf.sizePolicy().hasHeightForWidth())
        self.btn_scriptconf.setSizePolicy(sizePolicy)
        self.btn_scriptconf.setMinimumSize(QSize(0, 45))
        self.btn_scriptconf.setFont(font)
        self.btn_scriptconf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_scriptconf.setLayoutDirection(Qt.LeftToRight)
        self.btn_scriptconf.setStyleSheet(u"background-image: url(:/resources/images/icons/cil-file-black.png);")

        self.verticalLayout_8.addWidget(self.btn_scriptconf)

        self.btn_collectionmanag = QPushButton(self.topMenu)
        self.btn_collectionmanag.setObjectName(u"btn_collectionmanag")
        sizePolicy.setHeightForWidth(self.btn_collectionmanag.sizePolicy().hasHeightForWidth())
        self.btn_collectionmanag.setSizePolicy(sizePolicy)
        self.btn_collectionmanag.setMinimumSize(QSize(0, 45))
        self.btn_collectionmanag.setFont(font)
        self.btn_collectionmanag.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_collectionmanag.setLayoutDirection(Qt.LeftToRight)
        self.btn_collectionmanag.setStyleSheet(u"background-image: url(:/resources/images/icons/cil-file-black.png);")

        self.verticalLayout_8.addWidget(self.btn_collectionmanag)

        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/resources/images/icons/icon_settings_black.png);")
        self.verticalLayout_9.addWidget(self.toggleLeftBox)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)

        self.verticalLayout_3.addWidget(self.leftMenuFrame)

        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/resources/images/icons/cil-x-black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)

        self.verticalLayout_5.addLayout(self.extraTopLayout)

        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)


        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.extraTopMenu.setStyleSheet("background-color: lightblue;")
        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        # self.btn_confsave = QPushButton(self.extraTopMenu)
        # self.btn_confsave.setObjectName(u"btn_confsave")
        # sizePolicy.setHeightForWidth(self.btn_confsave.sizePolicy().hasHeightForWidth())
        # self.btn_confsave.setSizePolicy(sizePolicy)
        # self.btn_confsave.setMinimumSize(QSize(0, 45))
        # self.btn_confsave.setFont(font)
        # self.btn_confsave.setCursor(QCursor(Qt.PointingHandCursor))
        # self.btn_confsave.setLayoutDirection(Qt.LeftToRight)
        # self.btn_confsave.setStyleSheet(u"background-image: url(:/resources/images/icons/cil-save-black.png);")
        # self.verticalLayout_11.addWidget(self.btn_confsave)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12.addWidget(self.extraCenter, Qt.AlignTop)
        self.extraCenterLayout = QVBoxLayout(self.extraCenter)
        self.extraCenterLayout.setSpacing(0)
        self.extraCenterLayout.setObjectName(u"extraCenterLayout")
        self.extraCenterLayout.setContentsMargins(0, 0, 0, 0)

        self.mdsconntest = QGroupBox()
        self.mdsconntest.setTitle(u"数据库连接测试")
        self.mdsconntest.setFixedSize(QSize(230, 120))
        #self.verticalLayout_12.addWidget(self.mdsconntest)
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
        self.mdsconnLayout.addWidget(self.btn_mdsconn)

        self.extraCenterLayout.addWidget(self.mdsconntest, 0, Qt.AlignTop)
        self.configgrop = QGroupBox()
        self.configgrop.setTitle(u"图表显示布局")
        self.configgrop.setFixedSize(QSize(230, 180))
        self.extraCenterLayout.addWidget(self.configgrop, 1, Qt.AlignTop)
        self.verticalLayout_10 = QFormLayout(self.configgrop)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.ChartConfLabel = QLabel(self.extraCenter)
        self.ChartConfLabel.setObjectName(u"ChartConfLabel")
        self.ChartConfLabel.setText(u"图表显示列数：")
        self.ChartConfLabel.setStyleSheet(u"background: transparent;")
        self.ChartConfLabel.setFrameShape(QFrame.NoFrame)

        self.ChartConf = QLineEdit(self.extraCenter)
        self.ChartConf.setObjectName(u"ChartConf")
        self.ChartConf.setStyleSheet(u"background: transparent;")
        self.ChartConf.setText(u"2")
        self.verticalLayout_10.addWidget(self.ChartConfLabel)
        self.verticalLayout_10.addWidget(self.ChartConf)

        self.ChartConfTable = QTableWidget(self.extraCenter)
        self.ChartConfTable.setRowCount(1)
        self.ChartConfTable.verticalHeader().setVisible(False)
        self.ChartConfTable.horizontalHeader().setVisible(True)
        self.ChartConfTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        # self.ChartConfTable.setHorizontalHeaderLabels([f'第{i}列' for i in range(5)])
        self.ChartConfTable.setObjectName(u"ChartConfTable")
        self.ChartConfTable.setStyleSheet(u"background: transparent;")

        self.verticalLayout_10.addWidget(self.ChartConfTable)

        # self.textEdit = QTextEdit(self.extraCenter)
        # self.textEdit.setObjectName(u"textEdit")
        # self.textEdit.setMinimumSize(QSize(222, 0))
        # self.textEdit.setStyleSheet(u"background: transparent;")
        # self.textEdit.setFrameShape(QFrame.NoFrame)
        # self.textEdit.setReadOnly(True)
        #
        # self.verticalLayout_10.addWidget(self.textEdit)


        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12.addWidget(self.extraBottom, 0, Qt.AlignBottom)
        self.extraBottomLayout = QVBoxLayout(self.extraBottom)
        self.extraBottomLayout.setSpacing(0)
        self.extraBottomLayout.setObjectName(u"extraBottomLayout")
        self.extraBottomLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_confsave = QPushButton(self.extraBottom)
        self.btn_confsave.setObjectName(u"btn_confsave")
        sizePolicy.setHeightForWidth(self.btn_confsave.sizePolicy().hasHeightForWidth())
        self.btn_confsave.setSizePolicy(sizePolicy)
        self.btn_confsave.setMinimumSize(QSize(0, 45))
        self.btn_confsave.setFont(font)
        self.btn_confsave.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confsave.setLayoutDirection(Qt.LeftToRight)
        self.btn_confsave.setStyleSheet(u"background-image: url(:/resources/images/icons/cil-save-black.png);")
        self.extraBottomLayout.addWidget(self.btn_confsave)

        self.extraColumLayout.addWidget(self.extraContent)

        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Plain)
        self.contentTopBg.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Plain)
        self.leftBox.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.leftBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(50, 50))
        self.toggleButton.setMaximumSize(QSize(45, 16777215))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/resources/images/icons/icon_menu_black.png);")

        self.horizontalLayout_3.addWidget(self.toggleButton)

        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/resources/images/icons/icon_settings_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/resources/images/icons/icon_minimize_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/resources/images/icons/icon_restore_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/resources/images/icons/icon_close_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon4)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)

        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")

        self.home.setStyleSheet(u"background-color:#FFFFFF;\n"
                                "background-position: center;\n"
                                "background-repeat: no-repeat;")
        self.home_layout_m = QVBoxLayout(self.home)
        self.chartviewHLayout = QGridLayout()
        self.chartviewHLayout.setSpacing(0)
        self.chartviewHLayout.setContentsMargins(0, 0, 0, 0)
        self.home_layout_m.addLayout(self.chartviewHLayout)
        #self.home_layout_m.addStretch(0)
        self.home_bottom_widget = QWidget()
        self.home_bottom_widget.setStyleSheet("background-color:#0FFFFF;")
        self.home_bottom_widget.setFixedSize(1000, 50)
        self.home_bottom_laytou = QHBoxLayout()
        self.home_bottom_laytou.setSpacing(0)

        self.home_bottom_widget.setLayout(self.home_bottom_laytou)
        # self.treenamelable = QLabel(u'树名:')
        # self.home_bottom_laytou.addWidget(self.treenamelable, alignment=Qt.AlignLeft)
        # self.treename = QComboBox()
        # self.home_bottom_laytou.addWidget(self.treename, alignment=Qt.AlignLeft)
        self.shotlable = QLabel(u"炮号:")
        self.home_bottom_laytou.addWidget(self.shotlable, alignment=Qt.AlignLeft)
        self.shottext = QLineEdit()
        self.shottext.setFixedWidth(350)
        self.shottext.setText(u"120001;120002;120003;")
        self.home_bottom_laytou.addWidget(self.shottext,  alignment=Qt.AlignLeft)
        self.shotrangelable = QLabel(u"炮号范围")
        #self.home_bottom_laytou.addWidget(self.shotrangelable,  alignment=Qt.AlignLeft)

        self.btn_shot = QPushButton()
        self.btn_shot.setObjectName(u"btn_shot")
        self.btn_shot.setFixedSize(80,35)
        self.home_bottom_laytou.addWidget(self.btn_shot,  alignment=Qt.AlignLeft)
        self.btn_collshot = QPushButton()
        self.btn_collshot.setObjectName(u"btn_collshot")
        self.btn_collshot.setFixedSize(80, 35)
        self.home_bottom_laytou.addWidget(self.btn_collshot, alignment=Qt.AlignLeft)
        self.home_bottom_laytou.addStretch()
        self.layoutlable = QLabel(u"已有布局:")
        self.home_bottom_laytou.addWidget(self.layoutlable, alignment=Qt.AlignRight)
        self.layoutcombobox = QComboBox()
        self.home_bottom_laytou.addWidget(self.layoutcombobox,  alignment=Qt.AlignRight)
        self.btn_readlayoutcollection = QPushButton()
        self.btn_readlayoutcollection.setFixedSize(80, 35)
        self.btn_readlayoutcollection.setObjectName(u"btn_readlayoutcollection")
        self.home_bottom_laytou.addWidget(self.btn_readlayoutcollection, alignment=Qt.AlignRight)
        self.btn_layoutcollection = QPushButton()
        self.btn_layoutcollection.setFixedSize(80, 35)
        self.btn_layoutcollection.setObjectName(u"btn_layoutcollection")
        self.home_bottom_laytou.addWidget(self.btn_layoutcollection, alignment=Qt.AlignRight)
        self.home_layout_m.addWidget(self.home_bottom_widget, alignment=Qt.AlignBottom)
        self.stackedWidget.addWidget(self.home)

        self.shotcollection_page = QWidget()
        self.shotcollection_page.setObjectName(u"shotcollection_page")
        self.verticalLayout_20 = QHBoxLayout(self.shotcollection_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.shotcollection_layout = QVBoxLayout()
        self.layoutcollection_layout = QVBoxLayout()
        self.verticalLayout_20.addLayout(self.shotcollection_layout)
        separator = QFrame()
        separator.setFrameShape(QFrame.VLine)
        separator.setFrameShadow(QFrame.Plain)
        separator.setLineWidth(3)
        self.verticalLayout_20.addWidget(separator)
        self.verticalLayout_20.addLayout(self.layoutcollection_layout)

        self.shotcollview_layout = QVBoxLayout()
        self.search_entry = QLineEdit()
        self.search_entry.setPlaceholderText("请输入搜索文本")
        self.shotcollectionlist_widget = QListWidget()
        self.shotcollectionlist_widget.adjustSize()
        self.shotcollview_layout.addWidget(self.search_entry)
        self.shotcollview_layout.addWidget(self.shotcollectionlist_widget)
        self.shotcollview_layout.addStretch()
        self.shotcollection_layout.addLayout(self.shotcollview_layout)
        self.shotcollection_layout.addStretch()
        self.shotcollectionBottom_layout = QHBoxLayout()
        self.btn_readshotcoll = QPushButton(u"提取炮号")
        self.btn_readshotcoll.setFixedSize(80, 35)
        self.btn_readshotcoll.setObjectName(u"btn_readshotcoll")
        self.btn_deleteshotcoll = QPushButton(u"删除炮号")
        self.btn_deleteshotcoll.setFixedSize(80, 35)
        self.btn_deleteshotcoll.setObjectName(u"btn_deleteshotcoll")
        self.shotcollectionBottom_layout.addStretch()
        self.shotcollectionBottom_layout.addWidget(self.btn_readshotcoll,  alignment=Qt.AlignRight)
        self.shotcollectionBottom_layout.addWidget(self.btn_deleteshotcoll, alignment=Qt.AlignRight)
        self.shotcollection_layout.addLayout(self.shotcollectionBottom_layout,Qt.AlignBottom)

        self.layoutcollview_layout = QVBoxLayout()
        self.layoutcollection_layout.addLayout(self.layoutcollview_layout)
        self.layoutcollection_layout.addStretch()
        self.layoutcollectionBottom_layout = QHBoxLayout()
        self.btn_readlayoutcoll = QPushButton(u"提取布局")
        self.btn_readlayoutcoll.setFixedSize(80, 35)
        self.btn_readlayoutcoll.setObjectName(u"btn_readlayoutcoll")
        self.btn_deletelayoutcoll = QPushButton(u"删除布局")
        self.btn_deletelayoutcoll.setFixedSize(80, 35)
        self.btn_deletelayoutcoll.setObjectName(u"btn_deletelayoutcoll")
        self.layoutcollectionBottom_layout.addStretch()
        self.layoutcollectionBottom_layout.addWidget(self.btn_readlayoutcoll, alignment=Qt.AlignRight)
        self.layoutcollectionBottom_layout.addWidget(self.btn_deletelayoutcoll, alignment=Qt.AlignRight)
        self.layoutcollection_layout.addLayout(self.layoutcollectionBottom_layout, Qt.AlignBottom)

        self.scriptconf_page = QWidget()
        self.scriptlayout = QVBoxLayout()
        self.scriptconf_page.setLayout(self.scriptlayout)
        self.scriptlable = QLabel(u"脚本信息")
        self.scriptlable.setFixedHeight(30)
        self.scriptlayout.addWidget(self.scriptlable, Qt.AlignmentFlag.AlignTop)
        self.scripttext = QPlainTextEdit()
        self.scripttext.setTabStopDistance(18)
        self.scripttext.setGeometry(10, 10, 100, 50)
        self.hightlighter = PythonHighlighter(self.scripttext.document())
        self.chart = QChart()
        self.chart.setTitle("Line chart")
        self.chart.legend().setAlignment(Qt.AlignBottom)
        series = QLineSeries(self.chart)
        series.setName("Series")
        self.chart.createDefaultAxes()
        self.chart.legend().setInteractive(True)
        self.chart.legend().clickedItem = None
        self.chart_view = QChartView(self.chart)
        self.chart_view.setStyleSheet("QChartView { padding: 0px; }")
        subscriptlayout = QHBoxLayout()
        subscriptlayout.addWidget(self.scripttext)
        #subscriptlayout.addWidget(self.chart_view)
        self.scriptlayout.addLayout(subscriptlayout, Qt.AlignmentFlag.AlignTop)
        self.btn_scriptrun = QPushButton()
        self.btn_scriptrun.setObjectName(u"btn_scriptrun")
        self.scriptlayout.addWidget(self.btn_scriptrun, Qt.AlignmentFlag.AlignBottom)

        self.stackedWidget.addWidget(self.shotcollection_page)
        self.stackedWidget.addWidget(self.scriptconf_page)
        self.verticalLayout_15.addWidget(self.stackedWidget)

        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/resources/images/icons/icon_close_black.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)

        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.contentSettings)

        self.horizontalLayout_4.addWidget(self.extraRightBox)

        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)

        self.verticalLayout_6.addWidget(self.bottomBar)

        self.verticalLayout_2.addWidget(self.contentBottom)

        self.appLayout.addWidget(self.contentBox)

        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.translate_ui(MainWindow)

        self.stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)



    def translate_ui(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Genius Software", None))
        # self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Invoice App", None))
        self.btn_chartview.setText(QCoreApplication.translate("MainWindow", u"图表显示", None))
        self.btn_collectionmanag.setText(QCoreApplication.translate("MainWindow", u"收藏管理", None))
        self.btn_scriptconf.setText(QCoreApplication.translate("MainWindow", u"脚本配置", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"系统配置", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        # if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
        # endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_confsave.setText(QCoreApplication.translate("MainWindow", u"配置保存", None))
        #         self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        # "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        # "p, li { white-space: pre-wrap; }\n"
        # "</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        # "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">GUI With PySide</span></p>\n"
        # "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#454544;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
        # "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0p"
        #                         "x;\"><span style=\" color:#454544;\">MIT License</span></p>\n"
        # "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#454544;\">Developed by </span><a href=\"https://raherygino.github.io\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">Gino</span></a><span style=\" font-weight:600; color:#454544;\"> </span></p>\n"
        # "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">Convert UI</span></p>\n"
        # "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#483d37;\">pyside6-uic main.ui -o ui_main.py</span></p>\n"
        # "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -q"
        #                         "t-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">Convert QRC</span></p>\n"
        # "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#483d37;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.toggleButton.setText("")
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Modern GUI by Gino with PySide 6", None))
        # if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
        # endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        # endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        # endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.mdsiplabel.setText(QCoreApplication.translate("MainWindow", u"数据库IP", None))
        self.btn_mdsconn.setText(QCoreApplication.translate("MainWindow", u"连接数据库", None))
        self.btn_shot.setText(QCoreApplication.translate("MainWindow", u"读取炮号", None))
        self.btn_collshot.setText(QCoreApplication.translate("MainWindow", u"收藏炮号", None))
        self.btn_layoutcollection.setText(QCoreApplication.translate("MainWindow", u"保存布局", None))
        self.btn_readlayoutcollection.setText(QCoreApplication.translate("MainWindow", u"使用布局", None))
        self.btn_scriptrun.setText(QCoreApplication.translate("MainWindow", u"运行脚本", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Created & Developed", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))

