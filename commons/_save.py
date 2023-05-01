import logging
import tempfile
import os
import datetime


class _save:
  def _save(data):
    try:
      #scraper = Scraper()
      #res = scraper.scrape()

      # create dir
      path = os.path.join(
        os.path.join(
          tempfile.gettempdir(),
          f'scraper.output.{datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S")}.csv')
      )
      logging.info(path)

      data.to_csv(path)
      return True, path
    except Exception as e:
      return False, e
