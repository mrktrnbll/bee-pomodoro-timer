"""main entry point for bee pomodoro app"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtCore import Qt, QTimer
import sys
import os

from sprites.movement_handlers import (
    add_position_to_populated_positions,
    get_unpopulated_spawn_position,
)
from sprites.general import (
    load_sprite,
    load_random_flower,
)
from src.bee_pomodoro_app.interface.timer import (
    add_second_to_timer,
    has_five_minutes_passed,
    has_twenty_five_minutes_passed,
    has_thirty_minutes_passed,
    reset_timer,
)


ASSETS_DIR = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), "assets")
IMAGE_DIR = os.path.join(ASSETS_DIR, "images")
# MAGIC_NUMBERS
WIDTH_OFFSET = 40


class TransparentWindow(QMainWindow):
    def __init__(self, timer_label: QAction, menu: QMenu):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint # |
            # Qt.WindowType.Tool
        )

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen)

        self.current_timer_running: bool = False
        self.populated_positions: list[tuple[int, int]] = []
        self.flowers: list[QPixmap] = [load_sprite(f"flower{i}.png", IMAGE_DIR) for i in range(1, 6)]

        # UI elements
        self.stop_resume_button = QAction("▶ Resume")
        self.stop_resume_button.triggered.connect(self._stop_resume_timer)
        self.quit = QAction("🆇 Quit")
        self.quit.triggered.connect(QApplication.quit)
        # add to window based functions
        self._add_bee()
        self._add_random_flower()

        self.timer_label = timer_label
        self.menu = menu
        self._init_timer()
        self._init_status_menu_buttons()

    def _init_timer(self):
        self.qtimer = QTimer()
        self.qtimer.setInterval(1000)
        self.qtimer.timeout.connect(self._update_timer_menu)

    def _init_status_menu_buttons(self):
        """Initialize the buttons in the macOS menu bar."""
        self.menu.addSeparator()
        self.menu.addAction(self.stop_resume_button)
        self.menu.addAction(self.quit)

    def _stop_resume_timer(self):
        if self.current_timer_running:
            self.current_timer_running = False
            self.stop_resume_button.setText("▶ Resume")
            self.qtimer.stop()
        else:
            self.current_timer_running = True
            self.stop_resume_button.setText("■ Pause")
            self.qtimer.start()

    def _add_bee(self):
        bee_path = os.path.join(IMAGE_DIR, "bee.png")

        pixmap = QPixmap(bee_path)

        bee_label = QLabel(self)
        bee_label.setPixmap(pixmap)
        bee_label.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        bee_label.resize(pixmap.width(), pixmap.height())
        spawn_position_x, spawn_position_y = get_unpopulated_spawn_position(
            self, self.width() - WIDTH_OFFSET, self.height(), pixmap.width(), pixmap.height()
        )
        bee_label.move(spawn_position_x, spawn_position_y)
        add_position_to_populated_positions(self, spawn_position_x, spawn_position_y)
        bee_label.show()

    def _add_random_flower(self):
        flower_pixmap = load_random_flower(self.flowers)
        flower_label = QLabel(self)
        flower_label.setPixmap(flower_pixmap)
        flower_label.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        flower_label.resize(flower_pixmap.width(), flower_pixmap.height())
        spawn_position_x, spawn_position_y = get_unpopulated_spawn_position(
            self, self.width() - WIDTH_OFFSET, self.height(), flower_pixmap.width(), flower_pixmap.height()
        )
        flower_label.move(spawn_position_x, spawn_position_y)
        add_position_to_populated_positions(self, spawn_position_x, spawn_position_y)
        flower_label.show()

    def _update_timer_menu(self):
        """Update the timer label in the macOS menu bar."""
        new_time_to_display: str = add_second_to_timer(self.timer_label.text())
        self.timer_label.setText(new_time_to_display)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(ASSETS_DIR, "bee.ico")))

    tray = QSystemTrayIcon()
    tray.setIcon(QIcon(os.path.join(ASSETS_DIR, "bee.ico")))
    tray.setVisible(True)
    menu = QMenu()
    timer_label = QAction("00:55")
    timer_label.setDisabled(True)
    menu.addAction(timer_label)
    tray.setContextMenu(menu)

    window = TransparentWindow(timer_label, menu)
    window.setWindowTitle("Bee Pomodoro")
    window.show()
    sys.exit(app.exec())
