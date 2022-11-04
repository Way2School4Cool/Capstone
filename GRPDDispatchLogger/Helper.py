dispatchParseDoc = "DispatchAbbreviations.txt"
authKeysLocation = "C:\\AuthTokens\\Tokens.csv"
twilioNumbersLocation = "C:\\AuthTokens\\TwilioNumbers.csv"

def getAuth(site, tokenName):
	with open(authKeysLocation, mode="r", newline="") as authFile:
		for auth in authFile:
			auth = auth.split(",")
			if auth[0] == site and auth[1] == tokenName:
				return auth[2]
	return ""


def dispatchCodeParser(dispatchArea):
	with open(dispatchParseDoc, mode="r", newline="") as parseFile:

		for dispatchCode in parseFile:
			
			if dispatchArea.__contains__(dispatchCode[0:dispatchCode.find(":")]):
				return dispatchCode[0:dispatchCode.find(":")]

	return ""


def checkTwilioNumbers(street):
	with open(twilioNumbersLocation, mode="r", newline="") as userInfo:
		for user in userInfo:
			user = user.split(",")
			if  street.__contains__(user[2].upper()):
				return user[1]

	return ""