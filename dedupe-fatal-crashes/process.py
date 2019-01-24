###
# Python script to remove duplicate crashes and calculate number of fatal crashes
# per town per year. We assume that duplicate crashes are the ones occuring
# on the same day at the same time in the same town.
#
# Author: Ilya Ilyankou <ilyankou@gmail.com>
# Date: January 24, 2019
###

import pandas as pd

crashes = pd.read_csv('data/Fatal Crashes & Persons 15-19 - Fatal Crashes.csv', dtype=str)
persons = pd.read_csv('data/Fatal Crashes & Persons 15-19 - Fatal Persons.csv', dtype=str)

duplicate_crashes_size = crashes.groupby(['Town Name', 'Date Of Crash', 'Time of Crash']).size()

repeating_keys = []
for index, item in duplicate_crashes_size.iteritems():
    if item > 1:
        repeating_keys.append(index)

duplicate_crashes = crashes.set_index(['Town Name', 'Date Of Crash', 'Time of Crash'])

ignore_crash_ids = []
for index in repeating_keys:
    mini_list = duplicate_crashes.loc[index].CrashId.values.tolist()
    mini_list.pop()
    ignore_crash_ids = ignore_crash_ids + mini_list

# Removing duplicate crash IDs from Persons dataframe
persons = persons[~persons.CrashId.isin(ignore_crash_ids)]

# In Persons dataframe, create Town and Year columns
persons['Town'] = persons['CrashId'].apply(lambda x: crashes[crashes.CrashId == x]['Town Name'].values[0])
persons['Year'] = persons['CrashId'].apply(lambda x: int(crashes[crashes.CrashId == x]['Date Of Crash'].values[0].split('-')[0]))
persons = persons[ (persons.Year >= 2015) & (persons.Year <= 2018) ]

# Calculate number of fatalities per town per year
fatalities = persons.groupby(['Town', 'Year']).size()
fatalities.to_csv('fatalities.csv', header=['Fatalities'])
