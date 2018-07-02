import pandas as pd

coordinate = pd.read_csv('dataset_coordinates.csv',header=None, skiprows=1)
keylogger = pd.read_csv('dataset_keylogger.csv',header=None, skiprows=1)