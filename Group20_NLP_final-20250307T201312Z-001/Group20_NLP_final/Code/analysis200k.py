import pandas as pd
import re 
import numpy as np
import os
import sys
import analysis

#OUTPUT = sys.argv[1]
#INPUT = sys.argv[0]
#INPUT = 
OUTPUT = 'final_4_data.csv'
"""
final = pd.read_excel(INPUT)

date = pd.DataFrame()
date['url_time'] = final['url_time']
dropped = final[final['has_date'] == 1]
dropped = dropped[dropped['our_sentiment'] != "FALSE"]

dropped.to_csv('50K/final_dropped.csv')
"""

dropped = pd.read_csv('/Users/marcetter/NLP/FinalProj/200KSample(Representative)/baseline_sentiment_output.csv')

sentiment_yrly = pd.DataFrame()
for yr in range(2000,2020):
    yr_subset = dropped[dropped['yr'] == yr]
    qrtr = 0

    print(f'Computed sentiment for {yr}')

    year_obs = analysis.get_avg_sentiment(yr_subset, yr)

    year_obs = pd.DataFrame.from_dict(year_obs, orient='index')
    year_obs = pd.DataFrame.transpose(year_obs)
    sentiment_yrly = pd.concat([sentiment_yrly, year_obs])

sentiment_yrly.to_csv(f'Yearly{OUTPUT}')



        
    