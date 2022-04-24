

user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
message = "Hello, {}!".format(user_input)
message = f"Hello, {user_input}!"
message = f"Hello, {user_input.title()}!"

name = input("Enter your name: ")
surname = input("Enter your surname: ")

first_message = f"Hello, {name.title()} {surname.title()}!"
new_message = "Hello %s %s!" % (name, surname)


print(first_message)
print(new_message)
