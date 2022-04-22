

def weather_conditions(temperature):
    if temperature < 0:
        return "freezing"
    elif temperature < 10:
        return "cold"
    elif temperature < 20:
        return "mild"
    elif temperature < 30:
        return "warm"
    else:
        return "hot"


user_input = input("Enter a temperature: ")

print(weather_conditions(int(user_input)))
