# camera/qr_detection.py

import cv2

from utils.helpers import (
    draw_box,
    draw_label,
    draw_point,
    draw_coordinates
)


class QRDetector:

    def __init__(self):

        self.detector = cv2.QRCodeDetector()

    # =====================================================

    def detect(self, frame):

        detection = None

        data, points, _ = self.detector.detectAndDecode(frame)

        if points is not None and data != "":

            points = points.astype(int)

            pts = points[0]

            x = min(pts[:, 0])
            y = min(pts[:, 1])

            w = max(pts[:, 0]) - x
            h = max(pts[:, 1]) - y

            center_x = x + w // 2
            center_y = y + h // 2

            draw_box(
                frame,
                x,
                y,
                w,
                h,
                color=(255, 0, 0)
            )

            draw_label(
                frame,
                "QR Code",
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

            cv2.putText(

                frame,

                data,

                (x, y + h + 25),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.6,

                (0, 255, 255),

                2

            )

            detection = {

                "type": "qr",

                "data": data,

                "x": center_x,

                "y": center_y,

                "width": w,

                "height": h

            }

        return frame, detection