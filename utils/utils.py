import platform
import os


def notify(title, text):
  if platform.system().lower() == "darwin":
    os.system(
      """
              osascript -e 'display notification "{}" with title "{}"'
            """.format(
        text, title
      )
    )
  elif platform.system().lower() == "linux":
    os.system('notify-send "{}" "{}"'.format(title, text))

  else:  # windows
    try:
      from winotify import Notification
    except ModuleNotFoundError as err:
      raise err
    Notification(app_id="EpicGamesReminder", title=f"{title}", msg=f"{text}")
