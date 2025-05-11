import requests
from bs4 import BeautifulSoup
import pprint

#gathers website html in text form as soup 
res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")
#collects each link that is a child of a titleline span
links = soup.select('.titleline > a')
links2 = soup2.select('.titleline > a')
#collects each subtext below the title/link
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

#combines links and subtexts
mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hacker_news_list):
  return sorted(hacker_news_list, key= lambda k:k['Votes'], reverse = True)

#function that takes in:
# - list of links
# - list of subtexts directly underneath link/title
#creates empty array/list
#selects the specific title,href, and the span with '.score'
def create_custom_hn(links, subtext):
  hacker_news_list = []
  for index, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    votesList = subtext[index].select('.score')
    #if there are upvotes, strip off the texts, call it points, and
    #compare points to 100
    #if points > 100, add title,href,and votes to new list
    if votesList:
      points = int(votesList[0].getText().replace(' points', ''))
      if points > 99:
        hacker_news_list.append({'Title': title, 'Link': href , 'Votes': points})
  
  return sort_stories_by_votes(hacker_news_list)

#pprint is library to organize the unformatted data
pprint.pprint(create_custom_hn(mega_links, mega_subtext))