import logging
from pprint import pprint

from apps.scrape.tasks import Scraper


class _scrape():
  def _scrape():
    scraper = Scraper()
    res = scraper.scrape()
    # logging.info(f'''
    #    output of scrape:
    #    {res}
    #    ''')
    return res
