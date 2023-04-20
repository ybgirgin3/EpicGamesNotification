import logging
import unittest
from apps.mail.tasks import Mail
from apps.scrape.tasks import Scraper


class TestMail(unittest.TestCase):
  scraper = Scraper()
  m = Mail()

  def test_mail(self):
    # send mail
    self.m.send(
      data=self.scraper.scrape()
    )


if __name__ == "__main__":
  unittest.main()
