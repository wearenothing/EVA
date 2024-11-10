import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QApplication,QFrame
from PySide6.QtGui import QFont
from logic.file_operations import open_file, save_file

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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