import pandas as pd

fatalities = pd.read_csv('data/fatalities-deduped.csv', dtype=str)

#fatalities['DUI'] = fatalities['Condition at Time of Crash'].apply(lambda x: True if x == 'Under the Influence of Medications/Drugs/Alcohol' else False)
#fatalities['Speeding'] = fatalities['Speeding Related'].apply(lambda x: True if x in ['Too Fast for Conditions', 'Exceeded Speed Limit', 'Racing'] else False)

#fatalities[(fatalities.Year >= '2013') & (fatalities.Year <= '2017')].groupby(['Town']).size().to_frame('AvFatalities').to_csv('data/av-fatalities-13-17.csv')

#fatalities.groupby(['Town', 'Year', 'Age', 'Gender', 'DUI', 'Speeding']).size().to_frame('Count').to_csv('data/tidy-by-town-by-year-by-age.csv', header=True)
fatalities.groupby(['Age', 'Gender']).size().unstack().to_csv('data/age-sex-chart.csv')
