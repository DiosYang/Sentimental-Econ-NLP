import pandas as pd
import re 
import numpy as np
import os
import sys

#OUTPUT = sys.argv[1]
#INPUT = sys.argv[0]
#INPUT = 
OUTPUT = 'final_4_datanodrop.csv'
"""
final = pd.read_excel(INPUT)

date = pd.DataFrame()
date['url_time'] = final['url_time']
dropped = final[final['has_date'] == 1]
dropped = dropped[dropped['our_sentiment'] != "FALSE"]

dropped.to_csv('50K/final_dropped.csv')
"""

dropped = pd.read_csv('50K/final_date_4nodrop.csv')
def get_avg_sentiment(df, yr, month = 0):

    avg_sentiment = np.mean(df['our_sentiment']) 
    avg_sentiment_sd = np.std(df['our_sentiment'])
    reuters = df[df['source'] == 'reuters']
    wsj = df[df['source'] == 'wsj']
    fox = df[df['source'] == 'fox']
    nbc = df[df['source'] == 'nbcnews']

    avg_sentiment_reuters = np.mean(reuters['our_sentiment'])
    #asr_sd = np.std(reuters['our_sentiment'])
    avg_sentiment_wsj = np.mean(wsj['our_sentiment'])
    #aswsj_sd = np.std()
    avg_sentiment_fox = np.mean(fox['our_sentiment'])
    avg_sentiment_nbc = np.mean(nbc['our_sentiment'])
    #asfox_sd = np.std()

    paper_sentiment_overall = np.mean(df['sentiment'])
    paper_sentiment_overall_sd = np.std(df['sentiment'])
    paper_sentiment_reuters = np.mean(reuters['sentiment'])
    paper_sentiment_wsj = np.mean(wsj['sentiment'])
    paper_sentiment_fox = np.mean(fox['sentiment'])
    paper_sentiment_nbc = np.mean(nbc['sentiment'])

    avg_top3 = np.mean([avg_sentiment_wsj, avg_sentiment_fox, avg_sentiment_reuters])
    paper_avg_top3 = np.mean([paper_sentiment_wsj, paper_sentiment_fox, paper_sentiment_reuters])

    sentiment_obs = {
            'yr': yr,
            'month': month,
            'time': yr + month/12,
            'overall': avg_sentiment,
            'overall_sd': avg_sentiment_sd,
            'top3': avg_top3,
            'top3+overall': (avg_top3 + avg_sentiment)/2,
            'reuters': avg_sentiment_reuters,
            'wsj': avg_sentiment_wsj,
            'fox': avg_sentiment_fox,
            'nbc': avg_sentiment_nbc,
            'paper_overall': paper_sentiment_overall,
            'paper_overall_sd': paper_sentiment_overall_sd,
            'paper_top3': paper_avg_top3,
            'paper_top3+overall': (paper_sentiment_overall + paper_avg_top3)/2,
            'paper_reuters': paper_sentiment_reuters,
            'paper_wsj': paper_sentiment_wsj,
            'paper_fox': paper_sentiment_fox,
            'paper_nbc': paper_sentiment_nbc
        }
    
    return sentiment_obs


sentiment_monthly = pd.DataFrame()
sentiment_yrly = pd.DataFrame()
for yr in range(2000,2020):
    yr_subset = dropped[dropped['yr'] == yr]
    qrtr = 0
    for month in range(1,13):
        if month % 3 == 0 and month != 12:
            quarter_subset = yr_subset[yr_subset['month'] < month+4]
            quarter_subset = quarter_subset[quarter_subset['month'] >= month]
            sentiment_obs = get_avg_sentiment(month_subset, yr, month)

            sentiment_obs = pd.DataFrame.from_dict(sentiment_obs, orient='index')
            sentiment_obs = pd.DataFrame.transpose(sentiment_obs)
            sentiment_quarterly = pd.concat([sentiment_monthly, sentiment_obs])

        month_subset = yr_subset[yr_subset['month'] == month]
        sentiment_obs = get_avg_sentiment(month_subset, yr, month)

        sentiment_obs = pd.DataFrame.from_dict(sentiment_obs, orient='index')
        sentiment_obs = pd.DataFrame.transpose(sentiment_obs)
        sentiment_monthly = pd.concat([sentiment_monthly, sentiment_obs])

        print(f'Computed sentiment for {month}/{yr}')

    year_obs = get_avg_sentiment(yr_subset, yr, month)

    year_obs = pd.DataFrame.from_dict(year_obs, orient='index')
    year_obs = pd.DataFrame.transpose(year_obs)
    sentiment_yrly = pd.concat([sentiment_yrly, year_obs])

sentiment_yrly.to_csv(f'Yearly{OUTPUT}')
sentiment_monthly.to_csv(f'Monthly{OUTPUT}')
sentiment_quarterly.to_csv(f'Quarterly{OUTPUT}')



        
    