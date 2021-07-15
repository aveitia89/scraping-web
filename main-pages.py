from scraping import Crawler

def main():
    print("Comenzando el scrapping")
    crawler = Crawler()
    crawler.parseAllPages()        
    print("Scraping terminado con exito")
main() 