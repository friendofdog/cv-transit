from cvtransit.models.row import Row


def initialise_row(seat_count):
    row = Row(seat_count)
    row.set_occupancy()
    return row


def app(**config):
    initialise_row(config['seat_count'])
