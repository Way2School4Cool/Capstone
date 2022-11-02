from twilio.rest import Client
from Helper import getAuth

account_sid = getAuth("Twilio","Account_SID")
auth_token = getAuth("Twilio", "Authorization_Token")
client = Client(account_sid, auth_token) 

twilioNumbersLocation = "C:\\AuthTokens\\TwilioNumbers.csv"

def checkLocations(data):

    streetTest = "Leonard"
    
    for x in range(len(data)):
        if data[x][3].lower().__contains__(streetTest.lower()):
            message = client.messages.create(
                              body=data[x][2] + ' at ' + data[x][3],
                              from_='+16163286950',
                              to='+16164385547')
            print(message.sid)
            