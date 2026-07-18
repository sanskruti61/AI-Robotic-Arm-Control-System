# ui/main_window.py

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QStatusBar
)

from PyQt6.QtCore import (
    Qt,
    QTimer
)

from ui.styles import STYLE
from ui.sidebar import Sidebar
from ui.camera_widget import CameraWidget
from ui.info_panel import InfoPanel
from ui.console import Console


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "AI Robotic Arm Control System"
        )

        self.resize(1600, 900)

        self.setMinimumSize(
            1400,
            800
        )

        self.setStyleSheet(
            STYLE
        )

        # ----------------------------

        self.build_ui()

        self.connect_signals()

        # ----------------------------
        # Update Timer
        # ----------------------------

        self.info_timer = QTimer()

        self.info_timer.timeout.connect(
            self.update_detection_info
        )

        self.info_timer.start(100)



            # =====================================================
    # Build UI
    # =====================================================

    def build_ui(self):

        # ---------------------------------------
        # Central Widget
        # ---------------------------------------

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )

        main_layout = QVBoxLayout()

        central_widget.setLayout(
            main_layout
        )

        # ---------------------------------------
        # Header
        # ---------------------------------------

        title = QLabel(
            "🤖 AI ROBOTIC ARM CONTROL SYSTEM"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setStyleSheet("""

            font-size:30px;

            font-weight:bold;

            color:#00BFFF;

            padding:15px;

        """)

        main_layout.addWidget(
            title
        )

        # ---------------------------------------
        # Main Body
        # ---------------------------------------

        body_layout = QHBoxLayout()

        # Sidebar

        self.sidebar = Sidebar()

        # Camera Widget

        self.camera = CameraWidget()

        # Information Panel

        self.info = InfoPanel()

        body_layout.addWidget(
            self.sidebar
        )

        body_layout.addWidget(
            self.camera,
            1
        )

        body_layout.addWidget(
            self.info
        )

        main_layout.addLayout(
            body_layout
        )

        # ---------------------------------------
        # Console
        # ---------------------------------------

        self.console = Console()

        main_layout.addWidget(
            self.console
        )

        # ---------------------------------------
        # Status Bar
        # ---------------------------------------

        self.status = QStatusBar()

        self.setStatusBar(
            self.status
        )

        self.status.showMessage(

            "Camera : OFF | Robot : OFF | AI : Ready"

        )


            # =====================================================
    # Connect Signals
    # =====================================================

    def connect_signals(self):

        # -----------------------------------
        # Camera
        # -----------------------------------

        self.sidebar.camera_btn.clicked.connect(
            self.toggle_camera
        )

        # -----------------------------------
        # Color Detection
        # -----------------------------------

        self.sidebar.color_btn.clicked.connect(

            self.toggle_color_detection

        )

        # -----------------------------------
        # Object Detection
        # -----------------------------------

        self.sidebar.object_btn.clicked.connect(

            self.toggle_object_detection

        )

        # -----------------------------------
        # QR Scanner
        # -----------------------------------

        self.sidebar.qr_btn.clicked.connect(

            self.toggle_qr_detection

        )

        # -----------------------------------
        # ArUco Detection
        # -----------------------------------

        self.sidebar.aruco_btn.clicked.connect(

            self.toggle_aruco_detection

        )

        # -----------------------------------
        # Robot Button
        # -----------------------------------

        self.sidebar.robot_btn.clicked.connect(

            self.robot_control

        )

        # -----------------------------------
        # Settings
        # -----------------------------------

        self.sidebar.settings_btn.clicked.connect(

            self.open_settings

        )

        # -----------------------------------
        # Dashboard
        # -----------------------------------

        self.sidebar.dashboard_btn.clicked.connect(

            self.show_dashboard

        )

        # -----------------------------------
        # Exit
        # -----------------------------------

        self.sidebar.exit_btn.clicked.connect(

            self.close

        )


            # =====================================================
    # Camera
    # =====================================================

    def toggle_camera(self):

        if self.camera.is_running():

            self.camera.stop_camera()

            self.sidebar.camera_btn.setText(
                "📷 Start Camera"
            )

            self.console.log(
                "Camera Stopped"
            )

            self.status.showMessage(
                "Camera : OFF | Robot : OFF"
            )

        else:

            if self.camera.start_camera():

                self.sidebar.camera_btn.setText(
                    "⏹ Stop Camera"
                )

                self.console.log(
                    "Camera Started"
                )

                self.status.showMessage(
                    "Camera : ON | Robot : OFF"
                )

            else:

                self.console.log(
                    "Unable to open camera"
                )

                self.status.showMessage(
                    "Camera Error"
                )

    # =====================================================
    # Color Detection
    # =====================================================

    def toggle_color_detection(self):

        self.camera.toggle_color_detection()

        self.console.log(
            "Color Detection Enabled"
        )

        self.status.showMessage(
            "Mode : Color Detection"
        )

    # =====================================================
    # Object Detection
    # =====================================================

    def toggle_object_detection(self):

        self.camera.toggle_object_detection()

        self.console.log(
            "Object Detection Enabled"
        )

        self.status.showMessage(
            "Mode : Object Detection"
        )

    # =====================================================
    # QR Detection
    # =====================================================

    def toggle_qr_detection(self):

        self.camera.toggle_qr_detection()

        self.console.log(
            "QR Scanner Enabled"
        )

        self.status.showMessage(
            "Mode : QR Scanner"
        )

    # =====================================================
    # ArUco Detection
    # =====================================================

    def toggle_aruco_detection(self):

        self.camera.toggle_aruco_detection()

        self.console.log(
            "ArUco Detection Enabled"
        )

        self.status.showMessage(
            "Mode : ArUco Detection"
        )

    # =====================================================
    # Robot Control
    # =====================================================

    def robot_control(self):

        self.console.log(
            "Robot Control Clicked"
        )

        self.status.showMessage(
            "Robot Control (Coming Soon)"
        )

    # =====================================================
    # Dashboard
    # =====================================================

    def show_dashboard(self):

        self.camera.set_mode("camera")

        self.console.log(
            "Dashboard Selected"
        )

        self.status.showMessage(
            "Dashboard"
        )

    # =====================================================
    # Settings
    # =====================================================

    def open_settings(self):

        self.console.log(
            "Settings Opened"
        )

        self.status.showMessage(
            "Settings"
        )


            # =====================================================
    # Update Detection Information
    # =====================================================

    def update_detection_info(self):

        # -----------------------------------
        # Mode
        # -----------------------------------

        if hasattr(self.info, "update_mode"):

            self.info.update_mode(
                self.camera.mode
            )

        # -----------------------------------
        # FPS
        # -----------------------------------

        if hasattr(self.info, "update_fps"):

            try:

                fps_value = self.camera.fps.update()

                self.info.update_fps(
                    fps_value
                )

            except:

                pass

        # -----------------------------------
        # Resolution
        # -----------------------------------

        if hasattr(
            self.info,
            "update_resolution"
        ):

            self.info.update_resolution(
                1280,
                720
            )

        # -----------------------------------
        # Color Detection
        # -----------------------------------

        if hasattr(
            self.info,
            "update_color"
        ):

            self.info.update_color(
                self.camera.current_color
            )

        # -----------------------------------
        # Object Detection
        # -----------------------------------

        if hasattr(
            self.info,
            "update_object"
        ):

            self.info.update_object(
                self.camera.current_object
            )

        # -----------------------------------
        # QR Detection
        # -----------------------------------

        if hasattr(
            self.info,
            "update_qr"
        ):

            self.info.update_qr(
                self.camera.current_qr
            )

        # -----------------------------------
        # ArUco Detection
        # -----------------------------------

        if hasattr(
            self.info,
            "update_marker"
        ):

            self.info.update_marker(
                self.camera.current_marker
            )

    # =====================================================
    # Close Event
    # =====================================================

    def closeEvent(self, event):

        try:

            self.info_timer.stop()

        except:

            pass

        try:

            self.camera.close_camera()

        except:

            pass

        self.console.log(
            "Application Closed"
        )

        event.accept()