# ui/camera_widget.py

import cv2

from PyQt6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)

from PyQt6.QtCore import (
    Qt,
    QTimer
)

from PyQt6.QtGui import (
    QImage,
    QPixmap
)

# ------------------------------------
# Camera Modules
# ------------------------------------

from camera.camera_manager import CameraManager
from camera.color_detection import ColorDetector
from camera.object_detection import ObjectDetector
from camera.qr_detection import QRDetector
from camera.aruco_detection import ArucoDetector

# ------------------------------------
# Utilities
# ------------------------------------

from utils.fps import FPSCounter
from utils.helpers import draw_center


class CameraWidget(QFrame):

    def __init__(self):

        super().__init__()

        self.setObjectName("cameraFrame")

        # ===================================
        # Camera
        # ===================================

        self.camera = CameraManager()

        # ===================================
        # AI Modules
        # ===================================

        self.color_detector = ColorDetector()

        self.object_detector = ObjectDetector()

        self.qr_detector = QRDetector()

        self.aruco_detector = ArucoDetector()

        # ===================================
        # FPS
        # ===================================

        self.fps = FPSCounter()

        # ===================================
        # Current Detection Mode
        # ===================================

        self.mode = "camera"

        # camera
        # color
        # object
        # qr
        # aruco

        # ===================================
        # Current Detection Results
        # ===================================

        self.current_detection = None

        self.current_color = None

        self.current_object = None

        self.current_qr = None

        self.current_marker = None

        # ===================================
        # Timer
        # ===================================

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_frame
        )

        # ===================================

        self.setup_ui()



            # ====================================================
    # UI
    # ====================================================

    def setup_ui(self):

        layout = QVBoxLayout(self)

        # =====================================
        # Title
        # =====================================

        title = QLabel("📷 LIVE CAMERA")

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setStyleSheet("""

            font-size:22px;

            font-weight:bold;

            color:#00BFFF;

            padding:10px;

        """)

        layout.addWidget(title)

        # =====================================
        # Current Mode
        # =====================================

        self.mode_label = QLabel(
            "Current Mode : Camera"
        )

        self.mode_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.mode_label.setStyleSheet("""

            font-size:16px;

            color:#00FF99;

            padding:5px;

        """)

        layout.addWidget(
            self.mode_label
        )

        # =====================================
        # Camera View
        # =====================================

        self.camera_label = QLabel()

        self.camera_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.camera_label.setMinimumSize(
            900,
            600
        )

        self.camera_label.setStyleSheet("""

            background:#111;

            border:2px solid #555;

            border-radius:10px;

            color:white;

            font-size:18px;

        """)

        self.camera_label.setText(
            "Camera is OFF\n\nPress 'Start Camera'"
        )

        layout.addWidget(
            self.camera_label
        )

        # =====================================
        # Camera Status
        # =====================================

        self.status = QLabel(
            "🔴 Camera Stopped"
        )

        self.status.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.status.setStyleSheet("""

            font-size:15px;

            color:white;

            padding:6px;

        """)

        layout.addWidget(
            self.status
        )

        self.setLayout(layout)



            # ====================================================
    # Camera Controls
    # ====================================================

    def start_camera(self):

        if self.camera.start():

            self.status.setText(
                "🟢 Camera Running"
            )

            self.timer.start(30)

            return True

        self.status.setText(
            "🔴 Camera Not Found"
        )

        return False

    # ====================================================

    def stop_camera(self):

        self.timer.stop()

        self.camera.stop()

        self.camera_label.clear()

        self.camera_label.setText(
            "Camera is OFF\n\nPress 'Start Camera'"
        )

        self.status.setText(
            "🔴 Camera Stopped"
        )

        # Reset all detections

        self.current_detection = None
        self.current_color = None
        self.current_object = None
        self.current_qr = None
        self.current_marker = None

        self.mode = "camera"

        self.mode_label.setText(
            "Current Mode : Camera"
        )

    # ====================================================

    def close_camera(self):

        self.stop_camera()

    # ====================================================

    def is_running(self):

        return self.camera.is_running()
    


        # ====================================================
    # Detection Modes
    # ====================================================

    def set_mode(self, mode):

        self.mode = mode

        mode_names = {

            "camera": "📷 Camera",

            "color": "🎨 Color Detection",

            "object": "🧠 Object Detection",

            "qr": "🔳 QR Scanner",

            "aruco": "🏷 ArUco Detection"

        }

        self.mode_label.setText(

            f"Current Mode : {mode_names.get(mode, 'Camera')}"

        )

    # ====================================================

    def toggle_color_detection(self):

        if self.mode == "color":

            self.set_mode("camera")

        else:

            self.set_mode("color")

    # ====================================================

    def toggle_object_detection(self):

        if self.mode == "object":

            self.set_mode("camera")

        else:

            self.set_mode("object")

    # ====================================================

    def toggle_qr_detection(self):

        if self.mode == "qr":

            self.set_mode("camera")

        else:

            self.set_mode("qr")

    # ====================================================

    def toggle_aruco_detection(self):

        if self.mode == "aruco":

            self.set_mode("camera")

        else:

            self.set_mode("aruco")

    # ====================================================

    def reset_detections(self):

        self.current_detection = None

        self.current_color = None

        self.current_object = None

        self.current_qr = None

        self.current_marker = None



            # ====================================================
    # Update Camera Frame
    # ====================================================

    def update_frame(self):

        frame = self.camera.read()

        if frame is None:
            return

        # ==========================================
        # Draw Center Crosshair
        # ==========================================

        draw_center(frame)

        # ==========================================
        # Current FPS
        # ==========================================

        fps = self.fps.update()

        cv2.putText(

            frame,

            f"FPS : {int(fps)}",

            (15, 30),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.8,

            (0, 255, 0),

            2

        )

        # ==========================================
        # Camera Mode
        # ==========================================

        self.current_detection = None

        if self.mode == "color":

            frame, detection = self.color_detector.detect(frame)

            self.current_detection = detection
            self.current_color = detection

        elif self.mode == "object":

            frame, detection = self.object_detector.detect(frame)

            self.current_detection = detection
            self.current_object = detection

        elif self.mode == "qr":

            frame, detection = self.qr_detector.detect(frame)

            self.current_detection = detection
            self.current_qr = detection

        elif self.mode == "aruco":

            frame, detection = self.aruco_detector.detect(frame)

            self.current_detection = detection
            self.current_marker = detection

        # ==========================================
        # Display Current Mode
        # ==========================================

        cv2.putText(

            frame,

            f"Mode : {self.mode.upper()}",

            (15, 65),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.7,

            (255, 255, 0),

            2

        )

        # ==========================================
        # Convert OpenCV -> Qt
        # ==========================================

        rgb = cv2.cvtColor(

            frame,

            cv2.COLOR_BGR2RGB

        )

        h, w, ch = rgb.shape

        image = QImage(

            rgb.data,

            w,

            h,

            ch * w,

            QImage.Format.Format_RGB888

        )

        pixmap = QPixmap.fromImage(image)

        self.camera_label.setPixmap(

            pixmap.scaled(

                self.camera_label.width(),

                self.camera_label.height(),

                Qt.AspectRatioMode.KeepAspectRatio,

                Qt.TransformationMode.SmoothTransformation

            )

        )