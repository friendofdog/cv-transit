import unittest
from tests.helpers import make_dummy_car_obj
from cvtransit.cycle import (
    decrement_commuter_duration,
    unseat_expired_commuters,
    # set_seat_threat,
    # set_seat_exposure,
    # seat_commuters
)


class TestCycle(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCycle, self).__init__(*args, **kwargs)

    def test_decrement_time_decreases_commuter_duration_by_one(self):
        car = make_dummy_car_obj([3, 2, 1])
        initial = [d.get_duration() for d in car.get_commuters()]
        decrement_commuter_duration(car)
        final = [d.get_duration() for d in car.get_commuters()]
        self.assertEqual(final, [d - 1 for d in initial])

    def test_unseat_expired_commuters_removes_commuter_if_duration_zero(self):
        commuters = [2, 1, 0]
        car = make_dummy_car_obj(commuters)
        unseat_expired_commuters(car)
        self.assertEqual(len(car.get_commuters()), len(commuters) - 1)

    def test_set_seat_threat_sets_seat_threat_prop(self):
        pass

    def test_set_seat_exposure_sets_seat_exposure_prop(self):
        pass

    def test_seat_commuters_appends_to_seat_seats_prop(self):
        pass
