from datetime import date
from operator import attrgetter


class User:
    def __init__(self, can_see_reservations, name):
        self.can_see_reservations = can_see_reservations
        self.name = name


class Reservation:
    def __init__(self, _date, _total_price):
        self.date = _date
        self.total_price = _total_price


class ReservationService:

    def highest_total_price_reservations(self, date_from, date_to, reservations_count):
        # normally it would be read from database/external service
        reservations = [
            Reservation(date(2014, 5, 15), 100),
            Reservation(date(2017, 5, 15), 10),
            Reservation(date(2017, 1, 15), 50)
        ]
        filtered_reservations = filter(lambda r: date_from <= r.date <= date_to, reservations)
        return sorted(filtered_reservations, key=attrgetter('total_price'))[:reservations_count]


# Consumer Service
class StatsService:
    def __init__(self, reservation_service):
        self.reservation_service = reservation_service

    def year_top_100_reservations_average_total_price(self, year):
        reservations = self.reservation_service.highest_total_price_reservations(
            date(year, 1, 1),
            date(year, 12, 31),
            1
        )
        if len(reservations) > 0:
            total = sum(r.total_price for r in reservations)
            return total / len(reservations)
        else:
            return 0


class Proxy:
    def __init__(self, current_user, reservation_service):
        self.current_user = current_user
        self.reservation_service = reservation_service

    def highest_total_price_reservations(self, date_from, date_to, reservations_count):
        if self.current_user.can_see_reservations:
            return self.reservation_service.highest_total_price_reservations(date_from, date_to, reservations_count)
        return []


def test(user, year):
    reservation_service = Proxy(user, ReservationService())
    stats_service = StatsService(reservation_service)
    average_price = stats_service.year_top_100_reservations_average_total_price(year)
    print(F"{user.name} will see: {average_price}")


if __name__ == '__main__':
    test(User(True, "Admin"), 2017)
    test(User(False, "Guest"), 2017)
