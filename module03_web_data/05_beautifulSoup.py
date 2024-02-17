import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input("Enter -")
html = urllib.request.urlopen(url).read()
print("html",html)
soup = BeautifulSoup(html, 'html.parser')

# retrieve all the anchor tags

tags = soup('a')
for tag in tags:
  print(tag.get('href', None))


# Ignore SSL Certificate errors -----------------------------------

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url2 = input("Enter web -")
# html2 = urllib.request.urlopen(url2, context=ctx).read()
# soup2 = BeautifulSoup(html2, 'html.parser')

# tags = soup('a')
# for tag in tags:
#   print(tag.get('href', None))


