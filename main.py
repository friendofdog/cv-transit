from cvtransit.app import app


def main():
    duration = input('Enter time of commute in seconds: ')
    nomask = input('Enter chance of no mask (1-10): ')
    seat_count = input('Enter seat count: ')
    app(
        duration=duration,
        nomask=nomask,
        seat_count=seat_count
    )

if __name__ == "__main__":
    main()
