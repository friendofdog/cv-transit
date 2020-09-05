from cvtransit.app import initialise_row
import unittest


class TestApp(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestApp, self).__init__(*args, **kwargs)

    def test_initialise_app_creates_list_of_seats(self):
        initialised_app = initialise_row(5)
        seats = initialised_app.get_occupancy()
        self.assertEqual(len(seats), 5)
