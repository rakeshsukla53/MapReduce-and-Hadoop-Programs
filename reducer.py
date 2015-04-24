__author__ = 'rakesh'

import sys
salesTotal = 0.0
oldKey = None
dummy_Data = ["Miami 12.34", "Miami 99.07", "Miami 55.07", "NYC 88.97", "NYC 33.56"]

for line in dummy_Data:
	data = line.strip().split(" ")  #strip is basically used to remove those extra whitespaces
	if len(data) != 2:
		# Something has gone wrong. Skip this line.
        #the length of the input line has to be 2
		continue

	thisKey, thisSale = data
	if oldKey and oldKey != thisKey:
  		print oldKey, ":", salesTotal
  		oldKey = thisKey
  		salesTotal = 0

	oldKey = thisKey
	salesTotal += float(thisSale)

if oldKey != None:
	print oldKey, ":", salesTotal

