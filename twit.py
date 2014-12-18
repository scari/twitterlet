#!/usr/bin/env python2
# coding: utf8

import twitter
from local_setting import *

TWITTER_ACCOUNT = {
    'access_token_secret': SCARIBOT_ACCESS_SECRET,
    'access_token_key': SCARIBOT_ACCESS_TOKEN,
    'consumer_secret': SCARIBOT_CONSUMER_SECRET,
    'consumer_key': SCARIBOT_CONSUMER_KEY
}

t = twitter.Api(**TWITTER_ACCOUNT)

def dm(screen_name, message):
    if screen_name and message:
        return t.PostDirectMessage(screen_name=screen_name, text=message)

#print(t.VerifyCredentials())
