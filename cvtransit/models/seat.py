class Seat:

    def __init__(self):
        self._exposure = 0
        self._threat = 0
        self._commuter = None

    def get_exposure(self):
        return self._exposure

    def set_exposure(self, adj):
        self._exposure = sum([i for i in adj])

    def get_threat(self):
        return self._threat

    def set_threat(self, time, base):
        self._threat = time * base

    def get_commuter(self):
        return self._commuter

    def set_commuter(self, commuter):
        self._commuter = commuter
