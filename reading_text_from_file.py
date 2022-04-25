

my_file = open("fruits.txt", "r")  # open file in read mode

# print(my_file.read()) # read the file
content = my_file.read()
print(content)

# move the cursor to the beginning of the file
my_file.seek(0)

my_file.close()  # close the file


with open ("fruits.txt", "r") as my_file:
    content = my_file.read()
    
print(content)