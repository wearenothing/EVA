import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QApplication
from PyQt6.QtCore import QSize
from logic.file_operations import open_file, save_file

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.create_buttons()
        self.connect_signals()

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