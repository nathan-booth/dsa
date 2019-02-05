import requests
import string

from bs4 import BeautifulSoup
from collections import Counter


url = "https://bbc.com/news"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll('a')

links_list = []
for link in links:
  href = link.get('href')
  if href.startswith("/news") and href[-1].isdigit():
    links_list.append("https://bbc.com" + href)

# links_list = ["https://bbc.com" + link.get('href') for link in links if link.get('href').startswith("/news") and link.get('href')[-1].isdigit()]

links_list_unique = list(set(links_list))
for index, link in enumerate(links_list_unique):
  print(index, link)

nouns_list = []
for url in links_list_unique[:10]:
  print("Fetching {}".format(url))
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, "html.parser")

  words = soup.text.split()
  nouns = [word for word in words if word.isalpha() and word[0] in string.ascii_uppercase]
  nouns_list += nouns

for word, count in Counter(nouns_list).most_common(100):
    print(word, count)
