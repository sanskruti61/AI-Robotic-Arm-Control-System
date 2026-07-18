# utils/logger.py

from datetime import datetime


class Logger:

    def __init__(self):

        self.logs = []

    # =====================================

    def add(self, message):

        time = datetime.now().strftime("%H:%M:%S")

        text = f"[{time}] {message}"

        self.logs.append(text)

        print(text)

    # =====================================

    def latest(self):

        if len(self.logs) == 0:

            return ""

        return self.logs[-1]

    # =====================================

    def all(self):

        return self.logs