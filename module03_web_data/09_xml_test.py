import urllib.request, urllib.response, urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = "http://py4e-data.dr-chuck.net/comments_42.xml"
url = "http://py4e-data.dr-chuck.net/comments_1957500.xml"
xml = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(xml)
lst = tree.findall("comments/comment")

# for n in lst:
#   print("name", n.find("name").text)
#   print("count", n.find("count").text)

sum =  sum(int(n.find("count").text) for n in lst)
print(sum)