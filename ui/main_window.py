import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QApplication,QFrame,\
    QHBoxLayout,QLabel,QGridLayout,QStackedWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from logic.file_operations import open_file, save_file

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # first level
        self.styleSheet = QWidget(self)

        # second level
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.bgApp = QFrame(self.styleSheet)

        # 3rd level
        self.appLayout = QHBoxLayout(self.bgApp)
        self.leftMenuBg = QFrame(self.bgApp)
        self.extraLeftBox = QFrame(self.bgApp)
        self.contentBox = QFrame(self.bgApp)

        # 4th level
        # leftMenuBg
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        # extraLeftBox
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraContent = QFrame(self.extraLeftBox)
        # contentBox
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentBottom = QFrame(self.contentBox)

        # 5th level
        # topLogoInfo
        self.topLogo = QFrame(self.topLogoInfo)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        # leftMenuFrame
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu = QFrame(self.leftMenuFrame)
        # extraTopBg
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.extraTopLayout = QGridLayout() # 哪里来的单独布局？？
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraLabel = QLabel(self.extraTopBg)
        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        # extraContent
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraCenter = QFrame(self.extraContent)
        self.extraBottom = QFrame(self.extraContent)

        # contentTopBg
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.leftBox = QFrame(self.contentTopBg)
        self.rightButtons = QFrame(self.contentTopBg)
        # contentBottom
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.content = QFrame(self.contentBottom)
        self.bottomBar = QFrame(self.contentBottom)

        # extraTopMenu
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        # extraCenter
        self.extraCenterLayout = QVBoxLayout(self.extraCenter)
        # extraBottom
        self.extraBottomLayout = QVBoxLayout(self.extraBottom)

        # leftBox
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.toggleButton = QPushButton(self.leftBox)
        self.titleRightInfo = QLabel(self.leftBox)
        # rightButtons
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn = QPushButton(self.rightButtons)

        # content
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.pagesContainer = QFrame(self.content)
        self.extraRightBox = QFrame(self.content)

        # bottomBar
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.creditsLabel = QLabel(self.bottomBar)
        self.version = QLabel(self.bottomBar)
        self.frame_size_grip = QFrame(self.bottomBar)

        # pagesContainer
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.stackedWidget = QStackedWidget(self.pagesContainer)



        # extraRightBox
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.contentSettings = QFrame(self.extraRightBox)

        # contentSettings
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.topMenus = QFrame(self.contentSettings)
        # topMenus
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.btn_logout = QPushButton(self.topMenus)


        self.verticalLayout_14.addWidget(self.btn_logout)
        # verticalLayout_13
        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)

        # verticalLayout_7
        self.verticalLayout_7.addWidget(self.contentSettings)
        # stackedWidget
        self.stackedWidget.addWidget(self.home)
        self.stackedWidget.addWidget(self.shotcollection_page)
        self.stackedWidget.addWidget(self.scriptconf_page)
        # verticalLayout_15
        self.verticalLayout_15.addWidget(self.stackedWidget)

        # horizontalLayout_5
        self.horizontalLayout_5.addWidget(self.creditsLabel)
        self.horizontalLayout_5.addWidget(self.version)
        self.horizontalLayout_5.addWidget(self.frame_size_grip)

        # horizontalLayout_4
        self.horizontalLayout_4.addWidget(self.pagesContainer)
        self.horizontalLayout_4.addWidget(self.extraRightBox)

        # horizontalLayout_2
        self.horizontalLayout_2.addWidget(self.settingsTopBtn)
        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)
        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)
        self.horizontalLayout_2.addWidget(self.closeAppBtn)

        self.horizontalLayout_3.addWidget(self.toggleButton)
        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        self.extraBottomLayout.addWidget(self.btn_confsave)
        self.extraCenterLayout.addWidget(self.mdsconntest, 0, Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.content)
        self.verticalLayout_6.addWidget(self.bottomBar)

        # horizontalLayout
        self.horizontalLayout.addWidget(self.leftBox)
        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)

        self.verticalLayout_12.addWidget(self.extraBottom, 0, Qt.AlignBottom)
        self.verticalLayout_12.addWidget(self.extraCenter, Qt.AlignTop)
        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)
        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)
        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.extraTopLayout) # 看不懂只有这一个布局？确定这个布局是做什么用的！

        # 将 self.topMenu 小部件添加到 self.verticalMenuLayout 布局中
        # 第二个参数 `0` 表示将 topMenu 插入到布局的第一个位置
        # 第三个参数 `Qt.AlignTop` 表示将 topMenu 在布局中垂直对齐到顶部
        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)
        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)

        # verticalLayout_2
        self.verticalLayout_2.addWidget(self.contentTopBg)
        self.verticalLayout_2.addWidget(self.contentBottom)

        # 6th level
        self.extraColumLayout.addWidget(self.extraTopBg)
        self.extraColumLayout.addWidget(self.extraContent)

        # verticalLayout_3
        self.verticalLayout_3.addWidget(self.topLogoInfo)
        self.verticalLayout_3.addWidget(self.leftMenuFrame)



        # 3rd level
        self.appLayout.addWidget(self.leftMenuBg)
        self.appLayout.addWidget(self.extraLeftBox)
        self.appLayout.addWidget(self.contentBox)

        # 2rd level
        self.appMargins.addWidget(self.bgApp)

        # 1st level
        self.setCentralWidget(self.styleSheet)

        #
        self.central_widget = QWidget(self)



        # create fonts
        self.background_frame = None
        self.font = None
        self.font1 = None
        self.font2 = None
        self.font3 = None

        self.setup_fonts()


        # we can display hieracy? of the structure here 
        # create central widgets
        self.central_widget = None
        self.setup_central_widget()

        self.save_button = None
        self.open_button = None

        self.containerLayout = None
        self.mainContainer = None
        self.main_layout = None
        self.init_ui()
        self.create_buttons()
        self.connect_signals()

    def setup_fonts(self):
        self.font = QFont()
        self.font.setFamilies([u"Segoe UI"])
        self.font.setPointSize(10)
        self.font.setBold(False)
        self.font.setItalic(False)

    def setup_central_widget(self):
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName(u"centralWidget")
        self.central_widget.setFont(self.font)
        self.setCentralWidget(self.central_widget)

    def setup_main_layout(self):
        # 创建垂直布局并设置边距
        self.main_layout = QVBoxLayout(self.central_widget)  # 父对象是 central_widget
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName("main_layout")
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        # 创建 QFrame 小部件，并设置其样式和外观
        self.background_frame = QFrame(self.central_widget)  # 父对象是 central_widget
        self.background_frame.setObjectName("background_frame")
        self.background_frame.setFrameShape(QFrame.NoFrame)  # 无边框
        self.background_frame.setFrameShadow(QFrame.Raised)  # 设置框架阴影效果

        # 设置背景框架的样式
        self.background_frame.setStyleSheet("background-color: lightgray;")

        # 将 QFrame 添加到布局
        self.main_layout.addWidget(self.background_frame)

    def init_ui(self):
        """初始化界面的整体布局"""
        self.setObjectName(u"mainWindow")
        self.resize(150, 90)
        # self.setMinimumSize(QSize(40, 56))

        self.mainContainer = QWidget(self)
        self.containerLayout = QVBoxLayout(self.mainContainer)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

    def create_buttons(self):
        """创建界面中的按钮控件"""
        self.open_button = QPushButton("Open")
        self.save_button = QPushButton("Save")
        self.main_layout.addWidget(self.open_button)
        self.main_layout.addWidget(self.save_button)

    def connect_signals(self):
        """连接按钮的信号与槽函数"""
        self.open_button.clicked.connect(self.open_file)
        self.save_button.clicked.connect(self.save_file)

    def open_file(self):
        """按钮功能实现：打开文件，通过逻辑模块的函数实现"""
        filepath, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if filepath:
            content = open_file(filepath)
            print(content)  # 示例：打印内容，实际可以更新到界面

    def save_file(self):
        """按钮功能实现：保存文件，通过逻辑模块的函数实现"""
        filepath, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if filepath:
            data = "Example content"  # 示例数据，实际可以来自界面输入
            save_file(filepath, data)
            print("File saved successfully.")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())