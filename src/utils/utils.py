import os
import platform
import subprocess

_os = platform.system().lower()


def notify(title, text):
    if _os == "darwin":
        os.system(
            """
              osascript -e 'display notification "{}" with title "{}"'
            """.format(
                text, title
            )
        )
    elif _os == "linux":
        os.system('notify-send "{}" "{}"'.format(title, text))

    else:  # windows
        try:
            from winotify import Notification
        except ModuleNotFoundError as err:
            raise err
        Notification(app_id="EpicGamesReminder", title=f"{title}", msg=f"{text}")


def open_file(path: str):
    if _os == "darwin":
        subprocess.call(("open", path))
    elif _os == "linux":
        subprocess.call(("xdg-open", path))
    else:
        os.startfile(path)
