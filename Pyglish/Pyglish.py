from urllib2 import urlopen, quote, HTTPError
from bs4 import BeautifulSoup


class Synonyms:
    def __init__(self):
        self.url = None
        self.html = ""
        self.soup = None

    def get_all(self, word, donttouch=False):
        try:
            self.url = urlopen("http://www.thesaurus.com/browse/{}".format(str(quote(word.lower()))))
            self.html = self.url.read()
            self.soup = BeautifulSoup(self.html, 'html.parser')
            synonyms = []
            for link in self.soup.find_all('div'):
                try:
                    class_div = link.get('class')
                    if str(class_div[0]) == "relevancy-list":
                        num = 0
                        for words in link.find_all('span'):
                            not_star = words.get('class')
                            if str(not_star[0]) == "text":
                                synonyms.append(str(words.string))
                        break
                except (AttributeError, TypeError, ValueError):
                    pass
            return synonyms
        except HTTPError:
            return [""]

    def get_best(self, word):
        return self.get_all(word)[0]
