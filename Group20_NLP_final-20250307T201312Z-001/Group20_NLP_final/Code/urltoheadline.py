
import pandas as pd
import re
import nltk

final = pd.read_excel('50K/final_date_3_wwsj.xlsx')

wsj = final[final['source'] == 'wsj']
""""
wsj_url = pd.DataFrame()
wsj_url['headline_regex'] = wsj['url']

wsj_url = wsj_url.applymap(lambda x: re.split('/',x))
wsj_url = wsj_url.applymap(lambda x: x[4])
wsj_url = wsj_url.applymap(lambda x: re.sub('-', ' ', x))
wsj['headline_regex'] = wsj_url['headline_regex']
"""







nbc = final[final['source'] == 'nbcnews']

def get_element(list, i):
    try:
        return list[i]
    except:
        return ''
    
nbc_url = pd.DataFrame()
nbc_url['re'] = nbc['url']
nbc_url = nbc_url.applymap(lambda x: re.split('/',x))
nbc_url = nbc_url.applymap(lambda x: get_element(x, 5))
nbc_url = nbc_url.applymap(lambda x: re.sub('-', ' ', x))

nbc['headline_regex'] = nbc_url['re']
nbc.to_csv('50K/headlinesfromurl/nbcnews_head.csv')

print('finished')