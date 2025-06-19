class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []
    def add_flight(self, flight):
        self.flights.append(flight)
    def get_flight(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                return flight
        return None