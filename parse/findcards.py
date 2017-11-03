from bs4 import BeautifulSoup

with open("/Users/ford/Desktop/websites/gothamist.com/2017/01/01/buckle_up_sherlock_season_4_opener.php") as fp:
    title = None
    author = None
    date = None
    publication = None
    soup = BeautifulSoup(fp, "lxml")
    metas = soup.find_all('meta')
    rec = dict([[x.attrs['property'], x.attrs['content']]
                      for x in filter(lambda x: 'property' in x.attrs, metas)])
    print(rec.get('vr:author'), rec.get('og:title'))

