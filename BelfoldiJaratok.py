from Jaratok import Flight
class Domestic(Flight):
    def __init__(self, flight_number, destination, ticket_price):
        super().__init__(flight_number, destination, ticket_price)
    def info(self):
        return f"Domestic Flight: {self.flight_number} - {self.destination} - {self.ticket_price} Ft"
