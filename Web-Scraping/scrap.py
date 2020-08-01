import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_link = links + links2
mega_subtext = subtext + subtext2


def sort_stories(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'])


def create_custom_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories(hn)


pprint.pprint(create_custom_hn(links=mega_link, subtext=mega_subtext))
