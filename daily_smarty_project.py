""" 
"How to Implement FizzBuzz in Python"
"""

""" 
Libraries to use:
- Requests (pip3 install requests)
-Inflection (pip3 install inflection)
-Beautifulsoup (pip3 install beautifulsoup4)
"""

import requests
from bs4 import Beautifulsoup



def title_maker(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            titles.append(url)

    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_formatter(link.get('href'))

    return titles


r = requests.get('https://www.dailysmarty.com/topics/python')
soup = Beautifulsoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_maker(links)

for title in titles:
    print(title.title())