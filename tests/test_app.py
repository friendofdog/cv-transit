import unittest

from cvtransit.app import App
from cvtransit.models.car import Car
from unittest import mock


class TestApp(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestApp, self).__init__(*args, **kwargs)
        self.seat_count = 7
        self.duration = 20

    def test_initialise_car_creates_Car_object_with_seats(self):
        app = App(duration=self.duration, seat_count=self.seat_count)
        initialised_car = app.car
        seats = len(initialised_car.get_seats())
        self.assertIsInstance(initialised_car, Car)
        self.assertEqual(seats, self.seat_count)

    @mock.patch("cvtransit.app.time.sleep")
    @mock.patch("cvtransit.app.App._handle_cycle")
    def test_start_runs_until_running_false(self, mock_cycle, mock_sleep):
        app = App(duration=self.duration, seat_count=self.seat_count)
        app.start()
        self.assertTrue(mock_cycle.called)
        self.assertTrue(mock_sleep.called)
        self.assertEqual(app.running, False)
