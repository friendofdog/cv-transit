from cvtransit.models.seat import Seat  # type: ignore


class Car:

    def __init__(self, seat_count):
        self._seat_count = seat_count
        self._seats = []
        self._commuters = []

    def get_seats(self):
        return self._seats

    def set_seats(self):
        seats = [Seat() for seat in range(0, self._seat_count)]
        self._seats = seats

    def get_commuters(self):
        return self._commuters

    def add_commuter(self, commuter):
        self._commuters.append(commuter)

    def remove_commuter(self, commuter):
        self._commuters.remove(commuter)
