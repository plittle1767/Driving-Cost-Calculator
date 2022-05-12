# this program will calculate the cost of gasoline for a truck and gas powered car. As well as kilowatt-hours for an
# electric car

# this function helps calculate the total cost of a trip using gas
def calculate_gas_vehicle_trip_cost(miles_driven, miles_per_gallon, price_per_gallon):
    gallons_gas: float = (miles_driven / miles_per_gallon)
    total_cost_of_trip: float = gallons_gas * price_per_gallon

    return total_cost_of_trip


# this function helps calculate the total cost of a trip using kilowatts/kilowatt-hours
def calculate_electric_vehicle_trip_cost(miles_driven, miles_per_kilowatt, price_per_kilowatt):
    kilowatt_hours: float = miles_driven / miles_per_kilowatt
    total_cost_of_trip: float = kilowatt_hours * price_per_kilowatt

    return total_cost_of_trip


# this function will print the statements we need that tell us how much money we will spend on gas/kilowatt-hours
# at a certain distance
def print_trip_cost_table(price_per_gallon, price_per_kilowatt, truck_mpg=15, gas_car_mpg=25, e_car_mpkwh=4):
    for count in range(50, 501, 50):
        print("For a trip of", count, "miles, the cost for the truck is $",
              round(calculate_gas_vehicle_trip_cost(count, truck_mpg, price_per_gallon)), "the cost for the car is $",
              round(calculate_gas_vehicle_trip_cost(count, gas_car_mpg, price_per_gallon)),
              "the cost for the electric car is $", round(calculate_electric_vehicle_trip_cost(count, e_car_mpkwh,
                                                                                               price_per_kilowatt)))

# This main function will be where we input the prices for gas and kilowatt-hours.
# We also call the print_trip_cost_table function to help calculate the cost at each distance
def main():
    gas_price = float(input("What is the price of gasoline? "))
    kwh_price = float(input("What is the price of electricity in dollars per kilowatt-hour? "))
    car_mpg = 25
    truck_mpg = 15
    electric_car_mpkwh = 4
    print_trip_cost_table(gas_price, kwh_price, truck_mpg, car_mpg, electric_car_mpkwh)


# Keep these lines. It helps Python run the program correctly.
if __name__ == "__main__":
    main()
