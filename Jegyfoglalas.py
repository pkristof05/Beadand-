class Ticket_reservation:
    def __init__(self, passenger_name, flight, date):
        self.passenger_name = passenger_name  
        self.flight = flight                  
        self.date = date                     
    def __str__(self):
        return f"{self.passenger_name} - {self.flight.flight_number} ({self.flight.destination}) - {self.date.strftime('%Y-%m-%d')}"
from datetime import datetime
class Handler:
    def __init__(self):
        self.reservations = []
    def add_reservation(self, reservation):
        if reservation.date < datetime.now():
            print("Érvénytelen dátum! Múltbeli foglalás nem lehetséges.")
            return False
        self.reservations.append(reservation)
        print(f"Foglalás sikeres. Ár: {reservation.flight.ticket_price} Ft")
        return True
    def cancel_reservation(self, passenger_name, flight_number):
        for reservation in self.reservations:
            if reservation.passenger_name == passenger_name and reservation.flight.flight_number == flight_number:
                self.reservations.remove(reservation)
                print("Foglalás törölve.")
                return True
        print("Nem található ilyen foglalás.")
        return False
    def list_reservations(self):
        if not self.reservations:
            print("Nincs aktív foglalás.")
        else:
            for reservation in self.reservations:
                print(reservation)
