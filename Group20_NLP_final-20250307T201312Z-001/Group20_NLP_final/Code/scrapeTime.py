import pandas as pd
import os
import re
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import nltk


def get_presponse(url, tag):
    try:
        response=urlopen(url)
        soup=BeautifulSoup(response.read(),"lxml")
        result=soup.find_all(tag)
        data=list()
        for h1 in result:
            if h1:
                if h1.text:
                    row=dict()
                    row['title']=h1.text
                    data.append(row)
        
        print(f'Scraped ...{url[len(url)-20:len(url)]}, data={data}')
        return data
    except:
        print(f'Exception on {url[len(url)-20:len(url)]}')

#OUTPUT_FILE = 'samplemod40(inter-annot)Time.csv'
OUTPUT_FILE = '1MSampleEconomicTime.csv'
economic = pd.read_csv('1MSampleEconomic.csv')

urls = pd.DataFrame()
urls['url'] = economic['url']

urls = urls.applymap(lambda x: get_presponse(x, "time"))
economic['time'] = urls['url']
economic.to_csv(OUTPUT_FILE)