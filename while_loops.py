

a = 3

while a < 10:
    print(a)
    a += 1

username = ''

while username != 'admin':
    username = input("Username: ")


while True: 
    username = input("Username: ")
    if username == 'admin':
        break
    else: 
        print("Access denied")