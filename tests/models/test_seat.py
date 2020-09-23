from cvtransit.models.seat import Seat  # type: ignore
from tests.helpers import make_dummy_commuter
import unittest


class TestSeat(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSeat, self).__init__(*args, **kwargs)
        self.seat = Seat()

    def test_set_exposure_sets_exposure_prop(self):
        adjecent = [2, 5]
        self.seat.set_exposure(adjecent)
        self.assertEqual(self.seat.get_exposure(), sum(adjecent))

    def test_set_threat_sets_threat_prop(self):
        time = 15
        base = 100
        self.seat.set_threat(time, base)
        self.assertEqual(self.seat.get_threat(), time * base)

    def test_set_seated_sets_commuter_prop(self):
        commuter = make_dummy_commuter()
        self.seat.set_commuter(commuter)
        self.assertEqual(self.seat.get_commuter(), commuter)
