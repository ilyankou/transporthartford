import pandas as pd
import numpy as np

crashes_all = pd.read_csv('data/Crash Data - All roads - All.csv', index_col='Town').sort_values(by=['Town'])
population = pd.read_csv('data/ACS2017 5-year estimates - Population.csv', index_col='Town').sort_values(by=['Town'])

major_towns = [
    'Hartford',
    'New Haven',
    'Waterbury',
    'Bridgeport',
    'Stamford'
]

hartford_ring = [
    'Bloomfield',
    'Windsor',
    'South Windsor',
    'East Hartford',
    'Glastonbury',
    'Wethersfield',
    'West Hartford'
]

# For each year, calculate crash rate per 1,000 citizens
for i in [2015, 2016, 2017, 2018]:
    year = str(i)
    crashes_all[year + '_rate'] = crashes_all[year] / population['ACS2017'] * 1000
    crashes_all[year + '_rate'] = crashes_all[year + '_rate'].round(1)

crashes_all[crashes_all.index.isin(major_towns)].to_csv('output.csv')
