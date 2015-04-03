from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC2a296157780128730c02d31c8df41e40"
auth_token  = "{{auth}}"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Testing text message",
    to="+1myphone",    # Replace with your phone number
    from_="+15005550006") # Replace with your Twilio number
print message.sid
