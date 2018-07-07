import numpy as np
import pandas as pd
import pickle

# After saving the 6 datafiles as CSV UTF-8 in ExceL

files = ['airports', 'events_US', 'fares', 'flight_traffic', 'stock_prices', 'weather']

for file in files:
    file_np = pd.read_csv(file + '.csv').values
    with open(file + '.pkl', 'wb') as f:
        pickle.dump(file_np, f)