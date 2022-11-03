#Team Crime 9/13
#Version 0.1

import csv
import os
from datetime import date, datetime
from pathlib import Path
from TwilioOutreach import checkLocations
from Helper import dispatchCodeParser

def writeToCSV(data):
	
	writeData = data
	loggingPath = Path(os.getcwd())
	fileCreationNeeded = False
	
	#check if file exists
	dateFileName = str(date.today().year) + "-" + str(date.today().month) + "-" + str(date.today().day) + "DispatchLog.csv"
	
	loggingPath = os.path.dirname(loggingPath)
	loggingPath = os.path.dirname(loggingPath) + "\\PDLogs\\" + dateFileName
	
	dateFileName = "..\\..\\PDLogs\\" + dateFileName

	if not os.path.isfile(loggingPath):
		with open(dateFileName, 'w') as fileCreation:
			fileCreation.close()
			fileCreationNeeded = True

	#check if they are already in the csv:
	with open(dateFileName, mode="r", newline="") as dispatchFile:
		reader = csv.reader(dispatchFile)
		finishedLooping = False
		dataLog = []

		for dispatchLog in reader:
			dataLog.append([dispatchLog[0], dispatchLog[1], dispatchLog[2], dispatchLog[3]])
	
			if not finishedLooping:
	
				for x in range(len(writeData)):
				
					#if so, do nothing
					if (datetime.strptime(dispatchLog[0], '%m/%d/%Y') > datetime.strptime(writeData[x][0], '%m/%d/%Y')) or \
						(datetime.strptime(dispatchLog[0], '%m/%d/%Y') == datetime.strptime(writeData[x][0], '%m/%d/%Y') and dispatchLog[1] >= writeData[x][1]):
							writeData = writeData[0: x]
							finishedLooping = True
							break

	for x in range(len(writeData)):
		if writeData[x][2] == "":
			writeData[x][2] = dispatchCodeParser(writeData[x][3])
			writeData[x][3] = writeData[x][3][len(writeData[x][2]):]
					
		elif writeData[x][3] == "":
			codeAreaPlaceholder = writeData[x][2]
			writeData[x][2] = dispatchCodeParser(writeData[x][2])
			writeData[x][3] = codeAreaPlaceholder[len(writeData[x][2]):]

		else:
			writeData[x][3] = writeData[x][3][0 + len(writeData[x][2]):]
	
	#checkLocations(writeData)
	writeData = writeData + dataLog
	
	
	#append the users mentioned to the list
	with open(dateFileName, mode="w", newline="") as dispatchFile:
		writer = csv.writer(dispatchFile)
		
		#Clean up data
		for newLine in writeData:
			writer.writerow(newLine)

	dispatchFile.close()
