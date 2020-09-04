import random


class Commuter:

    def __init__(self):
        self._mask = True
        self._time = 30

    def get_mask(self):
        return self._mask

    def set_mask(self):
        self._mask = random.random() > 0.1

    def get_time(self):
        return self._time

    def set_time(self):
        self._time -= 1
