# utils/helpers.py

import cv2
import math


# =====================================================
# Draw Center Crosshair
# =====================================================

def draw_center(frame):

    h, w = frame.shape[:2]

    center_x = w // 2
    center_y = h // 2

    # Horizontal Line
    cv2.line(
        frame,
        (center_x - 20, center_y),
        (center_x + 20, center_y),
        (0, 255, 255),
        2
    )

    # Vertical Line
    cv2.line(
        frame,
        (center_x, center_y - 20),
        (center_x, center_y + 20),
        (0, 255, 255),
        2
    )

    cv2.circle(
        frame,
        (center_x, center_y),
        4,
        (0, 0, 255),
        -1
    )

    return frame


# =====================================================
# Draw Bounding Box
# =====================================================

def draw_box(frame, x, y, w, h, color=(0, 255, 0), thickness=2):

    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        color,
        thickness
    )

    return frame


# =====================================================
# Draw Label
# =====================================================

def draw_label(frame, text, x, y):

    cv2.putText(
        frame,
        text,
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )

    return frame


# =====================================================
# Draw Center Point
# =====================================================

def draw_point(frame, x, y):

    cv2.circle(
        frame,
        (x, y),
        5,
        (0, 0, 255),
        -1
    )

    return frame


# =====================================================
# Draw Coordinates
# =====================================================

def draw_coordinates(frame, x, y):

    cv2.putText(
        frame,
        f"({x}, {y})",
        (x + 10, y + 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 0),
        2,
        cv2.LINE_AA
    )

    return frame


# =====================================================
# Distance Between Two Points
# =====================================================

def distance(x1, y1, x2, y2):

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )


# =====================================================
# Draw Confidence
# =====================================================

def draw_confidence(frame, confidence, x, y):

    cv2.putText(
        frame,
        f"{confidence:.1f}%",
        (x, y + 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 255),
        2,
        cv2.LINE_AA
    )

    return frame


# =====================================================
# Resize Frame
# =====================================================

def resize_frame(frame, width=1280, height=720):

    return cv2.resize(
        frame,
        (width, height)
    )