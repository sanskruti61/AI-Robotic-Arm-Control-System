# camera/aruco_detection.py

import cv2
import numpy as np

from utils.helpers import (
    draw_point,
    draw_coordinates
)


class ArucoDetector:

    def __init__(self):

        # Dictionary
        self.dictionary = cv2.aruco.getPredefinedDictionary(
            cv2.aruco.DICT_4X4_50
        )

        # Detector Parameters
        self.parameters = cv2.aruco.DetectorParameters()

        # Detector
        self.detector = cv2.aruco.ArucoDetector(
            self.dictionary,
            self.parameters
        )

    # =====================================================

    def detect(self, frame):

        corners, ids, _ = self.detector.detectMarkers(
            frame
        )

        detection = None

        if ids is not None:

            cv2.aruco.drawDetectedMarkers(
                frame,
                corners,
                ids
            )

            for marker_corner, marker_id in zip(corners, ids):

                pts = marker_corner.reshape((4, 2)).astype(int)

                center_x = int(np.mean(pts[:, 0]))
                center_y = int(np.mean(pts[:, 1]))

                draw_point(
                    frame,
                    center_x,
                    center_y
                )

                draw_coordinates(
                    frame,
                    center_x,
                    center_y
                )

                cv2.putText(

                    frame,

                    f"ID : {int(marker_id)}",

                    (center_x - 30, center_y - 20),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.7,

                    (0, 255, 0),

                    2

                )

                detection = {

                    "type": "aruco",

                    "id": int(marker_id),

                    "x": center_x,

                    "y": center_y

                }

        return frame, detection