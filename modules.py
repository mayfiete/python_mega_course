
import time
import os
import sys

while True:
    if os.path.exists('fruit.txt'):
        with open('fruit.txt', 'r') as f:
            x = f.read()
            print(x)
    else: 
        print('File does not exist')
        modules = sys.builtin_module_names
    time.sleep(0.5)
