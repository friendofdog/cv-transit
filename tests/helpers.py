from cvtransit.models.car import Car
from cvtransit.models.commuter import Commuter


def make_dummy_car_obj(commuters, standing):
    count = (len(commuters) + standing) * 2 - 1
    car = Car(count)
    car.set_seats()
    for c in commuters:
        car.add_commuter(Commuter(c[0], c[1]))
    return car


def make_dummy_commuter(d=5, m=0):
    commuter = Commuter(d, m)
    return commuter


def populate_dummy_car_seats(car, standing):
    for i, c in enumerate(car.get_commuters()[:standing]):
        seat = car.get_seats()[i * 2]
        seat.set_commuter(c)
