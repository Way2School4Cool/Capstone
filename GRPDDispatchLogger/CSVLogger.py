#Team Crime 9/13
#Version 0.1

from asyncore import write
import csv
from datetime import date
from pathlib import Path
import os

def writeToCSV(data):
	
	writeData = data
	#check if file exists
	dateFileName = str(date.today().year) + "-" + str(date.today().month) + "-" + str(date.today().day) + "DispatchLog.csv"
	
	path = Path(os.getcwd() + "//" + dateFileName)
	
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
					and (dispatchLog[0] > writeData[x][0] \
					or dispatchLog[1] >= writeData[x][1]) :
					
					#and dispatchLog[2] == writeData[-x][2] \
					#and dispatchLog[3] == writeData[-x][3]:
				
					writeData = writeData[0:x - 1]
					finishedLooping = True
					break


	writeData = dataLog + writeData

	#append the users mentioned to the list
	with open(dateFileName, mode="w", newline="") as dispatchFile:
		writer = csv.writer(dispatchFile)
		for newLine in writeData:
			writer.writerow(newLine)