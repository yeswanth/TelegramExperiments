import requests
from bs4 import BeautifulSoup
import csv

url = 'http://telegramstickers.altervista.org/page/%d/'
FILE = 'output.csv'
parsed = []

class StickerModel(object):
    def __init__(self,title,avatar_url,detail_url):
        self.title = title
        self.avatar_url = avatar_url 
        self.detail_url = detail_url 
    def get_model_as_list(self):
        return [self.title,self.avatar_url,self.detail_url]
    def print_model(self):
        print '%s - %s - %s'%(self.title,self.avatar_url,self.detail_url)
    
def parse_article(article):
    try:
        parsed_avatar = article.findAll('a',{'class':'entry-thumb'})[0] 
        title = parsed_avatar['title']
        avatar_url = parsed_avatar.findAll('img')[0]['src'] 
        detail_url = parsed_avatar['href']
        return StickerModel(title,avatar_url,detail_url)
    except IndexError, e:
        return None

def get_sticker_models(articles):
    for article in articles:
        sticker_model = parse_article(article) 
        if(sticker_model):
            parsed.append(sticker_model) 

def get_page(no):
    _url = url%(no)
    r = requests.get(_url)
    b = BeautifulSoup(r.text)  
    articles = b.findAll('article')
    get_sticker_models(articles)
    
def write_output():
    llist = []
    f = open(FILE,'a')
    writer = csv.writer(f,delimiter=',')
    for l in parsed:
        _list = l.get_model_as_list()
        try:
            writer.writerow(_list)
        except UnicodeEncodeError, e:
            print _list

def main():
    for i in range(150,180):
        get_page(i)
    write_output() 

if __name__ == '__main__':
    main()

