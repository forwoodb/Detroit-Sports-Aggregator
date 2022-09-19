import requests 
from bs4 import BeautifulSoup
from pprint import pprint 
import time

start_time = time.time()
# url_byb = "https://www.blessyouboys.com/"
# url = "https://www.detroitbadboys.com/"

headlines = []
links = []
img_links = []
time_stamps = []
teams = []

# ########## SB Nation ##########
# sb_sites = [
#     ('tigers',"https://www.blessyouboys.com/",'c-six-up'),
#     ('lions',"https://www.prideofdetroit.com/",'c-six-up'),
#     ('red wings', "https://www.wingingitinmotown.com/",'c-six-up'),
#     ('pistons',"https://www.detroitbadboys.com/",'c-five-wide')
# ]

# for team, url, section in sb_sites:
#     res = requests.get(url)
#     html = res.content
#     soup = BeautifulSoup(html, 'html.parser')
#     articles = soup.find(class_=section).find_all(class_='c-entry-box--compact--article')

#     for ar in articles:
#         teams.append(team)
#         headline = ar.find('h2')
#         link = ar.find('h2').a
#         image = ar.find('img')
#         time_ = ar.find('time')

#         headlines.append(headline.text)
#         links.append(link['href'])
#         img_links.append(image['src'])
#         time_stamps.append(time_['datetime'])


########## Fansided ##########
# fansided = ('Tigers', "https://motorcitybengals.com/", 'template-1and3_noad')

fansided = "https://motorcitybengals.com/"

fs_headlines = []
# fs_links = []
# fs_img_links = []
# fs_time = []

# for url in fansided:
res = requests.get(fansided)
html = res.content
soup = BeautifulSoup(html, 'html.parser')
articles = soup.find(id="the-mosaic").find_all(class_='article')

for ar in articles:
    # teams.append(team)
    headline = ar.find('h2')
    link = ar.find('h2').a
    image = ar.find('a')
    time_ = ar.find('time')

    fs_headlines.append(headline.text)
    links.append(link['href'])
    img_links.append(image['style'].split("url(")[1][:-2])
    time_stamps.append(None)


article_list = list(zip(headlines, links, img_links,
                    time_stamps, teams))

for i in fs_headlines:
    print(i)
