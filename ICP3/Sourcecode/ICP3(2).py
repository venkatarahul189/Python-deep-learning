#print out the title of the page
from bs4 import BeautifulSoup
import requests
html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
soup = BeautifulSoup(html.content, "html.parser")
print(soup.title)
#Find all the links in the page 'a'
text = open("file.txt", "a+")
for link in soup.find_all('a'):
    text.write("\n")
    text.write(str(link.get('href')))
text.close()