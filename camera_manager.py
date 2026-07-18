# camera/camera_manager.py

import cv2


class CameraManager:
    """
    Handles all webcam operations.
    """

    def __init__(self):

        self.cap = None

        self.running = False

    # ======================================================

    def start(self, camera_index=0):

        """
        Start the webcam.
        """

        if self.running:
            return True

        self.cap = cv2.VideoCapture(camera_index)

        if not self.cap.isOpened():

            self.cap = None

            self.running = False

            return False

        # Set camera resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        self.running = True

        return True

    # ======================================================

    def read(self):

        """
        Read one frame from webcam.
        """

        if not self.running:
            return None

        if self.cap is None:
            return None

        success, frame = self.cap.read()

        if not success:
            return None

        # Mirror effect
        frame = cv2.flip(frame, 1)

        return frame

    # ======================================================

    def stop(self):

        """
        Stop webcam.
        """

        if self.cap is not None:

            self.cap.release()

            self.cap = None

        self.running = False

    # ======================================================

    def is_running(self):

        """
        Returns True if camera is running.
        """

        return self.running