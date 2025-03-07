import pandas as pd
import json
import os

outletAbbreviationToFullName = {
    'alternet': "Alternet",
    'democracynow': "Democracy Now",
    'db': "Daily Beast",
    'hp': "Huffington Post",
    'jacobin': "Jacobin",
    'theintercept': "The Intercept",
    'motherjones': "Mother Jones",
    'thenewyorker': "The New Yorker",
    'thenation': "The Nation",
    'slate': "Slate",
    'vox': "Vox",
    
    'cnn': "CNN",
    'nyt': "New York Times",
    'abcnews': "ABC News",
    'theatlantic': "The Atlantic",
    'buzzfeed': "Buzzfeed",
    'cbs': "CBS News",
    'economist': "The Economist",
    'guardian': "The Guardian",
    'nbcnews': "NBC News",
    'politico': "POLITICO",
    'timemagazine': "TIME",
    'wp': "Washington Post",
    'npr': "NPR",
    
    'ap': "Associated Press",
    'bbc': "BBC",
    'bloomberg': "Bloomberg",
    'csm': "Christian Science Monitor",
    'reuters': "REUTERS",
    'thehill': "The Hill",
    'usatoday': "USA Today",
    
    'wsj': "Wall Street Journal",
    'reason': "Reason",
    'we': "Washington Examiner",    
    'wt': "Washington Times",
    'fox': "Fox News",
    
    'americanspectator': "American Spectator",
    'bre': "Breitbart",
    'theblaze': "The Blaze",
    'cbn': "Christian Broadcasting Network",
    'dailycaller': "The Daily Caller",
    'dailymail': "The Daily Mail",
    'dailywire': 'The Daily Wire',
    'thefederalist': "The Federalist",
    'nationalreview': "National Review",
    'nyp': "New York Post",
    'newsmax': "Newsmax",    
}

YRCAP = 1000000#maximum number of articles allowed for one news source for one year
OUTPUT_FILE = 'finalDroppedInfo'
os.makedirs(f'{OUTPUT_FILE}')

#economic = pd.read_csv('50K/final_dropped.csv')
#economic = pd.read_excel('50K/final_date_3_wwsj.xlsx')
economic = pd.read_csv('50K/final_dropped.csv')#file with data without dates or setniment scores dropped
sampled = pd.DataFrame()


obs_outlet_yr = ''
obs_outlet = ''
outlets = dict()
for outlet in outletAbbreviationToFullName.keys():
    date = dict()
    outlet_df = economic[economic['source'] == outlet]
    total_outlet_sample = 0


    for year in range(2000,2019):
        try:
            date[year] = outlet_df[outlet_df['yr'] == year]
            num_obs = len(date[year])

            if num_obs > YRCAP:
                date[year] = date[year].sample(YRCAP, random_state=1)

            sampled = pd.concat([sampled, date[year]])
            num_obs_sampled = len(date[year])
            total_outlet_sample += num_obs_sampled

            outlet_yr_str = f'{num_obs_sampled}, observations for, {outlet}, year, {year}\n'
            print(outlet_yr_str)
            obs_outlet_yr += outlet_yr_str

        except:
            print(f'Exception on {outlet}, year {year}')

    #num_obs_outlet = len(outlet_df)
    outlet_str = f'{total_outlet_sample}, observations for, {outlet}\n'
    print(outlet_str)
    obs_outlet += outlet_str
    
    outlets[outlet] = outlet_df
    outlets[f'{outlet}Date'] = date

sampled.to_csv(f'{OUTPUT_FILE}/{OUTPUT_FILE}.csv')

with open (f'{OUTPUT_FILE}/{OUTPUT_FILE}outletyrCnt.csv', 'w') as f:
    f.write(obs_outlet_yr)

with open (f'{OUTPUT_FILE}/{OUTPUT_FILE}outletCnt.csv', 'w') as f:
    f.write(obs_outlet)
