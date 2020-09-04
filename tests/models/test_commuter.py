from cvtransit.models.commuter import Commuter
import unittest

class TestCommuter(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCommuter, self).__init__(*args, **kwargs)
        self.commuter = Commuter()

    def test_set_mask_returns_bollean(self):
        self.commuter.set_mask()
        self.assertEqual(type(self.commuter.get_mask()), bool)

    def test_set_time_reduces_Commuter_time_by_one(self):
        initial = self.commuter.get_time()
        self.commuter.set_time()
        final = self.commuter.get_time()
        self.assertEqual(initial, final + 1)
