

temps = [0, 12, 34, -100] 

new_temps = [temp for temp in temps if temp > 0] 

new_temps = [temp /10 if temp > 0 else 0 for temp in temps]

print(new_temps)



