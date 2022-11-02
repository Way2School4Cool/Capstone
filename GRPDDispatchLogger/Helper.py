import csv

authKeysLocation = "C:\\AuthTokens\\Tokens.csv"

def getAuth(site, tokenName):
	with open(authKeysLocation, mode="r", newline="") as authFile:
		reader = csv.reader(authFile)
		for auth in authFile:
			auth = auth.split(",")
			if auth[0] == site and auth[1] == tokenName:
				return auth[2]
	return ""