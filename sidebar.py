# ui/sidebar.py

from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QPushButton,
    QLabel
)

from PyQt6.QtCore import Qt


class Sidebar(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")

        self.setFixedWidth(240)

        self.setup_ui()

    # =====================================================

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(15, 15, 15, 15)

        layout.setSpacing(12)

        # ==========================================
        # Logo
        # ==========================================

        logo = QLabel("🤖")

        logo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        logo.setStyleSheet("""

            font-size:48px;

        """)

        layout.addWidget(logo)

        title = QLabel("AI ROBOT")

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setStyleSheet("""

            font-size:20px;

            font-weight:bold;

            color:#00BFFF;

        """)

        layout.addWidget(title)

        version = QLabel("Version 2.0")

        version.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        version.setStyleSheet("color:gray;")

        layout.addWidget(version)

        layout.addSpacing(15)



                # ==========================================
        # Helper Function
        # ==========================================

        def create_button(text):

            button = QPushButton(text)

            button.setMinimumHeight(45)

            button.setCursor(
                Qt.CursorShape.PointingHandCursor
            )

            return button

        # ==========================================
        # Buttons
        # ==========================================

        self.dashboard_btn = create_button(
            "🏠 Dashboard"
        )

        self.camera_btn = create_button(
            "📷 Start Camera"
        )

        self.color_btn = create_button(
            "🎨 Color Detection"
        )

        self.object_btn = create_button(
            "🧠 Object Detection"
        )

        self.qr_btn = create_button(
            "🔳 QR Scanner"
        )

        self.aruco_btn = create_button(
            "🏷 ArUco Detection"
        )

        self.robot_btn = create_button(
            "🤖 Robot Control"
        )

        self.settings_btn = create_button(
            "⚙ Settings"
        )

        self.exit_btn = create_button(
            "❌ Exit"
        )

        buttons = [

            self.dashboard_btn,

            self.camera_btn,

            self.color_btn,

            self.object_btn,

            self.qr_btn,

            self.aruco_btn,

            self.robot_btn,

            self.settings_btn,

            self.exit_btn

        ]

        for button in buttons:

            layout.addWidget(button)

        layout.addStretch()

        footer = QLabel("© 2026 AI Robotic Arm")

        footer.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        footer.setStyleSheet("""

            color:gray;

            font-size:11px;

            padding-top:10px;

        """)

        layout.addWidget(footer)



        