import logging
import unittest
from apps.mail.tasks import Mail
from apps.scrape.tasks import Scraper


class TestMail(unittest.TestCase):
  def test_mail(self):
    # get data
    scraper = Scraper()
    res = scraper.scrape()

    # send mail
    m = Mail(data=res)
    m.send()


if __name__ == "__main__":
  unittest.main()
