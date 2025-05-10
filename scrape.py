import requests
from bs4 import BeautifulSoup

#gathers website html in text form as soup 
res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, "html.parser")
#collects each link that is a child of a titleline span
links = soup.select('.titleline > a')
#collects each subtext below the title/link
subtext = soup.select('.subtext')

def create_custom_hn(links, subtext):
  hacker_news_list = []
  for index, item in enumerate(links):
    title = links[index].getText()
    href = links[index].get('href', None)
    votesList = subtext[index].select('.score')
    if votesList:
      points = int(votesList[0].getText().replace(' points', ''))
      if points > 100:
        print(points)
        hacker_news_list.append({'Title: ': title, 'Link: ': href})
  
  return hacker_news_list

(create_custom_hn(links, subtext))