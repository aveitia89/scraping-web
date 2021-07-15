from scraping import Crawler
from timer import timer

@timer(sec = 60)
def mainTimer():
    crawler = Crawler()
    crawler.parseFirtsPage()
    
mainTimer()