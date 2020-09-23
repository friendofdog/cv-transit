import unittest
from tests.helpers import make_dummy_car_obj, populate_dummy_car_seats
from cvtransit.cycle import (
    decrement_commuter_duration,
    unseat_expired_commuters,
    set_seat_threat,
    set_seat_exposure,
    seat_commuters
)


BASE_THREAT = 100  # temporary, move to config file


class TestCycle(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCycle, self).__init__(*args, **kwargs)
        stand_count = 4
        self.commuters = [(3, 10), (3, 0), (5, 10), (1, 0), (8, 0), (9, 10),
                          (11, 0), (10, 0)]
        self.standing = self.commuters[:-stand_count]
        self.car = make_dummy_car_obj(self.commuters, -stand_count)
        populate_dummy_car_seats(self.car, -stand_count)

    def test_decrement_time_decreases_commuter_duration_by_one(self):
        initial = [d.get_duration() for d in self.car.get_commuters()]
        decrement_commuter_duration(self.car)
        final = [d.get_duration() for d in self.car.get_commuters()]
        self.assertEqual(final, [d - 1 for d in initial])

    def test_unseat_expired_commuters_removes_commuter_if_duration_zero(self):
        decrement_commuter_duration(self.car)  # depends on another method
        unseat_expired_commuters(self.car)
        self.assertEqual(
            len(self.car.get_commuters()), len(self.commuters) - 1)

    def test_set_seat_threat_sets_seat_threat_prop(self):
        set_seat_threat(self.car, BASE_THREAT)
        threat = [t.get_threat() for t in self.car.get_seats()]
        expected = [0] * (len(self.standing) * 2 - 1)
        expected[0::2] = [d[0] * BASE_THREAT for d in self.standing]
        self.assertEqual(threat, expected)

    def test_set_seat_exposure_sets_seat_exposure_prop(self):
        set_seat_threat(self.car, BASE_THREAT)  # depends on another method
        set_seat_exposure(self.car)
        exposure = [s.get_exposure() for s in self.car.get_seats()]
        expected = [0] * (len(self.standing) * 2 - 1)
        commuters = [i for i, d in enumerate(self.standing)]
        commuters.pop()
        expected[1::2] = [(self.commuters[c][0] + self.commuters[c+1][0]) *
                          BASE_THREAT for c in commuters]
        self.assertEqual(exposure, expected)

    def test_seat_commuters_appends_to_seat_seats_prop(self):
        """
        This test is a bit weak because (1) it only tests a situation where
        there are no vacant seats after seat_commuters() is run and (2) it does
        not have a programmatic way of constructing an expected. Include these
        things when completing this test.
        """
        set_seat_threat(self.car, BASE_THREAT)  # depends on another method
        set_seat_exposure(self.car)  # depends on another method
        print([c.get_commuter().get_duration() for c in self.car.get_seats()
               if c.get_commuter()])
        seat_commuters(self.car)
        print([c.get_commuter().get_duration() for c in self.car.get_seats()])
        pass
