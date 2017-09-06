from twilio.rest import Client
from credential import account_sid, auth_token, my_cell, my_twilio

account_sid = "paste your account_sid here"
auth_token = "paste your account token here"
client = Client(account_sid, auth_token)
client.messages.create(
  to="type your mobile number without space",
  from_="type your twilio number without space",
  body="Here you can type your text. which should be reach your mobile")
