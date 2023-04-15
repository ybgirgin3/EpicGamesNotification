import unittest
import logging
from pprint import pprint

from apps.scrape.tasks import Scraper


class TestScrape(unittest.TestCase):
  def test_scrape(self):
    scraper = Scraper()
    res = scraper.scrape()
    logging.info(f'''
        output of scrape:
{res}
        ''')
    # self.assertIsInstance(res, dict)


if __name__ == "__main__":
  unittest.main()
