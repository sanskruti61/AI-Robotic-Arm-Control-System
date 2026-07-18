# camera/color_detection.py

import cv2
import numpy as np

from utils.helpers import (
    draw_box,
    draw_label,
    draw_point,
    draw_coordinates
)


class ColorDetector:
    """
    Detect colored objects using HSV thresholding.
    Returns:
        frame, detection
    """

    def __init__(self):

        self.colors = {

            "Red": [
                (
                    np.array([0, 120, 70]),
                    np.array([10, 255, 255])
                ),
                (
                    np.array([170, 120, 70]),
                    np.array([180, 255, 255])
                )
            ],

            "Green": [
                (
                    np.array([35, 70, 70]),
                    np.array([85, 255, 255])
                )
            ],

            "Blue": [
                (
                    np.array([90, 80, 60]),
                    np.array([130, 255, 255])
                )
            ],

            "Yellow": [
                (
                    np.array([20, 100, 100]),
                    np.array([35, 255, 255])
                )
            ]

        }

    # =====================================================

    def detect(self, frame):

        hsv = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2HSV
        )

        best_detection = None

        largest_area = 0

        kernel = np.ones((5, 5), np.uint8)

        for color_name, ranges in self.colors.items():

            mask = None

            for lower, upper in ranges:

                current = cv2.inRange(
                    hsv,
                    lower,
                    upper
                )

                if mask is None:
                    mask = current
                else:
                    mask = cv2.bitwise_or(
                        mask,
                        current
                    )

            # -------------------------
            # Noise Removal
            # -------------------------

            mask = cv2.GaussianBlur(
                mask,
                (5, 5),
                0
            )

            mask = cv2.morphologyEx(
                mask,
                cv2.MORPH_OPEN,
                kernel
            )

            mask = cv2.morphologyEx(
                mask,
                cv2.MORPH_CLOSE,
                kernel
            )

            contours, _ = cv2.findContours(

                mask,

                cv2.RETR_EXTERNAL,

                cv2.CHAIN_APPROX_SIMPLE

            )

            for contour in contours:

                area = cv2.contourArea(contour)

                if area < 2500:
                    continue

                if area < largest_area:
                    continue

                x, y, w, h = cv2.boundingRect(
                    contour
                )

                center_x = x + w // 2
                center_y = y + h // 2

                draw_box(
                    frame,
                    x,
                    y,
                    w,
                    h
                )

                draw_label(
                    frame,
                    color_name,
                    x,
                    y
                )

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

                largest_area = area

                best_detection = {

                    "type": "color",

                    "color": color_name,

                    "x": center_x,

                    "y": center_y,

                    "width": w,

                    "height": h,

                    "area": int(area)

                }

        return frame, best_detection