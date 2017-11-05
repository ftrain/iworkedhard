from bs4 import BeautifulSoup
import os
import csv
import argparse

MIRROR_DIR='/Users/ford/Dropbox/mirror/'

def walk(site):
    csv_file = open(site + '.csv', 'w')
    csv_writer = csv.writer(csv_file)

    print(MIRROR_DIR + site)

    for root, dirs, files in os.walk(MIRROR_DIR + site):
        for fname in files:
            full_name = u""+os.path.join(root, fname)
            try:
                with open(full_name) as fp:
                    soup = BeautifulSoup(fp, "lxml")
                    metas = soup.find_all('meta')
                    rec = dict([[x.attrs['property'], x.attrs['content']]
                                for x in filter(lambda x: 'property' in x.attrs, metas)])
                    author = rec.get('vr:author')
                    if author is not None:
                        url = "http://web.archive.org/web/*/{}".format(rec.get('og:url'))
                        row = [author, rec.get('og:site_name'), rec.get('og:title'), url]
                        print(row[2])
                        csv_writer.writerow(row)
            except FileNotFoundError as e:
                pass
            except UnicodeDecodeError as e:
                pass


def __main__():
    parser = argparse.ArgumentParser(description='Extract metadata from articles.')
    parser.add_argument('site_dir')
    args = parser.parse_args()
    site_dir = vars(args).get('site_dir')
    walk(site_dir)
    


    


__main__()
    
