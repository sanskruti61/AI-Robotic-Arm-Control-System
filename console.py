# ui/console.py

from PyQt6.QtWidgets import (
    QFrame,
    QLabel,
    QTextEdit,
    QVBoxLayout
)

from PyQt6.QtCore import QDateTime


class Console(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("consoleFrame")

        self.setup_ui()

    # =====================================================

    def setup_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("💻 SYSTEM CONSOLE")

        title.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
            color:#00BFFF;
            padding:5px;
        """)

        layout.addWidget(title)

        self.console = QTextEdit()

        self.console.setReadOnly(True)

        self.console.setStyleSheet("""

            background:#111;

            color:#00FF99;

            font-family:Consolas;

            font-size:12px;

            border:2px solid #444;

            border-radius:8px;

            padding:8px;

        """)

        layout.addWidget(self.console)

        self.log("System Started")

    # =====================================================

    def log(self, message):

        time = QDateTime.currentDateTime().toString(
            "hh:mm:ss"
        )

        self.console.append(
            f"[{time}] {message}"
        )

    # =====================================================

    def clear(self):

        self.console.clear()

        self.log("Console Cleared")