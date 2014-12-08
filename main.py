#!/bin/python2

#import urllib
from pyquery import PyQuery as pq
#from lxml import etree


class AvisLimitPriceFinder:

    URL = 'http://www.avis-taiwan.com/tw/limited%20offer/limited%20offer/limited%20offer.html'

    def run(self):
        d = pq(url=self.URL)

        for p in d('table').find('tbody').find('tr'):
            print(pq(p).text())
        #print(p.text())
        #print(p.html())




if __name__ == '__main__':
    finder = AvisLimitPriceFinder()

    finder.run()

