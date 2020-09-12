def decrement_commuter_duration(car):
    commuters = car.get_commuters()
    for commuter in commuters:
        commuter.decrement_duration()


def unseat_expired_commuters(car):
    commuters = car.get_commuters()
    for commuter in commuters:
        duration = commuter.get_duration()
        if duration < 1:
            car.remove_commuter(commuter)


def set_seat_threat(car):
    pass


def set_seat_exposure(car):
    pass


def seat_commuters():
    pass
