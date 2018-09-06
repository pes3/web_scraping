import bs4, requests, random, csv
from datetime import datetime

def CISurfDesigns(boardesign):
    r = requests.get(boardesign)
    s = bs4.BeautifulSoup(r.text, 'html.parser') # second argument to avoid a warning
    boards = s.select(r'#surfboards > div > ul.grid-details > li:nth-of-type(2) > h2 > a') # had to adjust to nth-of-type to make css selector work
    randomboards = random.choice(boards)
    return randomboards.text

shape = CISurfDesigns('http://www.cisurfboards.com/surfboards/')

print('The randomly picked board you get to ride today from CI Surfborads is ' + shape + '!')

# store in an excel file what board you road each day, this will add to the excel file each time it is ran
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([shape, datetime.now()])
