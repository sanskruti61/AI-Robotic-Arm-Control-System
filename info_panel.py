# ui/info_panel.py

from PyQt6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QGroupBox,
    QFormLayout
)

from PyQt6.QtCore import Qt


class InfoPanel(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("infoPanel")
        self.setFixedWidth(330)

        self.setup_ui()

    # =====================================================

    def setup_ui(self):

        main_layout = QVBoxLayout(self)

        # ===========================================
        # Title
        # ===========================================

        title = QLabel("📊 AI STATUS PANEL")

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
            color:#00BFFF;
            padding:10px;
        """)

        main_layout.addWidget(title)

        # ===========================================
        # CAMERA GROUP
        # ===========================================

        camera_group = QGroupBox("📷 Camera")

        camera_layout = QFormLayout()

        self.mode_label = QLabel("Camera")

        self.fps_label = QLabel("0")

        self.resolution_label = QLabel("1280 x 720")

        camera_layout.addRow("Mode :", self.mode_label)
        camera_layout.addRow("FPS :", self.fps_label)
        camera_layout.addRow("Resolution :", self.resolution_label)

        camera_group.setLayout(camera_layout)

        main_layout.addWidget(camera_group)

        # ===========================================
        # DETECTION GROUP
        # ===========================================

        detection_group = QGroupBox("🧠 Detection")

        detection_layout = QFormLayout()

        self.object_label = QLabel("None")

        self.color_label = QLabel("None")

        self.confidence_label = QLabel("0 %")

        self.x_label = QLabel("0")

        self.y_label = QLabel("0")

        self.area_label = QLabel("0")

        detection_layout.addRow("Object :", self.object_label)
        detection_layout.addRow("Color :", self.color_label)
        detection_layout.addRow("Confidence :", self.confidence_label)
        detection_layout.addRow("Center X :", self.x_label)
        detection_layout.addRow("Center Y :", self.y_label)
        detection_layout.addRow("Area :", self.area_label)

        detection_group.setLayout(detection_layout)

        main_layout.addWidget(detection_group)


                # ===========================================
        # MARKERS GROUP
        # ===========================================

        marker_group = QGroupBox("🏷 Detection Markers")

        marker_layout = QFormLayout()

        self.marker_label = QLabel("None")

        self.qr_label = QLabel("None")

        marker_layout.addRow(
            "ArUco ID :",
            self.marker_label
        )

        marker_layout.addRow(
            "QR Data :",
            self.qr_label
        )

        marker_group.setLayout(marker_layout)

        main_layout.addWidget(marker_group)

        # ===========================================
        # ROBOT GROUP
        # ===========================================

        robot_group = QGroupBox("🤖 Robot")

        robot_layout = QFormLayout()

        self.robot_label = QLabel("Disconnected")

        self.robot_status_label = QLabel("Idle")

        robot_layout.addRow(
            "Connection :",
            self.robot_label
        )

        robot_layout.addRow(
            "Action :",
            self.robot_status_label
        )

        robot_group.setLayout(robot_layout)

        main_layout.addWidget(robot_group)

        # ===========================================
        # STATUS
        # ===========================================

        self.status_label = QLabel("🟢 System Ready")

        self.status_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.status_label.setStyleSheet("""

            background:#1f8f4d;

            color:white;

            font-size:14px;

            font-weight:bold;

            border-radius:8px;

            padding:8px;

        """)

        main_layout.addWidget(self.status_label)

        main_layout.addStretch()



            # =====================================================
    # Camera Updates
    # =====================================================

    def update_mode(self, mode):

        self.mode_label.setText(mode)

    # =====================================================

    def update_fps(self, fps):

        self.fps_label.setText(str(int(fps)))

    # =====================================================

    def update_resolution(self, width, height):

        self.resolution_label.setText(f"{width} x {height}")

    # =====================================================
    # Color Detection
    # =====================================================

    def update_color(self, detection):

        if detection is None:

            self.color_label.setText("None")
            self.x_label.setText("0")
            self.y_label.setText("0")
            self.area_label.setText("0")

            return

        self.color_label.setText(
            detection.get("color", "None")
        )

        self.x_label.setText(
            str(detection.get("x", 0))
        )

        self.y_label.setText(
            str(detection.get("y", 0))
        )

        self.area_label.setText(
            str(detection.get("area", 0))
        )

    # =====================================================
    # Object Detection
    # =====================================================

    def update_object(self, detection):

        if detection is None:

            self.object_label.setText("None")
            self.confidence_label.setText("0 %")

            return

        self.object_label.setText(
            detection.get("label", "Unknown")
        )

        self.confidence_label.setText(
            f"{detection.get('confidence',0)} %"
        )

        self.x_label.setText(
            str(detection.get("x", 0))
        )

        self.y_label.setText(
            str(detection.get("y", 0))
        )

        self.area_label.setText(
            str(detection.get("area", 0))
        )

    # =====================================================
    # QR Detection
    # =====================================================

    def update_qr(self, detection):

        if detection is None:

            self.qr_label.setText("None")

            return

        self.qr_label.setText(
            detection.get("data", "None")
        )

    # =====================================================
    # ArUco Detection
    # =====================================================

    def update_marker(self, detection):

        if detection is None:

            self.marker_label.setText("None")

            return

        self.marker_label.setText(
            str(detection.get("id", "None"))
        )

    # =====================================================
    # Robot Status
    # =====================================================

    def update_robot(self, connected=False, action="Idle"):

        if connected:

            self.robot_label.setText("Connected")

        else:

            self.robot_label.setText("Disconnected")

        self.robot_status_label.setText(action)

    # =====================================================
    # Reset Everything
    # =====================================================

    def reset(self):

        self.update_mode("Camera")

        self.update_fps(0)

        self.update_resolution(1280, 720)

        self.color_label.setText("None")

        self.object_label.setText("None")

        self.confidence_label.setText("0 %")

        self.x_label.setText("0")

        self.y_label.setText("0")

        self.area_label.setText("0")

        self.marker_label.setText("None")

        self.qr_label.setText("None")

        self.robot_label.setText("Disconnected")

        self.robot_status_label.setText("Idle")