from cvtransit.models.car import Car
from cvtransit.models.commuter import Commuter


def make_dummy_car_obj(durations):
    count = len(durations) * 2
    car = Car(count)
    car.set_seats()
    for d in durations:
        car.add_commuter(Commuter(d, 0))
    return car


def make_dummy_commuter(d=5, m=0):
    commuter = Commuter(d, m)
    return commuter
