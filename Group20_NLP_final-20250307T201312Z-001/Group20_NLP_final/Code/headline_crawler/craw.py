import pandas as pd
from readability.readability import Document
import scrapy
PATH_TO_DATA = 'AggregateHeadlines - Sheet1.csv'
df = pd.read_csv(PATH_TO_DATA)
df = df.drop('Unnamed: 0.1', axis=1)
df = df.drop('Unnamed: 0', axis=1)
df = df.drop('US-Economy-related?', axis=1)
df = df.drop('emotion', axis=1)
df = df.drop('headline', axis=1)
df = df.drop('Unnamed: 6', axis=1)
df = df.drop('Unnamed: 7', axis=1)
df = df.drop('Unnamed: 8', axis=1)
df = df.drop('Unnamed: 9', axis=1)
df = df.drop('Unnamed: 10', axis=1)
df = df.drop('Unnamed: 11', axis=1)
df = df.drop('Unnamed: 12', axis=1)
df = df.drop('Unnamed: 13', axis=1)
df = df.url.tolist()


class HeadlineSpider(scrapy.Spider):
    name = 'headline crawl'
    start_urls = df

    def parse(self, response):
        doc = Document(response.text)
        yield {
            'short_title': doc.short_title(),
            'full_title': doc.title(),
            'url': response.url
        }
