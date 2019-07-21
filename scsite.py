# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import pprint
import csv
from datetime import datetime

# Set the URL you want to webscrape from
url = 'https://www.timeanddate.com/weather/kenya/nairobi/historic?month=7&year=2019'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

script_tag = soup.findAll('script', attrs={'type': 'text/javascript'})
#print(script_tag)

cntr=0
for s in script_tag:
    cntr += 1
    #we are getting the fourth script tag that contains data in this example
    if cntr == 4:
        #strip to to remove the tags and replace to clean the first part of the data
        s = s.text.strip().replace('var data=','')
        weather=  s[0:s.index(";")]
        #print(weather)
        weather = json.loads(weather)
        #print (weather["detail"][3])
        #this gets all the weather data for the month of July in the detail element
        #for each day, theres 4 weather details ie 2 july has 3, 3 july - 3 ...etc. Only 1st of july has 3
        #with this in mind, to get 15th of July to 19th of July, we do
        date_start=14 #for the 15th
        date_index_start=(date_start*4)-1
        date_end=19 #for the 19th
        date_index_end=(date_end*4)-1
        for w in range(date_index_start,date_index_end):
            #print (weather["detail"][w])
            with open('index.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([weather["detail"][w], datetime.now()])

      
        
      
