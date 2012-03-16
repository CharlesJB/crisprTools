#!/usr/bin/python
# encoding: utf-8

"""
usage:

DataStoreMerger.py <fileName>
fileName: File in genbanks format

"""

import sys
import Bio
from Bio import SeqIO

def getFeatureQualifier(gb_features, qualifier):
	answer=""
	for value in gb_features.qualifiers:
		if value == qualifier:
			answer =  gb_features.qualifiers[value]
	
	if answer != "":
		return answer
	else:
		print 'Incorrect qualifier: ' + qualifier
		sys.exit(1)

if __name__=="__main__":
	if len(sys.argv)!=2:
		print __doc__
		sys.exit(1)

	fileName=sys.argv[1]
	input_handle = open(fileName, "rU")

	count = 0
	genome = SeqIO.read(input_handle, "genbank")

	for gb_features in genome.features:
		f_type = gb_features.type
		if (f_type != 'gene' and f_type != 'source' 
		    and f_type != 'Source' and f_type != 'fasta_record'):
			header = str(gb_features.qualifiers)
			seqStart = gb_features.location.start
			seqEnd = gb_features.location.end
			print ">",
			print getFeatureQualifier(gb_features, "protein_id"),
			print "|product: ",
			print getFeatureQualifier(gb_features, "product"),
			print " (",
			print getFeatureQualifier(gb_features, "db_xref"),
			print  ")"
			#print ">" + gb_features.protein_id + "|product:" + gb_features.product + " (" + gb_features.db_xref + ")" 
			print genome.seq[seqStart:seqEnd]

	input_handle.close()
