# Exercise 4: Tuple Basics

coordinates = (10, 20, 30)

print("First element:", coordinates[0])
print("Last element:", coordinates[2])

# Tuples are immutable - this will give error
# coordinates[1] = 25   # TypeError

# Convert tuple to list, modify, then back to tuple
coordinates_list = list(coordinates)
coordinates_list[1] = 25

coordinates = tuple(coordinates_list)
print("Modified tuple:", coordinates)