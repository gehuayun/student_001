from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import sys
import os
from comtypes import client


# 文件转换脚本
class FileDropWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        # 设置窗口标题
        self.setWindowTitle("word/pdf")
        # 隐藏标题栏和控制按钮
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置窗口置于顶层
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # 获取屏幕的可用几何区域
        screen_geometry = QApplication.desktop().availableGeometry()
        # 设置窗口大小
        window_width = 400
        window_height = 300
        self.resize(window_width, window_height)
        # 将窗口移动到屏幕中心
        x = (screen_geometry.width() - window_width) // 2
        y = (screen_geometry.height() - window_height) // 2
        self.move(x, y)
        # 拖拉区域代码
        label = QLabel("拖放Word文件到此区域")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            QLabel {
                background-color: #EAF2F8;
                font-family: Arial;
                font-size: 35px;
                font-weight: 40px;
                color: #333333;
                padding: 10px;
                border: 4px dashed #CCCCCC;
                border-radius: 30px;
            }
        """)

        label.setAcceptDrops(True)
        label.installEventFilter(self)

        layout.addWidget(label)
        self.setLayout(layout)

    def eventFilter(self, obj, event):
        if event.type() == event.DragEnter:
            if event.mimeData().hasUrls():
                event.acceptProposedAction()
        elif event.type() == event.Drop:
            if event.mimeData().hasUrls():
                files = [url.toLocalFile() for url in event.mimeData().urls()]
                self.handleDroppedFiles(files)
            event.acceptProposedAction()
        return super().eventFilter(obj, event)

    def handleDroppedFiles(self, files):
        for file in files:
            if file.endswith('.docx') or file.endswith('.doc'):
                self.convertToPDF(file)
            else:
                self.showErrorMessage("请拖放Word文件或类似文件！")

    def convertToPDF(self, docx_file):
        word = client.CreateObject("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(docx_file)
        pdf_file = os.path.splitext(docx_file)[0] + ".pdf"
        doc.SaveAs(pdf_file, FileFormat=17)
        doc.Close()

        # 关闭 Word 窗口
        word.Quit()

        # 显示转换成功的消息框
        reply = QMessageBox.question(self, "转换成功", f"已将Word文件转换为PDF文件：\n{pdf_file}\n\n是否继续拖放Word文件",
                                     QMessageBox.Yes | QMessageBox.No)

        # 根据用户的选择执行相应的操作
        if reply == QMessageBox.Yes:
            # 用户选择继续执行代码
            print("继续执行代码...")
        elif reply == QMessageBox.No:
            # 用户选择关闭 Word/PDF 窗口
            os.startfile(pdf_file)  # 打开 PDF 文件


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = FileDropWidget()
    widget.resize(300, 200)
    widget.show()
    sys.exit(app.exec_())
