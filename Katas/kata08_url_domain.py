"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

# url_= "http://github.com/carbonfive/raygun"
url_ = "http://www.zombie-bites.com"  
# url_ = "https://www.cnet.com"   
# url_ = "www.xakep.ru"   
# url_ = "https://hyphen-site.org"   
# url_ = "icann.org"   

# def domain_name(url):
#   if url.startswith("https://www."):
#     txt = url.removeprefix("https://www.")
#   elif url.startswith("http://www."):
#     txt = url.removeprefix("http://www.")
#   elif url.startswith("https://"):
#     txt = url.removeprefix("https://")
#   elif url.startswith("http://"):
#     txt = url.removeprefix("http://")
#   elif url.startswith("www."):
#     txt = url.removeprefix("www.")
#   else:
#     txt = url
  
#   domain = txt.split(".")
#   print(domain[0])
#   return domain[0]

# domain_name(url_)

# --- Solution 01
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


print(domain_name(url_))

# --- Solution 02
# def domain_name(url):
#     url = url.replace('www.','')
#     url = url.replace('https://','')
#     url = url.replace('http://','')
    
#     return url[0:url.find('.')]

# ---- solutio 03
# def domain_name(url):
#     headers = ["http://", "https://", "www.", "http://www", "https://www."]
#     for header in headers:
#         if header in url:
#             url = url.replace(header, "")
#     domain = url.split(".")[0]
#     return domain