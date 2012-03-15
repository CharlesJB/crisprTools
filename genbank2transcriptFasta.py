#!/usr/bin/python

import Bio
from Bio import SeqIO

input_handle = open("S_thermo_DGCC7710.gbk", "rU")

count = 0
genome = SeqIO.read(input_handle, "genbank")

for gb_features in genome.features:
	f_type = gb_features.type
	if (f_type != 'gene' and f_type != 'Source' 
	    and f_type != 'fasta_record'):
		header = str(gb_features.qualifiers)
		seqStart = gb_features.location.start
		seqEnd = gb_features.location.end
		print "> " + gb_features.type + " " + header
		print genome.seq[seqStart:seqEnd]

output_handle.close()

print "Converted %i records" % count
