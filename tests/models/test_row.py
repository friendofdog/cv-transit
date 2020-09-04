from cvtransit.models.row import Row  # type: ignore
import unittest


class TestRow(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestRow, self).__init__(*args, **kwargs)
        self.row = Row()

    def test_set_occupancy_creates_list(self):
        self.row.set_occupancy(6)
        self.assertEqual(type(self.row.get_occupancy()), list)
        self.assertEqual(len(self.row.get_occupancy()), 6)
