from cvtransit.models.seat import Seat

class Row:

    def __init__(self):
        self._occupancy = []

    def get_occupancy(self):
        return self._occupancy

    def set_occupancy(self, seat_count=12):
        seats = [Seat() for i in range(0, seat_count)]
        self._occupancy = seats
