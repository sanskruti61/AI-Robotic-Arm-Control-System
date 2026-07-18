# utils/fps.py

import time
import cv2


class FPSCounter:
    """
    Calculates and displays Frames Per Second (FPS).
    """

    def __init__(self):

        self.prev_time = time.time()

        self.curr_time = time.time()

        self.fps = 0

    # ==================================================

    def update(self):

        self.curr_time = time.time()

        diff = self.curr_time - self.prev_time

        if diff > 0:

            self.fps = 1 / diff

        self.prev_time = self.curr_time

        return self.fps

    # ==================================================

    def draw(self, frame):

        fps = self.update()

        cv2.putText(

            frame,

            f"FPS : {int(fps)}",

            (20, 35),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.8,

            (0, 255, 0),

            2,

            cv2.LINE_AA

        )

        return frame