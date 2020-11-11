import time
from cvtransit.models.car import Car
from cvtransit.cycle import (
    decrement_commuter_duration,
    unseat_expired_commuters,
    set_seat_threat,
    set_seat_exposure,
    seat_commuters
)


BASE_THREAT = 100


def initialise_car(seat_count):
    car = Car(seat_count)
    car.set_seats()
    return car


def handle_cycle(car):
    decrement_commuter_duration(car)
    unseat_expired_commuters(car)
    set_seat_threat(car, BASE_THREAT)
    set_seat_exposure(car)
    seat_commuters(car, BASE_THREAT)


def app(**config):
    car = initialise_car(int(config['seat_count']))

    while True:
        handle_cycle(car)
        time.sleep(1)
