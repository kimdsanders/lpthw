#cars
cars = 100
#space in a car
space_in_a_car = 4.0
#number of drivers
drivers = 30
#number of passengers
passengers = 90
#number of cars not driven (number of cars minus number of drivers)
cars_not_driven = cars - drivers
#number of cars driven 
cars_driven = drivers
#number of carpool capacity (cars driven multiplied by the space in a car)
carpool_capacity = cars_driven * space_in_a_car
# 
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"

# Study Drills Exercise 4
# ------------------------
# The error is in line 7 (now line 10): carpool_capacity , not car_pool_capacity was defined. There is an extra underscore character.

# 1. If just 4 is used the answers stay the same.  I think 4.0 is necessary in case you need to divde up the space in the car.

# 2-6 Done!


