import pandas as pd

fatalities = pd.read_csv('data/fatalities-deduped.csv', dtype=str)

fatalities['DUI'] = fatalities['Condition at Time of Crash'].apply(lambda x: True if x == 'Under the Influence of Medications/Drugs/Alcohol' else False)
fatalities['Speeding'] = fatalities['Speeding Related'].apply(lambda x: True if x in ['Too Fast for Conditions', 'Exceeded Speed Limit', 'Racing'] else False)

fatalities.groupby(['Town', 'Year', 'Age', 'Gender', 'DUI', 'Speeding']).size().to_frame('Count').to_csv('data/tidy-by-town-by-year-by-age.csv', header=True)
fatalities.groupby(['Age', 'Gender', 'Person Type', 'DUI', 'Speeding']).size().to_frame('Count').to_csv('data/tidy-by-age.csv')
