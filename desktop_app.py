import rumps
import logging

from pprint import pprint

#from apps.scrape.tasks import Scraper
#from apps.mail.tasks import Mail

from commons._save import _save
from commons._mail import _mail
from commons._scrape import _scrape

from utils.utils import notify

rumps.debug_mode(True)


def _notification(_type: str, **kwargs: dict):
  #subtitle = 'Data {"Saved" if _type = "save" else "Sent"}'
  subtitle = 'Process Done..'

  notify(
    title='EpicGames',
    text=kwargs.get('message', 'No-Data')
  )

  # rumps.notification(
  #    title='EpicGames',
  #    subtitle=subtitle,
  #    message=kwargs.get('message', 'No Data')
  #  )


class EpicReminder:
  #scraper = Scraper()
  #mail = Mail()

  def __init__(self):
    # def toggle_button(self, sender):
    #  sender.state = not sender.state

    self.config = {
      "app_name": "EpicReminder",
      "start": "Get Free Games",
      "mail": "Mail",
      "notif": "Save"
    }

    # App
    self.app = rumps.App(self.config['app_name'])

    # Menu
    self.set_up_menu()

    # Options
    self.start_button = rumps.MenuItem(
      title=self.config['start'], callback=self.start)
    self.send_mail_button = rumps.MenuItem(
      title=self.config['mail'], callback=self.send_mail)
    self.save_button = rumps.MenuItem(
      title=self.config['notif'],
      callback=self.save_local)

    self.app.menu = [
      self.start_button,
      self.send_mail_button,
      self.save_button]

  def set_up_menu(self):
    self.app.title = 'EGR'
    self.app.icon = 'docs/Epic-Games-logo.png'

  def start(self, _):
    #data = self.scraper.scrape()
    data = _scrape._scrape()
    if self.send_mail_button.state:
      ret = _mail._mail(data)
      if ret[0]:
        _notification(
          _type='mail',
          message='Your Free Games Alert Sent To Your Mail')
    if self.save_button.state:
      ret = _save._save(data)
      if ret[0]:
        _notification(
          _type='save',
          path=ret[1],
          message=f'You Free Games File Saved to {ret[1]}')

    logging.info(data)

  def send_mail(self, sender):
    sender.state = not sender.state

  def save_local(self, sender):
    sender.state = not sender.state

  def run(self):
    self.app.run()


if __name__ == '__main__':
  app = EpicReminder()
  app.run()
