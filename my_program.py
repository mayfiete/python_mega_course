

# tuples are immutable
monday_temperatures = [9.1, 8.8, 7.6]
monday_temperatures.append(32)

print(monday_temperatures[1])

print(monday_temperatures[0:2])

print(monday_temperatures[-1])

# provides positional access
print(monday_temperatures.index(8.8, 1))

monday_temperatures.clear() 

print(monday_temperatures)