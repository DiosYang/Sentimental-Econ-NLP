import time
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

url = 'https://www.wsj.com/search/term.html?KEYWORDS=cybersecurity&min-date=2018/04/01&max-date=2019/03/31' \
  '&isAdvanced=true&daysback=90d&andor=AND&sort=date-desc&source=wsjarticle,wsjpro&page={}'

pages = 32

for page in range(1, pages+1):
    res = requests.get(url.format(page))
    soup = BeautifulSoup(res.text,"lxml")

    for item in soup.find_all("a",{"class":"headline-image"},href=True):
        _href = item.get("href")
        try:
            resp = requests.get(_href)
        except Exception as e:
            try:
                resp = requests.get("https://www.wsj.com"+_href)
            except Exception as e:
                continue

        sauce = BeautifulSoup(resp.text,"lxml")
        dateTag = sauce.find("time",{"class":"timestamp article__timestamp flexbox__flex--1"})
        tag = sauce.find("li",{"class":"article-breadCrumb"})
        titleTag = sauce.find("h1",{"class":"wsj-article-headline"})
        contentTag = sauce.find("div",{"class":"wsj-snippet-body"})

        date = None
        tagName = None
        title = None
        content = None

        if isinstance(dateTag,Tag):
            date = dateTag.get_text().strip()

        if isinstance(tag,Tag):
            tagName = tag.get_text().strip()

        if isinstance(titleTag,Tag):
            title = titleTag.get_text().strip()

        if isinstance(contentTag,Tag):
            content = contentTag.get_text().strip()

        print(f'{date}\n {tagName}\n {title}\n {content}\n')
        time.sleep(3)