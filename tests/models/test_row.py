from cvtransit.models.row import Row  # type: ignore
import unittest


class TestRow(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestRow, self).__init__(*args, **kwargs)
        self.seat_count = 6
        self.row = Row(self.seat_count)

    def test_set_occupancy_creates_list(self):
        self.row.set_occupancy()
        self.assertEqual(type(self.row.get_occupancy()), list)
        self.assertEqual(len(self.row.get_occupancy()), self.seat_count)
