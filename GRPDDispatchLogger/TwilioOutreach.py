from twilio.rest import Client

account_sid = 'ACa3892293626495af286ab913180b99c9' 
auth_token = '93f3319077d2ca9a8e010435497f0b96' 
client = Client(account_sid, auth_token) 

def checkLocations(data):

    streetTest = "Cherry"

    

    for x in range(len(data)):
        if data[x][3].lower().__contains__(streetTest.lower()):
            message = client.messages.create(
                              body=data[x][2] + ' at ' + data[x][3],
                              from_='+16163286950',
                              to='+15158026014')
            print(message.sid)

            #caleb: 6164385547 Leonard
            #phil: 6162954667 Knapp
            #colin: 2692749689 monroe center
            #aaron: 5158026014 pearl

#if when log is generted
#if any watched streets match
#text user watching street
