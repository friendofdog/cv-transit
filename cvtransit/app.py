from cvtransit.models.car import Car


def initialise_car(seat_count):
    car = Car(seat_count)
    car.set_seats()
    return car


def app(**config):
    initialise_car(config['seat_count'])
