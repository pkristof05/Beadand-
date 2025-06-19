from datetime import datetime
from BelfoldiJaratok import Domestic
from KulfoldiJaratok import International
from Legitarsasag import Airline
from Jegyfoglalas import Ticket_reservation, Handler

def preload_data(airline, handler):
    f1 = Domestic("A001", "Budapest", 20000)
    f2 = Domestic("B001", "Debrecen", 25000)
    f3 = International("C001", "London", 50000)
    airline.add_flight(f1)
    airline.add_flight(f2)
    airline.add_flight(f3)
    handler.add_reservation(Ticket_reservation("Anna Kovacs", f1, datetime(2025, 6, 20)))
    handler.add_reservation(Ticket_reservation("Peter Nagy", f2, datetime(2025, 6, 25)))
    handler.add_reservation(Ticket_reservation("Laszlo Kiss", f3, datetime(2025, 7, 1)))
    handler.add_reservation(Ticket_reservation("Marta Szabo", f1, datetime(2025, 6, 21)))
    handler.add_reservation(Ticket_reservation("Eva Toth", f2, datetime(2025, 6, 22)))
    handler.add_reservation(Ticket_reservation("Gabor Horvath", f3, datetime(2025, 7, 3)))
def show_menu():
    print("\n=== Repülőjegy Foglalási Rendszer ===")
    print("1. Jegy foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("0. Kilépés")
def main():
    airline = Airline("AirPython")
    handler = Handler()
    preload_data(airline, handler)
    while True:
        show_menu()
        choice = input("Válassz egy lehetőséget: ")
        if choice == "1":
            name = input("Utas neve: ")
            flight_number = input("Járatszám: ")
            date_str = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                flight = airline.get_flight(flight_number)
                if not flight:
                    print("A járat nem található.")
                    continue
                reservation = Ticket_reservation(name, flight, date)
                handler.add_reservation(reservation)
            except ValueError:
                print("Hibás dátumformátum.")
        elif choice == "2":
            name = input("Utas neve: ")
            flight_number = input("Járatszám: ")
            handler.cancel_reservation(name, flight_number)
        elif choice == "3":
            handler.list_reservations()
        elif choice == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")
if __name__ == "__main__":
    main()