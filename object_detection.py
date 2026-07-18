# camera/object_detection.py

import cv2
from ultralytics import YOLO

from utils.helpers import (
    draw_box,
    draw_label,
    draw_point,
    draw_coordinates,
    draw_confidence
)


class ObjectDetector:

    def __init__(self):

        # Load YOLOv8 Nano model
        self.model = YOLO("yolov8n.pt")

    # =====================================================

    def detect(self, frame):

        detection = None

        results = self.model(
            frame,
            verbose=False
        )

        largest_area = 0

        for result in results:

            for box in result.boxes:

                confidence = float(box.conf[0]) * 100

                if confidence < 50:
                    continue

                cls = int(box.cls[0])

                label = self.model.names[cls]

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                width = x2 - x1
                height = y2 - y1

                area = width * height

                if area < largest_area:
                    continue

                largest_area = area

                center_x = x1 + width // 2
                center_y = y1 + height // 2

                draw_box(
                    frame,
                    x1,
                    y1,
                    width,
                    height,
                    color=(0, 255, 0)
                )

                draw_label(
                    frame,
                    label,
                    x1,
                    y1
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

                draw_confidence(
                    frame,
                    confidence,
                    x1,
                    y1
                )

                detection = {

                    "type": "object",

                    "label": label,

                    "confidence": round(confidence, 1),

                    "x": center_x,

                    "y": center_y,

                    "width": width,

                    "height": height,

                    "area": area

                }

        return frame, detection