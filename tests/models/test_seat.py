from cvtransit.models.seat import Seat  # type: ignore
import unittest


class TestSeat(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSeat, self).__init__(*args, **kwargs)
        self.seat = Seat()

    def test_set_exposure_sets_adjacent_prop(self):
        adjecent = [2, 5]
        self.seat.set_exposure(adjecent)
        self.assertEqual(self.seat.get_exposure(), sum(adjecent))

    def test_set_exposure_takes_list_length_one_or_two(self):
        too_many = [1, 2, 3]
        with self.assertRaises(ValueError) as err:
            self.seat.set_exposure(too_many)

        self.assertEqual(
            str(err.exception),
            f"Expected length 1 or 2, got {len(too_many)}")

    def test_set_threat_sets_threat_prop(self):
        time = 15
        base = 100
        self.seat.set_threat(time, base)
        self.assertEqual(self.seat.get_threat(), time * base)
