# Web Scrapping

# Used to extract content or data from a website.
# Example: emails, location, business, flight data etc.
# External module bs4, requests, lxml

# Example 1: 
# import requests
# res = requests.get("https://en.wikipedia.org/wiki/Robots.txt")
# print(res)
# txt = res.text
# print(txt)

# Example 2: 
# import requests
# res = requests.get("https://analytics.usa.gov/data/live/browsers.json")
# print(res)
# txt = res.text
# txt = res.json()
# txt = (res.json()['totals']['browser'])
# txt = (res.json()['query']['dateRanges'][0]['startDate'])
# print(txt)

# Optimized code: 

# print(requests.get("https://en.wikipedia.org/wiki/Robots.txt").text)
# print(requests.get("https://analytics.usa.gov/data/live/browsers.json").json()['totals']['browser'])
# print(requests.get("https://analytics.usa.gov/data/live/browsers.json").json()['query']['dateRanges'][0]['startDate'])

# Example 3:
# BeautifulSoup - external module, using this we can handle html tags, classes and id.

# from urllib.request import urlopen
# from bs4 import BeautifulSoup 

# html = urlopen('https://www.wikipedia.org')
# bs = BeautifulSoup(html, 'html.parser')
# print(bs)

# To get text from some class:

# nameList = bs.findAll('a', {'class':'link-box'})
# for name in nameList:
#   print(name.get_text())

# nameList = bs.findAll('a', {'class':'jsl10n'})
# for name in nameList:
#   print(name.get_text())

# nameList = bs.findAll('p', {'class':'jsl10n'})
# for name in nameList:
#   print(name.get_text())

# import re

# html = urlopen('https://pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# images = bs.find_all('img', {'src':re.compile('.jpg')})
# for img in images:
#   # print(images)
#   # print(img)
#   print(img['src']+'\n')

# help('bs4')
# import requests
# req = requests.get('https://makeawebsitehub.com/social-media-sites/')
# req = requests.get('https://buffer.com/library/social-media-sites/')
# facelinks = [fa for fa in req if 'https://www.facebook.com/']
# # print(facelinks)
  
# for fa in facelinks:
#   print(fa)

# Header info about the response
# import requests
# res = requests.get('https://www.python.org/')
# print("Status: ", res.status_code)
# print("Headers: ", res.headers)
# print("URL: ", res.url)
# print("History: ", res.history)
# print("Encoding: ", res.encoding)
# print("Cookies: ", res.cookies)
# print("Content: ", res._content)


# import requests
# from bs4 import BeautifulSoup

# Printing Date, Time and Topic
# res = requests.get('https://www.python.org/')
# soup = BeautifulSoup(res.text, "html.parser")
# upcoming = soup.find("div", class_="shrubbery")
# events = upcoming.findAll("li")

# for event in events:
#   # print(event)
#   # data = event.find('time')['datetime'].text.strip()
#   # title = event.find("a").text.strip()
#   # print(data + "-" + title)
#   print(event.find('time')['datetime'], "-", event.find("a").text.strip())

# Printing Headlines 
# res = requests.get('https://www.python.org/')
# soup = BeautifulSoup(res.text, "html.parser")
# headlines = soup.find_all('ul', class_='menu')
# for hl in headlines:
#   print(hl.text.strip())

# Printing Headers
# import requests
# res = requests.get('https://www.python.org/psf/donations/')
# soup = BeautifulSoup(res.text, "html.parser")
# headings = soup.findAll(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
# texts = [he.get_text() for he in headings]
# for txt in texts:
#   print(txt.strip())

# Printing anchor tags' text
# import requests
# res = requests.get('https://www.python.org/psf/donations/')
# soup = BeautifulSoup(res.text, "html.parser")
# headings = soup.findAll(['a'])
# texts = [he.get_text() for he in headings]
# for txt in texts:
#   print(txt.strip())

# Printing title paragraph content, length
# import requests
# res = requests.get('https://www.python.org/psf/donations/')
# soup = BeautifulSoup(res.text, "html.parser")
# print(soup.title)
# print(soup.findAll('p'))
# print(len(soup.findAll('p')))
# print(soup.find(href="https://google.com"))

