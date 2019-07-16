import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

filename = 'new_york_city.csv'
df = pd.read_csv(filename)

print(df.head())