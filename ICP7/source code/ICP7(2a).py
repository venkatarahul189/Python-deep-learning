from bs4 import BeautifulSoup
#here i imported the library of url
import urllib.request
#Here i take the URL text by using Beautiful Soap
def search_spider():
#here i take the given url link
    url = "https://en.wikipedia.org/wiki/Google"
#Here i used source code to to covert
    source_code = urllib.request.urlopen(url)
#This is the data taken
    soup = BeautifulSoup(source_code, "html.parser")
    body = soup.find('div', {'class': 'mw-parser-output'})
#this is the file taken here
    file.write(str(body.text))
#this is the input
search = input('type "s" to start wikiScrap, type "q" to quit')
if search == 'q' or search == 'Q':
    print("Quit...")
    exit()
else:
    print("Creating .txt file ...")
    file = open('input.txt', 'a+', encoding='utf-8')
    search_spider()