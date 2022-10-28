from twilio.rest import Client

account_sid = 'ACa3892293626495af286ab913180b99c9' 
auth_token = '55a1bcb89bca7558e7fd63954add6494' 
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
            