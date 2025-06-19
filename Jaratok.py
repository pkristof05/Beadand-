from abc import ABC, abstractmethod
class Flight(ABC):
    def __init__(self, flight_number, destination, ticket_price):
        self.flight_number = flight_number
        self.destination = destination
        self.ticket_price = ticket_price
    @abstractmethod
    def info(self):
        pass