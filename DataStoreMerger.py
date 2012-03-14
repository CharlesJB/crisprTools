#!/usr/bin/env python
# encoding: utf-8

"""
usage:

DataStoreMerger.py script.ds


accepted commands in script.ds:

AddEntries columnName dataFile

CreateFile outputFile

Clear

"""

class DataStoreMerger:
	def __init__(self):
		self.clear()

	def clear(self):
		self.genes={}
		self.customColumns=[]
		self.counts={}


	def addEntries(self,columnName,dataFile):
		self.customColumns.append(columnName)

		self.counts[columnName]={}

		for line in open(dataFile):
			tokens=line.split("\t")
			gene=tokens[0]
			geneIdentifier=tokens[1]
			count=tokens[2]

			self.genes[gene]=geneIdentifier

			self.counts[columnName][gene]=count

	def getCustomColumns(self):
		return self.customColumns

	def getGeneIdentifier(self,gene):
		return self.genes[gene]
	
	def getGenes(self):
		return self.genes

	def createOutputFile(self,fileName):
		file=open(fileName, 'w')
		genes=self.getGenes()

		customColumns=self.getCustomColumns()

		file.write("#Gene    GeneIdentifier")

		for column in customColumns:
			file.write("        "+column)

		file.write("\n")

		for gene in genes:
			geneIdentifier=self.getGeneIdentifier(gene)

			file.write(gene+"   "+geneIdentifier)
			for column in customColumns:
				count=self.getCountForGeneAndColumn(gene,column)
				file.write(" "+str.strip(str(count)))
			file.write("\n")
		file.close()

			

	def getCountForGeneAndColumn(self,gene,column):
		if column not in self.counts:
			return 0

		if gene not in self.counts[column]:
			return 0

		return self.counts[column][gene]

class Interpreter:

	def __init__(self):
		self.dataStoreMerger=DataStoreMerger()

	def runCommand(self,command):
		operationCode=command[0]

		if operationCode=="AddEntries":
			columnName=command[1]
			dataFile=command[2]

			self.dataStoreMerger.addEntries(columnName,dataFile)

		elif operationCode=="CreateFile":
			outputFile=command[1]

			self.dataStoreMerger.createOutputFile(outputFile)

		elif operationCode=="Clear":
			self.dataStoreMerger.clear()

	def runCommands(self,commandFile):
		for line in open(commandFile):
			tokens=line.split()

			if len(tokens)<1:
				continue

			self.runCommand(tokens)
		

import sys

if __name__=="__main__":
	if len(sys.argv)!=2:
		print __doc__
		sys.exit(1)

	interpreter=Interpreter()

	commandFile=sys.argv[1]

	interpreter.runCommands(commandFile)

