from cvtransit.models.seat import Seat  # type: ignore


class Row:

    def __init__(self, seat_count):
        self._seat_count = seat_count
        self._occupancy = []

    def get_occupancy(self):
        return self._occupancy

    def set_occupancy(self):
        seats = [Seat() for i in range(0, self._seat_count)]
        self._occupancy = seats
