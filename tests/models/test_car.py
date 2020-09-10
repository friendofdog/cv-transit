from cvtransit.models.car import Car  # type: ignore
import unittest


class TestCar(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCar, self).__init__(*args, **kwargs)
        self.seat_count = 6
        self.car = Car(self.seat_count)

    def test_set_seats_creates_list(self):
        self.car.set_seats()
        self.assertEqual(type(self.car.get_seats()), list)
        self.assertEqual(len(self.car.get_seats()), self.seat_count)

    def test_Car_getter_setter(self):
        commuter = 'mock commuter'
        self.car.add_commuter(commuter)
        self.assertEqual(len(self.car.get_commuters()), 1)
        self.car.remove_commuter(commuter)
        self.assertEqual(len(self.car.get_commuters()), 0)
