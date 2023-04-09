from apps.scrape.tasks import Scraper
import pprint

scraper = Scraper()

res = scraper.scrape()
pprint.pprint(res)
