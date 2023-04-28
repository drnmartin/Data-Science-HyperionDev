# TASK 14 COMPULSORY TASK HOLIDAY COST CALCULATOR

# (1) Using functions to calculate the costs of the various elements of the holiday


FLIGHT_PRICES = {
    "madrid": 250.0,
    "lisbon": 285.0,
    "berlin": 478.0
}


def hotel_cost(num_nights):
    return float(num_nights) * 220.00


def plane_cost(city):
    return FLIGHT_PRICES[city.lower()]


def car_rental(rental_days):
    return float(rental_days) * 35.00


def holiday_cost(hotel_cost, car_rental, plane_cost):
    return hotel_cost(num_nights) + car_rental(rental_days) + plane_cost(city_flight)

# (2) Collecting user inputs including validation checks.

border = "-" * 80
print(border)
print("\nWelcome to the holiday cost calculator.")

while True:
    city_flight = input("\nPlease enter the name of the city you will be flying to (Madrid/Lisbon/Berlin): ")    
    if city_flight.lower() in ("madrid", "lisbon", "berlin"):
        break
    else: 
        print("\nThat is not a valid entry. Please try again.")   

while True:
    try:
        num_nights = int(input("\nPlease enter the number of nights you will be staying at a hotel: "))
        if num_nights < 0:
            raise ValueError
        break
    except ValueError:
        print("\nThat is not a valid number. Please try again.") 

while True:
    try:
        rental_days = int(input("\nPlease enter the number of days that you will be hiring a car for: "))
        if rental_days < 0:
            raise ValueError
        break
    except ValueError:
        print("\nThat is not a valid number. Please try again.") 

print(border)

# (3) Print out the information for the user.

print(f"The total cost of the hotel is: £ {hotel_cost(num_nights):.2f}")
print(f"The total cost of the car rental is: £ {car_rental(rental_days):.2f}")
print(f"The cost of the flight is: £ {plane_cost(city_flight):.2f}")
print(f"\nTHE TOTAL COST OF THE HOLIDAY IS: £ {holiday_cost(hotel_cost, car_rental, plane_cost):.2f}")
print(border)
