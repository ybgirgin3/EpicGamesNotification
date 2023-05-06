import logging

import rumps

from commons._mail import _mail
from commons._save import _save
from commons._scrape import _scrape
from utils.utils import notify, open_file

# from apps.scrape.tasks import Scraper
# from apps.mail.tasks import Mail

rumps.debug_mode(True)


def _notification(_type: str, **kwargs: dict):
  # subtitle = 'Data {"Saved" if _type = "save" else "Sent"}'
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
  # scraper = Scraper()
  # mail = Mail()

  def __init__(self):

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
    # sub
    self.save_button_jr = rumps.MenuItem('Just Save', callback=self.save_local)
    self.open_directly_button = rumps.MenuItem(
      'Open Directly', callback=self._open)

    # main
    self.start_button = rumps.MenuItem(
      title=self.config['start'], callback=self.start, key='e')
    self.send_mail_button = rumps.MenuItem(
      title=self.config['mail'], callback=self.send_mail)
    self.save_button = rumps.MenuItem(
      self.config['notif']), (self.save_button_jr, self.open_directly_button)

    self.app.menu = [
      self.start_button,
      self.send_mail_button,
      self.save_button]

  def set_up_menu(self):
    self.app.title = 'EGR'
    self.app.icon = 'docs/Epic-Games-logo.png'

  def start(self, _):
    # data = self.scraper.scrape()
    data = _scrape._scrape()
    if self.send_mail_button.state:
      ret = _mail._mail(data)
      if ret[0]:
        _notification(
          _type='mail',
          message='Your Free Games Alert Sent To Your Mail')
    if self.save_button_jr.state:
      ret = _save._save(data)
      if ret[0]:
        _notification(
          _type='save',
          path=ret[1],
          message=f'You Free Games File Saved to {ret[1]}')
      if self.open_directly_button.state:
        print('OPENING FILE')
        open_file(ret[1])

    logging.info(data)

  def send_mail(self, sender):
    sender.state = not sender.state

  def save_local(self, sender):
    sender.state = not sender.state

  def _open(self, sender):
    sender.state = not sender.state
    self.save_button_jr.state = True

  def run(self):
    self.app.run()


if __name__ == '__main__':
  app = EpicReminder()
  app.run()
