

# write to a file
with open('fruit.txt', 'w') as f:
    f.write('apple\nbanana\ncherry\n')
# this will overwrite the file

# append to a file without overwriting
with open('fruit.txt', 'a') as f:
    f.write('\npear\n')

# read and write to a file
with open('fruit.txt', 'a+') as myfile:
    myfile.write('\norange')
    myfile.seek(0)
    content = myfile.read()

print(content)


with open("vegetables.txt", "a") as f:
    f.write("broccoli\n")
# this will look for existing file, and create it if not exists
