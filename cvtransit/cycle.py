BASE_THREAT = 100  # temporary, move to config file


def _find_lowest_exposure(seats):
    vacant = [s for s in seats if not s.get_commuter()]
    if not vacant:
        return None
    lowest = min([v.get_exposure() for v in vacant])
    return [s for s in vacant if s.get_exposure() == lowest]


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


def set_seat_threat(car, base_threat):
    for s in car.get_seats():
        if s.get_commuter():
            s.set_threat(s.get_commuter().get_duration(), base_threat)


def set_seat_exposure(car):
    seats = car.get_seats()
    for i, s in enumerate(seats):
        adjecent = [s.get_threat() for s in [
            seats[i-1] if i > 0 else None,
            seats[i+1] if i < len(seats) - 1 else None
        ] if s]
        s.set_exposure(adjecent)


def seat_commuters(car):
    standing = [c for c in car.get_commuters()
                if c not in [s.get_commuter() for s in car.get_seats()]]
    standing = sorted(standing, key=lambda s: s.get_duration(), reverse=True)
    for s in standing:
        lowest = _find_lowest_exposure(car.get_seats())
        if lowest:
            """
            This is a bit weak, just grabs the first seat in lowest should two
            seats have equally lowest exposure. Change this to more accurately
            identify the lowest exposed seat.
            """
            lowest[0].set_commuter(s)
            lowest[0].set_threat(s.get_duration(), BASE_THREAT)
        else:
            continue
