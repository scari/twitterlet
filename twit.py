#!/usr/bin/env python3

from twython import Twython
from local_setting import *

TWITTER_ACCOUNT = {
    'oauth_token_secret': SCARIBOT_ACCESS_SECRET,
    'oauth_token': SCARIBOT_ACCESS_TOKEN,
    'app_secret': SCARIBOT_CONSUMER_SECRET,
    'app_key': SCARIBOT_CONSUMER_KEY
}
MAX_LEN = 140
t = Twython(**TWITTER_ACCOUNT)

def dm(screen_name, message):
    if screen_name and message:
        if len(message) > MAX_LEN:
            head = message[:MAX_LEN]
            message = message[MAX_LEN:]
            t.send_direct_message(screen_name=screen_name, text=head)
        else:
            t.send_direct_message(screen_name=screen_name, text=message)
            return

        return dm(screen_name, message)
