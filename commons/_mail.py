import logging
from apps.mail.tasks import Mail
from apps.scrape.tasks import Scraper


class _mail():
  def _mail(data):
    try:
      m = Mail()        # define mail
      m.send(data=data)  # send mail
      return True, 1
    except Exception as e:
      return False, e
