from cvtransit.models.commuter import Commuter  # type: ignore
import unittest


class TestCommuter(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCommuter, self).__init__(*args, **kwargs)
        self.duration = 30
        self.commuter = Commuter(self.duration, 0.1)

    def test_set_mask_sets_prop_as_boolean(self):
        self.commuter.set_mask()
        self.assertEqual(type(self.commuter.get_mask()), bool)

    def test_set_duration_reduces_duration_by_one(self):
        self.commuter.set_duration()
        final = self.commuter.get_duration()
        self.assertEqual(self.duration - 1, final)
