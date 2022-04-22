

user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
message = "Hello, {}!".format(user_input)
message = f"Hello, {user_input}!"
message = f"Hello, {user_input.title()}!"


print(message)