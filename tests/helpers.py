from cvtransit.models.car import Car
from cvtransit.models.commuter import Commuter


def make_dummy_car_obj(commuters):
    count = len(commuters) * 2
    car = Car(count)
    car.set_seats()
    for c in commuters:
        car.add_commuter(Commuter(c[0], c[1]))
    return car


def make_dummy_commuter(d=5, m=0):
    commuter = Commuter(d, m)
    return commuter
