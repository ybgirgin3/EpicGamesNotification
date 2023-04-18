# Epic Games Reminder

## Mail Sender app for weekly epic games free games

**to make it work;**

- create an outlook account
- create a .credentials.json file

  schema of needed file:

  ```json
  {
      "EMAIL": "<your-outlook-account-email>",
      "PASSWORD": "<your-outlook-account-password>"
  }
  ```

**for test run (after complete previous step);**

```sh
~$ python -m unittest test_mail.py
```

**NOTE:**

- I use outlook because, we can not use gmail to send mail for free anymore. We need business account for create a mail sender bot (a.k.a: no unsecure apps anymore)

mail example: <br>
<img src='docs/images/mail.png'/>
