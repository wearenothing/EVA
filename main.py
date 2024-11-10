import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow


# 创建 QApplication 实例并传入命令行参数
app = QApplication(sys.argv)

# 主窗口
main_window = MainWindow()
main_window.show()

# 执行应用程序
sys.exit(app.exec())
