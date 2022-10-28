#Team Crime 9/13
#Version 0.1

import csv
import os
from datetime import date, datetime
from pathlib import Path
from TwilioOutreach import checkLocations

dispatchParseDoc = "DispatchAbbreviations.txt"

def writeToCSV(data):
	
	writeData = data
	#check if file exists
	dateFileName = str(date.today().year) + "-" + str(date.today().month) + "-" + str(date.today().day) + "DispatchLog.csv"
	
	path = Path(os.getcwd() + "..//..//PDLogs//" + dateFileName)
	
	dateFileName = "..//..//PDLogs//" + dateFileName

	if not path.is_file():
		with open(dateFileName, 'w') as fileCreation:
			fileCreation.close

	#check if they are already in the csv:
	with open(dateFileName, mode="r", newline="") as dispatchFile:
		reader = csv.reader(dispatchFile)

		finishedLooping = False
		dataLog = []

		for dispatchLog in reader:
			dataLog.append([dispatchLog[0], dispatchLog[1], dispatchLog[2], dispatchLog[3]])
			for x in range(len(writeData)):
			#if so, do nothing
				if not finishedLooping \
					and (datetime.strptime(dispatchLog[0], '%m/%d/%Y') > datetime.strptime(writeData[x][0], '%m/%d/%Y') \
					or dispatchLog[1] >= writeData[x][1]) :
					
					#and dispatchLog[2] == writeData[-x][2] \
					#and dispatchLog[3] == writeData[-x][3]:
				
					writeData = writeData[0:x - 1]
					finishedLooping = True
					break


	writeData = writeData + dataLog
	checkLocations(dataLog)
	
		#append the users mentioned to the list
	with open(dateFileName, mode="w", newline="") as dispatchFile:
		writer = csv.writer(dispatchFile)
		
		#Clean up data
		for newLine in writeData:

			if newLine[2] == "":
				newLine[2] = dispatchCodeParser(newLine[3])
				newLine[3] = newLine[3][len(newLine[2]):]
					
			elif newLine[3] == "":
				codeAreaPlaceholder = newLine[2]
				newLine[2] = dispatchCodeParser(newLine[2])
				newLine[3] = codeAreaPlaceholder[len(newLine[2]):]

			else:
				newLine[3] = newLine[3][0 + len(newLine[2]):]
				
			writer.writerow(newLine)

def dispatchCodeParser(dispatchArea):
	with open(dispatchParseDoc, mode="r", newline="") as parseFile:
		reader = csv.reader(parseFile)

		for dispatchCode in parseFile:
			
			#TODO: if dispatch area starts with a letter, the code is probably wrong (or check a for a "/")
			if dispatchArea.__contains__(dispatchCode[0:dispatchCode.find(":")]):
				return dispatchCode[0:dispatchCode.find(":")]

	return ""