# Bus/Train Ticket Booking System
# Language: Python 3
# Concepts: Lists, Dictionaries, Functions, Seat Management

# Initialize seats list (Seats 1 to 10)
seats = list(range(1, 11))

# Initialize passenger details dictionary (Mapping seat number -> passenger name)
passengers = {}

FARE_PER_SEAT = 500


def get_seats_left():
    """Returns the number of unbooked seats left."""
    return len(seats) - len(passengers)


def view_seats():
    """View current seat status, available seats, and booked seats."""
    print("\n--- Seat Status ---")
    available_seats = [s for s in seats if s not in passengers]
    booked_seats = [s for s in seats if s in passengers]

    if booked_seats:
        booked_info = ", ".join([f"{s} ({passengers[s]})" for s in booked_seats])
        print(f"Booked: {booked_info}")
    else:
        print("Booked: None")

    print(f"Available: {', '.join(map(str, available_seats))}")
    print(f"Seats left: {get_seats_left()}")


def book_seat():
    """Book a seat for a passenger with validation."""
    if get_seats_left() == 0:
        print("\nBus is now full. No seats available.")
        return

    try:
        seat_num = int(input("Enter seat number to book (1-10): "))
    except ValueError:
        print("Invalid input. Please enter a valid integer between 1 and 10.")
        return

    # Validate seat number range
    if seat_num not in seats:
        print(f"Invalid seat. Choose a seat from {seats[0]} to {seats[-1]}.")
        return

    # Check if already booked
    if seat_num in passengers:
        print(f"Seat {seat_num} is already booked.")
        return

    passenger_name = input("Enter passenger name: ").strip()
    if not passenger_name:
        print("Passenger name cannot be empty.")
        return

    # Confirm booking
    passengers[seat_num] = passenger_name
    print(f"Seat {seat_num} booked for {passenger_name}. Fare: {FARE_PER_SEAT}")
    print(f"Seats left: {get_seats_left()}")

    if get_seats_left() == 0:
        print("Bus is now full.")


def view_bookings():
    """View all current active bookings."""
    print("\n--- Current Bookings ---")
    if not passengers:
        print("No active bookings.")
    else:
        for seat_num in sorted(passengers.keys()):
            print(f"Seat {seat_num}: {passengers[seat_num]} (Fare Paid: {FARE_PER_SEAT})")
    print(f"Seats left: {get_seats_left()}")


def cancel_booking():
    """Cancel a booking and calculate 80% refund."""
    if not passengers:
        print("\nNo bookings to cancel.")
        return

    try:
        seat_num = int(input("Enter seat number to cancel: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    if seat_num not in passengers:
        print(f"Seat {seat_num} is not currently booked.")
        return

    # Calculate 80% refund
    refund = int(FARE_PER_SEAT * 0.80)
    passenger_name = passengers.pop(seat_num)
    
    print(f"Booking for seat {seat_num} cancelled. Refund: {refund}")
    print(f"Seats left: {get_seats_left()}")


def main():
    """Main console menu loop."""
    while True:
        print("\n==============================")
        print(" BUS TICKET BOOKING SYSTEM ")
        print("==============================")
        print("1. View seats")
        print("2. Book")
        print("3. Bookings")
        print("4. Cancel")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            view_seats()
        elif choice == '2':
            book_seat()
        elif choice == '3':
            view_bookings()
        elif choice == '4':
            cancel_booking()
        elif choice == '5':
            print("\nExiting system. Thank you!")
            break
        else:
            print("\nInvalid choice! Please select an option between 1 and 5.")


if __name__ == "__main__":
    main()