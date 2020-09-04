class Seat:

    def __init__(self):
        self._exposure = 0
        self._threat = 0

    def get_exposure(self):
        return self._exposure

    def set_exposure(self, adj):
        if len(adj) in [1, 2]:
            self._exposure = sum([i for i in adj])
        else:
            raise ValueError(f"Expected length 1 or 2, got {len(adj)}")

    def get_threat(self):
        return self._threat

    def set_threat(self, time, base):
        self._threat = time * base
