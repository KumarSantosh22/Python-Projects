# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "<your a/c sid here>"
auth_token = "your auth token here"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+918700004930",
    from_="+15089162594",
    body="Hello Alien!, You are hacked. :) ")