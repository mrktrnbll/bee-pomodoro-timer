"""main entry point for bee pomodoro app"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
import os

from sprites.movement_handlers import get_random_spawn_position

ASSETS_DIR = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), "assets")
IMAGE_DIR = os.path.join(ASSETS_DIR, "images")
WIDTH_OFFSET = 40


class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
        )
        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen)

        self.populated_positions: list[tuple(int)] = []

        # add to window based functions
        self._add_quit_button()
        self._add_bee()

    def _add_quit_button(self):
        btn = QPushButton("✕", self)
        btn.setFixedSize(30, 30)
        btn.move(10, 50)  # top-left corner
        btn.clicked.connect(QApplication.quit)
        btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 0, 0, 150);
                color: white;
                border-radius: 15px;
                font-size: 14px;
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(255, 0, 0, 220);
            }
        """)
        btn.show()

    def _add_bee(self):
        bee_path = os.path.join(IMAGE_DIR, "bee.png")

        pixmap = QPixmap(bee_path)

        bee_label = QLabel(self)
        bee_label.setPixmap(pixmap)
        bee_label.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        bee_label.resize(pixmap.width(), pixmap.height())
        spawn_position_x, spawn_position_y = get_random_spawn_position(
            self.width() + WIDTH_OFFSET, self.height(), pixmap.width() + WIDTH_OFFSET, pixmap.height()
        )
        bee_label.move(spawn_position_x, spawn_position_y)
        bee_label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec())
