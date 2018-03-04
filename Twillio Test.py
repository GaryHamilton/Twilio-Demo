from twilio.rest import Client


# The original version of this was taken from a sample on the Twilio web site
# Your Account SID from twilio.com/console
 account_sid = "Your account_sid from Twilio"
# Your Auth Token from twilio.com/console
 auth_token  = "Your Auth Token from Twilio"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+my number",
    from_="+mytwilionumber",
    body="Python Twilio Test!")

# print(message.sid)
print("Confirm Message was sent")