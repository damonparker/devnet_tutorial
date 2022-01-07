#Import requests: this handles downloads of webpages
import requests
#Import beautifulsoup. Gives structure to html. Used for parsing
from bs4 import BeautifulSoup

#Set site variable to the requests call to a url
url = "https://www.nytimes.com/"
site = requests.get(url)

#Checking for errors. Use the raise_for_status method on the site object. This prints out the error if one is raise
try: 
    site.raise_for_status()
except Exception as ecx:
    print("There was a problem: %s' % (exc)")

soup = BeautifulSoup(site.text, "html.parser")

print(soup)

for head in soup.find_all('class_=e1lsht870'):
    print(head)

