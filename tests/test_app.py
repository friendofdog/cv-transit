from cvtransit.app import initialise_car
import unittest


class TestApp(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestApp, self).__init__(*args, **kwargs)

    def test_initialise_app_creates_list_of_seats(self):
        initialised_app = initialise_car(5)
        initialised_app.get_seats()
