import bs4
import requests
r = requests.get('http://www.cisurfboards.com/surfboards/')
s = bs4.BeautifulSoup(r.text, 'html.parser') # second argument to avoid a warning
boards = s.select(r'#surfboards > div > ul.grid-details > li:nth-of-type(2) > h2 > a') # had to change to 'nth - of type'

print(boards[1].text)

