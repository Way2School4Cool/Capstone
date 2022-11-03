from twilio.rest import Client
from Helper import getAuth, checkTwilioNumbers

account_sid = getAuth("Twilio","Account_SID")
auth_token = getAuth("Twilio", "Authorization_Token")
senderPhone = getAuth("Twilio", "Outbound_Number")
client = Client(account_sid, auth_token)

def checkLocations(data):

	for x in range(len(data)):
		#if data[x][3].lower().__contains__(streetTest.lower()):
		userPhoneNumber = checkTwilioNumbers(data[x][3])
		if userPhoneNumber != "":
			message = client.messages.create(
							  body=data[x][2] + ' at ' + data[x][3],
							  from_='+1' + senderPhone,
							  to='+1' + userPhoneNumber)
			print(message.sid)
		