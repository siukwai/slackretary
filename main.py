import time
from slackclient import SlackClient

#token = "xoxb-15173171061-zsOq9I0KFNFW7vYa6tWdrXtm"# found at https://api.slack.com/web#authentication
token = "xoxp-4716502579-4716502587-15168575377-db3199a91c" #main user account token
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        print(sc.rtm_read())
        time.sleep(1)
else:
    print("Connection Failed, invalid token?")