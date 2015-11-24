import time
import settings
from slackclient import SlackClient

sc = SlackClient(settings.TOKEN)
if sc.rtm_connect():
    while True:
        print(sc.rtm_read())
        time.sleep(1)
else:
    print("Connection Failed, invalid token?")