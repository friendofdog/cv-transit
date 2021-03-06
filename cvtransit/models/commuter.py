import random


class Commuter:

    def __init__(self, duration, nomask):
        self._duration = duration
        self._mask = True
        self._nomask = nomask

    def get_mask(self):
        return self._mask

    def set_mask(self):
        self._mask = random.random() > self._nomask

    def get_duration(self):
        return self._duration

    def decrement_duration(self):
        self._duration -= 1
