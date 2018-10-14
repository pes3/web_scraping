# run in cmd by going to path, pythonw and script  name
import datetime, threading, time
import bs4, requests, random, csv
from datetime import datetime

_SECOND = 1
_MINUTE = 60*_SECOND
_HOUR = 60*_MINUTE
_DAY = 24*_HOUR

def CISurfDesigns(boardesign):
    r = requests.get(boardesign)
    s = bs4.BeautifulSoup(r.text, 'html.parser') # second argument to avoid a warning
    boards = s.select(r'#surfboards > div > ul.grid-details > li:nth-of-type(2) > h2 > a') # had to adjust to nth-of-type to make css selector work
    randomboards = random.choice(boards)
    return randomboards.text

next_call = time.time()

def foo():
  
  global next_call # Use global next_call

  # Do some important stuff.


  shape = CISurfDesigns('http://www.cisurfboards.com/surfboards/')

  print('The randomly picked board you get to ride today from CI Surfborads is ' + shape + '!')

  try:
    # store in an excel file what board you road each day, this will add to the excel file each time it is ran
    with open('index.csv', 'a') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow([shape, datetime.now()])
    # End importantant stuff script
  except Exception as e:
    print("Something went wrong.")
    print(e)

  print(datetime.now()) 
  print("Doing important stuff...")
  
  next_call = next_call + (10*_SECOND)
  
  threading.Timer( next_call - time.time(), foo ).start() # Schedule it for (next_call - NOW) seconds!

foo()
