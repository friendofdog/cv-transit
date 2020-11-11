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


class App(object):

    def __init__(self, **config):
        self.car = self._initialise_car(config["seat_count"])
        self.duration = config["duration"]
        self.running = False

    def _initialise_car(self, seat_count):
        car = Car(seat_count)
        car.set_seats()
        return car

    def _handle_cycle(self):
        decrement_commuter_duration(self.car)
        unseat_expired_commuters(self.car)
        set_seat_threat(self.car, BASE_THREAT)
        set_seat_exposure(self.car)
        seat_commuters(self.car, BASE_THREAT)

    def start(self):
        self.running = True

        while self.running:
            self.duration -= 1
            self._handle_cycle()
            time.sleep(1)
            if self.duration == 0:
                self.running = False


if __name__ == "__main__":
    get_duration = int(input('Enter time of commute in seconds: '))
    get_seat_count = int(input('Enter seat count: '))
    app = App(
        duration=get_duration,
        seat_count=get_seat_count
    )
    app.start()
