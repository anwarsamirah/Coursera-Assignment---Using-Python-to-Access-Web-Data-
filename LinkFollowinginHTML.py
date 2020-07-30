# The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags,
# scan for a tag that is in a particular position from the top and follow that link, repeat the process a number of times, 
# and report the last name you find.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
my_list=list()
url = input('Enter URL - ')

count=int(input("Enter count - "))
pos=int(input("Enter position - "))

i=1
while(i<=count):
   
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        my_list.append(tag.get("href",None))      
    url=my_list[pos-1]
    my_list=[]
    i=i+1
    print("Retrieving:",url)

