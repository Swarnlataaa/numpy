import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load COVID-19 data from a CSV file
data = pd.read_csv('covid_data.csv')

# Extract daily new cases from the data
confirmed_cases = data['Confirmed'].values
new_cases = np.diff(confirmed_cases, prepend=0)  # Calculate daily new cases

# Calculate a 7-day rolling average of new cases
rolling_avg = np.convolve(new_cases, np.ones(7)/7, mode='valid')

# Basic statistics
total_cases = confirmed_cases[-1]
max_daily_cases = np.max(new_cases)
avg_daily_cases = np.mean(new_cases)
median_daily_cases =
