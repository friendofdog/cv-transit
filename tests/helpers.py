from cvtransit.models.commuter import Commuter


def make_dummy_commuter(d=5, m=0):
    commuter = Commuter(d, m)
    return commuter
