
import pandas as pd
import os
import time

x = 0

while x < 3:
    if os.path.exists('data.csv'):
        print('File exists')
        data = pd.read_csv('data.csv')
        print(data.mean())
        x = x+1
    else:
        print('File does not exist')
    time.sleep(1)
