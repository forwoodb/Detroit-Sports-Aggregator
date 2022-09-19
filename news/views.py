from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import date


########## SB Nation ##########

sb_sites = [
    ('Tigers', "https://www.blessyouboys.com/", 'c-six-up'),
    ('Lions', "https://www.prideofdetroit.com/", 'c-six-up'),
    ('Red Wings', "https://www.wingingitinmotown.com/", 'c-six-up'),
    ('Pistons', "https://www.detroitbadboys.com/", 'c-five-wide')
]

headlines = []
links = []
img_links = []
time_stamps = []
teams = []

for team, url, section in sb_sites:
    res = requests.get(url)
    html = res.content
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find(class_=section).find_all(
        class_='c-entry-box--compact--article')

    for ar in articles:
        teams.append(team)
        headline = ar.find('h2')
        link = ar.find('h2').a
        image = ar.find('img')
        time_ = ar.find('time')

        headlines.append(headline.text)
        links.append(link['href'])
        img_links.append(image['src'])
        time_stamps.append(time_['datetime'])


########## Fansided ##########

fansided = [
    ('Tigers', "https://motorcitybengals.com/", "the-mosaic"),
    ('Lions', "https://sidelionreport.com/", "the-mosaic"),
    ('Pistons', "https://pistonpowered.com/", "the-mosaic"),
    ('Red Wings', "https://octopusthrower.com/", "the-mosaic"),
]

for team, url, section in fansided:

    res = requests.get(url)
    html = res.content
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find(id=section).find_all(class_='article')

    for ar in articles:
        teams.append(team)
        headline = ar.find('h2')
        link = ar.find('h2').a
        image = ar.find('a')
        # time_ = ar.find('time')

        headlines.append(headline.text)
        links.append(link['href'])
        img_links.append(image['style'].split("url(")[1][:-2])
        time_stamps.append(str(date.today()))


########## Bleacher Report ##########

article_list = list(zip(headlines, links, img_links,
                    time_stamps, teams))
articles_order = sorted(article_list, key=lambda article: article[3], reverse=True)

def index(request):
    template = 'home.html'
    context = {'article_list': articles_order}
    return render(request, template, context)

def tigers(request):
    template = 'tigers.html'
    context = {'article_list': articles_order}
    return render(request, template, context)

def pistons(request):
    template = 'pistons.html'
    context = {'article_list': articles_order}
    return render(request, template, context)

def redwings(request):
    template = 'redwings.html'
    context = {'article_list': articles_order}
    return render(request, template, context)

def lions(request):
    template = 'lions.html'
    context = {'article_list': articles_order}
    return render(request, template, context)
