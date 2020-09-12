from cvtransit.models.commuter import Commuter


class Seat:

    def __init__(self):
        self._exposure = 0
        self._threat = 0
        self._commuter = None

    def get_exposure(self):
        return self._exposure

    def set_exposure(self, adj):
        if len(adj) not in [1, 2]:
            raise ValueError(f"Expected length 1 or 2, got {len(adj)}")
        if not all(isinstance(x, int) for x in adj):
            raise TypeError(f"{adj} was given, expected list of integers")
        self._exposure = sum([i for i in adj])

    def get_threat(self):
        return self._threat

    def set_threat(self, time, base):
        self._threat = time * base

    def get_commuter(self):
        return self._commuter

    def set_commuter(self, commuter):
        if type(commuter) is Commuter:
            self._commuter = commuter
        else:
            raise TypeError(f'{commuter} is not an instance of Commuter')
